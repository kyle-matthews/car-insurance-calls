import pandas as pd
from datetime import datetime

car_insurance = pd.read_csv('Car_Insurance.csv')

df = pd.DataFrame(car_insurance)

df_dropped = df.dropna()

print(df_dropped.head())

call_end = datetime.strptime(df_dropped['CallEnd'], '%H::%M::%S').time()
call_start = datetime.strptime(df_dropped['CallStart'], '%H::%M::%S').time()

#df_dropped['CallDuration'] = df_dropped['CallEnd'] - df_dropped['CallStart']

