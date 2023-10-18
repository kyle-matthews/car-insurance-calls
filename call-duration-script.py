import pandas as pd
from datetime import datetime

car_insurance = pd.read_csv('Car_Insurance.csv')

df = pd.DataFrame(car_insurance)

df_dropped = df.dropna()

print(df_dropped.head())

df_dropped['CallEnd'] = pd.to_datetime(df_dropped['CallEnd'], format='%HH::%MM::%SS')
df_dropped['CallStart'] = pd.to_datetime(df_dropped['CallStart'], format='%HH::%MM::%SS')


df_dropped['CallDuration'] = df_dropped['CallEnd'] - df_dropped['CallStart']

