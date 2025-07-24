import os
import pandas as pd
import numpy as np
import mysql.connector
import logging
from datetime import datetime

# ===================== LOGGING SETUP =====================
logging.basicConfig(
    filename='etl_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("ETL Process Started")

# ===================== STEP 1: EXTRACT =====================
try:
    data_dir = 'D:/python class/AI&ML/employees1'
    files = [f for f in os.listdir(data_dir) if f.endswith('D:/python class/AI&ML/employees1.csv')]

    df_list = [pd.read_csv(os.path.join(data_dir, file)) for file in files]
    df = pd.concat(df_list, ignore_index=True)

    logging.info(f"{len(files)} CSV files read and combined successfully.")
except Exception as e:
    logging.error(f"Error during extraction: {e}")
    raise

# ===================== STEP 2: TRANSFORM =====================
try:
    
    df.fillna({
        'Quantity_Sold': 0,
        'Unit_Price': 0.0,
        'Discount_Percent': 0.0,
        'Payment_Mode': 'Unknown'
    }, inplace=True)

    
    df['Total_Sale_Value'] = (
        df['Quantity_Sold'] * df['Unit_Price'] * (1 - df['Discount_Percent'] / 100)
    )

   
    df.columns = df.columns.str.lower()

    
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    
    df.dropna(subset=['date'], inplace=True)

    
    df.drop_duplicates(subset=['store_id', 'date', 'product_id'], inplace=True)

    
    bins = [0, 500, 2000, np.inf]
    labels = ['Low', 'Medium', 'High']
    df['sale_category'] = pd.cut(df['total_sale_value'], bins=bins, labels=labels)

    logging.info("Transformation completed successfully.")
except Exception as e:
    logging.error(f"Error during transformation: {e}")
    raise

# ===================== STEP 3: LOAD TO MYSQL =====================
try:
    conn = mysql.connector.connect(
        host='"127.0.0.1"',
        user='root',         
        password='Root123@',     
        database='employees'      
    )
    cursor = conn.cursor()

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS retail_sales (
            store_id VARCHAR(50),
            date DATE,
            product_id VARCHAR(50),
            product_name VARCHAR(100),
            quantity_sold INT,
            unit_price FLOAT,
            discount_percent FLOAT,
            payment_mode VARCHAR(20),
            total_sale_value FLOAT,
            sale_category VARCHAR(10),
            PRIMARY KEY (store_id, date, product_id)
        )
    ''')
    conn.commit()

    insert_query = '''
        INSERT INTO retail_sales (
            store_id, date, product_id, product_name,
            quantity_sold, unit_price, discount_percent,
            payment_mode, total_sale_value, sale_category
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE
        total_sale_value = VALUES(total_sale_value),
        sale_category = VALUES(sale_category)
    '''

    for _, row in df.iterrows():
        cursor.execute(insert_query, (
            row['store_id'], row['date'].date(), row['product_id'],
            row['product_name'], int(row['quantity_sold']),
            float(row['unit_price']), float(row['discount_percent']),
            row['payment_mode'], float(row['total_sale_value']),
            row['sale_category']
        ))

    conn.commit()
    cursor.close()
    conn.close()

    logging.info("Data loaded to MySQL successfully.")
except Exception as e:
    logging.error(f"Error during loading to MySQL: {e}")
    raise

# ===================== STEP 4: ANALYSIS & REPORT =====================
try:
    
    store_sales = df.groupby('store_id')['total_sale_value'].sum().reset_index()
    store_sales.to_csv('store_sales_summary.csv', index=False)

   
    top_products = df.groupby('product_name')['total_sale_value'].sum().nlargest(5).reset_index()
    top_products.to_csv('top_5_products.csv', index=False)


    daily_trend = df.groupby(['date', 'store_id'])['total_sale_value'].sum().reset_index()
    daily_trend.to_csv('daily_sales_trend.csv', index=False)

    logging.info("Analysis reports generated successfully.")
except Exception as e:
    logging.error(f"Error during analysis/reporting: {e}")
    raise

logging.info("ETL Process Completed")
