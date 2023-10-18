import pandas as pd


car_insurance = pd.read_csv('Car_Insurance.csv')

df = pd.DataFrame(car_insurance)

df_dropped = df.dropna()

#print(df_dropped.head())
df_dropped.loc[df_dropped.index, 'CallEnd'] = pd.to_datetime(df_dropped['CallEnd'], format='%H:%M:%S')
df_dropped.loc[df_dropped.index, 'CallStart'] = pd.to_datetime(df_dropped['CallStart'], format='%H:%M:%S')

# Calculate the 'CallDuration'
df_dropped.loc[df_dropped.index, 'CallDuration'] = df_dropped.loc[df_dropped.index,'CallEnd'] - df_dropped.loc[df_dropped.index, 'CallStart']

print(df_dropped['CallDuration'])
