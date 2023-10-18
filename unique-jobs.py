import pandas as pd

# The code is reading a CSV file named 'Car_Insurance.csv' using the pandas library. It then creates a
# DataFrame called `df` from the data in the CSV file. The `df_dropped` DataFrame is created by
# dropping any rows that contain missing values (NaN).

car_insurance = pd.read_csv('Car_Insurance.csv')

df = pd.DataFrame(car_insurance)

df_dropped = df.dropna()

print(df_dropped['Job'].unique())

counted_jobs = df_dropped['Job'].value_counts()

print(counted_jobs)
