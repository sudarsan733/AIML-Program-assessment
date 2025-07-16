import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr)
print()
print()

reshaped = arr.reshape(3,4)
print(reshaped)
print()
print()

array = ([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
flattened = reshaped.flatten()
print(flattened)
print()
print()

flattened = reshaped.flatten()
flattened[0] = 99
print(flattened)
print()
print(reshaped)
print()

reveled = reshaped.ravel()
reveled[1] = 88
print(reveled)
print()

print(reshaped)
print()

arr1 = np.array([1,2,3])
print(arr1)
arr2 = np.array([2,3,4])
print(arr2)
print()
print()

print(arr1+arr2)
print()

print(arr1+4)# ?
print()


arr1 = np.array([1,2,3])
print(arr1)
arr2 = np.array([[2],[4],[6]])
print(arr2)
print()
print()
print(arr1+arr2)
________________________________________________________________________________________________________________________________________________________________________

import numpy as np  
import pandas as pd
np.random.seed(42)
apartments = [f"Apt_{i}" for i in range(1, 21)]
dates = pd.date_range(start="2025-07-15", periods=30, freq="D")
data = {"date":np.tile(dates , len(apartments)),
        "Apartment":np.repeat(apartments,len(dates)),
        "Electricity_usage":np.random.normal(loc=20,scale=5,size=len(dates)*len(apartments))}
df = pd.DataFrame(data)
df["Electricity_usage"]= df["Electricity_usage"].round(2)
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)
usage_by_apartment = df.groupby("Apartment")["Electricity_usage"].sum().sort_values(ascending=False)   
print(usage_by_apartment)
daily_avg = df.groupby("date")["Electricity_usage"].mean()
print(daily_avg.head())


import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(12, 6))
sns.barplot(x=usage_by_apartment.index, y=usage_by_apartment.values)
plt.xticks(rotation=90)
plt.title("TOTAL USAGE PER APARTMENT")
plt.xlabel("Apartment")
plt.ylabel("Total KWH")
plt.tight_layout()
plt.show()     


plt.figure(figsize=(12, 6))
sns.lineplot(x=daily_avg.index, y=daily_avg.values)
plt.title("DAILY AVERAGE ELECTRICITY USAGE")
plt.xlabel("Date")
plt.ylabel("Average KWH")
plt.tight_layout()
plt.show()


threshold = df["Electricity_usage"].mean() + 2 * df["Electricity_usage"].std()
df["High_usage"] = df["Electricity_usage"] > threshold
print(df[df["High_usage"] == True].head())
________________________________________________________________________________________________________________________________________________________________________

#assessment - Employee working hours analysis

import numpy as np
import pandas as pd
np.random.seed(42)
employee_ids = [f"EMP_{i:03d}" for i in range (1,31)]
dates = pd. date_range(start="2025-07-01",periods=30, freq="D")

data = {

 "Date": np.tile(dates, len(employee_ids)),
 "Employee_ID" : np.repeat(employee_ids, len(dates)),
 "Working_Hours": np.random.uniform(4, 10, size=len(dates)
* len(employee_ids)).round(2)
}
df = pd.DataFrame(data)

df.to_csv("D:\employee_working_hours.csv", index=False)

df_csv = pd.read_csv("employee_working_hours.csv")
row = df.iloc[52]
print(row)

print(df_csv.head())
print(df_csv.describe())
print(df_csv["Employee_ID"].nunique())


total_hours =df_csv.groupby("Employee_ID")["Working_Hours"].sum().sort_values(ascending=False)


avg_daily =df_csv.groupby("Employee_ID")["Working_Hours"].mean()

threshold_low = 5
threshold_high = 9
df_csv["Low_Hour_Flag"] = df_csv["Working_Hours"] <threshold_low
df_csv["High_Hour_Flag"]=df_csv["Working_Hours"] >threshold_high

print(df_csv[df_csv["Low_Hour_Flag"] |
df_csv["High_Hour_Flag"]].head())
       
import matplotlib.pyplot as plt
import seaborn as sns

top10 = total_hours.head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top10.index, y=top10.values)
plt.xticks(rotation=45)
plt.title("Top 10 Employees by Total working Hours")
plt.ylabel("Hours")
plt.tight_layout()
plt.show()