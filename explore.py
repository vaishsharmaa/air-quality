import pandas as pd

df = pd.read_csv("data/city_day.csv")

print("Shape:", df.shape)
print("\nColumns:", list(df.columns))
print("\nInfo:")
df.info()

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values per column:")
print(df.isna().sum())

print("\nMissing values (% of rows):")
print((df.isna().mean() * 100).round(1))

print("\nNumber of cities:", df["City"].nunique())
print(df["City"].unique())

print("\nRows per city:")
print(df["City"].value_counts())

dates = pd.to_datetime(df["Date"])
print("\nDate range:", dates.min(), "to", dates.max())

print("\nAQI summary:")
print(df["AQI"].describe())
