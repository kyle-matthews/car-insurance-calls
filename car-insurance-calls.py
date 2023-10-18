import pandas as pd

car_insurance = pd.read_csv('Car_Insurance.csv')

df = pd.DataFrame(car_insurance)

df_dropped = df.dropna()

print(df_dropped)

# Finding the mean age of all claimants. 

total_age = 0
customers_counter = 0

for age in df_dropped['Age']:
    total_age += age
    customers_counter += 1


mean_age = total_age / customers_counter 
# Calculates the mean age is 41
print(int(mean_age))