import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"

response = requests.get("http://books.toscrape.com")

soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    print(f"Title: {title}\nPrice: {price}\n")


book_data = []
books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    print(f"Title: {title}\nPrice: {price}\n")
    book_data.append({"Title": title, "Price": price})

    df = pd.DataFrame(book_data)
    print(df) 


# Enhanced code to convert book prices from GBP to INR and organize files
book_data = []
conversion_rate = 104 

for book in books:
    title = book.h3.a['title']
    price_gbp = book.find('p', class_='price_color').text  
    
    price_gbp_cleaned = price_gbp.replace('£', '').replace('Â', '').strip()
    
    try:
        # Convert cleaned price to float
        price_gbp_value = float(price_gbp_cleaned) if price_gbp_cleaned else 0.0
        
        # Convert to INR
        price_inr = price_gbp_value * conversion_rate
        
        
        print(f"Title: {title}\nPrice (GBP): £{price_gbp_value:.2f}\nPrice (INR): ₹{price_inr:.2f}\n")
        book_data.append({
            "Title": title,
            "Price (GBP)": f"£{price_gbp_value:.2f}",
            "Price (INR)": f"₹{price_inr:.2f}"
        })
    except ValueError:
        print(f"Error converting price for '{title}': {price_gbp}")


# Convert book data to DataFrame
import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)
            ext = ext[1:].upper()  
            if not ext:
                continue
            dest_folder = os.path.join(folder_path, ext)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, filename))





# Plotting the top 10 books by price in INR
import matplotlib.pyplot as plt 
import seaborn as sns   
df = pd.DataFrame(book_data)
df['Price (INR)'] = df['Price (INR)'].replace('₹', '', regex=True).astype(float)
top10 = df.sort_values('Price (INR)', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top10['Title'], y=top10['Price (INR)'])
plt.xticks(rotation=45)
plt.title('Top 10 Books by Price')
plt.xlabel('Books')
plt.ylabel('Price (INR)')
plt.show()