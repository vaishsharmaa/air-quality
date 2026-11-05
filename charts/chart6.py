import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv("data/city_day_clean.csv", parse_dates=["Date"])

df["Month"]= df["Date"].dt.month
df["Weekday"]= df["Date"].dt.day_name()

city="Delhi"
city_df = df[df["City"]== city]

monthly = city_df.groupby("Month")["AQI"].mean()
month_names=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(monthly.index, monthly.values, color="tab:orange")
ax.set_xticks(range(1,13))
ax.set_xticklabels(month_names)
ax.set_title(f"Average AQI by month in {city}")
ax.set_xlabel("Month")
ax.set_ylabel("Avg AQI")
ax.grid(True, axis="y", alpha=0.3)
fig.tight_layout()
fig.savefig(f"charts/monthly_{city.lower()}.png", dpi=150)
plt.show()