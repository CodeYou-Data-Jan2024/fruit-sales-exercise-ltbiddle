# add your code here
import pandas as pd

data = {'Apples': [35, 21], 'Bannanas': [41, 34]}

df = pd.DataFrame(data, index=['2017 Sales', '2018 Sales'])

df.to_csv('/Users/lancebiddle/CodeYou/fruit-sales-exercise-ltbiddle/fruit.csv')

print(df)