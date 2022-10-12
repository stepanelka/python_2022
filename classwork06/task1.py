
#Упражнение 8. Создайте датафрейм, в котором будует
# средние количества звонков Total day calls и Total eve calls
# для каждого штата, а также столбец со значениями True и False - ответом
# на вопрос, больше ли дневных звонков, чем вечерних.
import pandas as pd
f = pd.read_csv("telecom_churn.csv")

d_sr_day = f.groupby('Total day calls', sort=False, as_index=False).sum()
d_sr_eve = f.groupby('Total eve calls', sort=False, as_index=False).sum()
DataFrame.compare(, keep_equal = True )

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.compare.html
