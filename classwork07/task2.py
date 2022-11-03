import pandas as pd
import matplotlib.pyplot as plt

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

#1
more_than_5 = diamonds[(diamonds.x > 5) & (diamonds.y > 5) & (diamonds.z > 5)]
print(more_than_5, end = '\n \n \n')
#2
numbers = diamonds[[c for c in diamonds if diamonds.dtypes.loc[c] != 'object']]
print(numbers, end = '\n \n \n')
print(numbers.mean(), end = '\n \n \n')
#3


#4,5
cut_price = diamonds.groupby(['cut']).agg({'price': "mean"})

cut_price.plot()                                                                                                                 #4
plt.legend(["average price"])                                                                                                   #4
plt.show()                                                                                                                      #4

#6
df['carat'].fillna(df['carat'].mean(), inplace = True)
df['cut'].fillna(df['cut'].mean(), inplace = True)
df['color'].fillna(df['color'].mean(), inplace = True)
df['clarity'].fillna(df['clarity'].mean(), inplace = True)
df['depth'].fillna(df['depth'].mean(), inplace = True)
df['table'].fillna(df['table'].mean(), inplace = True)
df['price'].fillna(df['price'].mean(), inplace = True)


#7
diamonds['carat'].hist(bins = 100)
plt.show()

print(diamonds.isnull().sum().sum(), end = '\n \n \n')

znach = diamonds.dropna(axis = 0, how = 'any', inplace = False)
print(znach, end = '\n \n \n')

#8
print(diamonds.info(), end = '\n \n \n')
#9
print(diamonds.sample(20))
