import pandas as pd

df = pd.read_csv("data/city_day.csv")
rows_before = len(df)

# 1. Convert Date from text to real dates
df["Date"] = pd.to_datetime(df["Date"])

# 2. Sort by city and date so time-series charts draw correctly
df = df.sort_values(["City", "Date"]).reset_index(drop=True)

# 3. Drop rows with no AQI, because AQI is the main column of the project
df = df.dropna(subset=["AQI"])

# 4. Keep only the columns the project needs
df = df[["Date", "City", "PM2.5", "PM10", "AQI", "AQI_Bucket"]]

# 5. Remove duplicate city-date rows, if any
df = df.drop_duplicates(subset=["City", "Date"])

# 6. Leave PM2.5 and PM10 gaps as NaN. Filling with 0 or the mean would invent data.

print("Rows before:", rows_before)
print("Rows after:", len(df))
print(df.isna().sum())
print(df.dtypes)
print(df.head())

df.to_csv("data/city_day_clean.csv", index=False)
print("Saved data/city_day_clean.csv")
