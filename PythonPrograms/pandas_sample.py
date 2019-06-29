import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = np.ones(3)
b = np.array([3,8,7])
plt.plot(b)
plt.show()

data = pd.DataFrame({'Country':['India','US','Canada','Austraila','Dubai'],
                     'Rank':[121,40,100,130,11]})

print(data)

print(data.describe())

print(data.info())

data = pd.DataFrame({'Group':['a','a','a','b','b','b','c','c','c'],
                     'ounces':[4,3,12,6,3,5,6,5,6]})
print(data)
print(data.sort_values(by=['ounces'], ascending=True, inplace=False))

print(data.sort_values(by=['Group','ounces'], ascending=[True,False], inplace=False))
#data = pd.DataFrame
# Pandas - Panel Data,

data = pd.read_csv('myCsv.csv',delimiter=',',names=['Names','Age','Active'])
#data = pd.read_csv('Events.csv',delimiter=',')
print(data)
print(data.head(7))
print(data.tail())
print(data.sample(5))
print(data[data.Age=='21'].head(1))
plt.plot(data)
plt.show()
data = pd.DataFrame({'K1':['One']*3 + ['Two']*4, 'K2': [4,4,3,3,4,2,1]})
print(data)
print(data.drop_duplicates())
print(data.drop_duplicates(subset='K1'))
