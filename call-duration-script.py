import pandas as pd


car_insurance = pd.read_csv('Car_Insurance.csv')

df = pd.DataFrame(car_insurance)

df_dropped = df.dropna()

print(df_dropped.head())

df_dropped['CallEnd'] = pd.to_datetime(df_dropped['CallEnd'], format='%H:%M:%S')
df_dropped['CallStart'] = pd.to_datetime(df_dropped['CallStart'], format='%H:%M:%S')


df_dropped['CallDuration'] = df_dropped['CallEnd'] - df_dropped['CallStart']

