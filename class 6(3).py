
import pandas as pd
import numpy

csv_url ='https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(csv_url)
print(df.head())

stud_alcoh = df.loc[: , "school":"guardian"]
print(stud_alcoh.head())

capitalizer = lambda x: x.capitalize()

stud_alcoh['Mjob'].apply(capitalizer)
stud_alcoh['Fjob'].apply(capitalizer)

print(stud_alcoh.tail())


stud_alcoh['Mjob'] = stud_alcoh['Mjob'].apply(capitalizer)
stud_alcoh['Fjob'] = stud_alcoh['Fjob'].apply(capitalizer)
print(stud_alcoh.tail())

def majority(x):
   if x > 17:
      return True
   else:
     return False
   
stud_alcoh['legal_drinker'] = stud_alcoh['age'].apply(majority)
print(stud_alcoh.head())

def times10(x):
   if type(x) is int:
     return 10 * x
   return x

stud_alcoh.applymap(times10).head(10)
