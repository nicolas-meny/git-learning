import pandas as pd

df = pd.read_csv('customers.csv')
print(f"Taux de Churn : {df['churn'].mean() * 100}%")