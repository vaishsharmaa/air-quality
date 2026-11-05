import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv("data/city_day_clean.csv", parse_dates=["Date"])

df["Month"]= df["Date"].dt.month
df["Weekday"]= df["Date"].dt.day_name()

city="Delhi"
city_df = df[df["City"]== city]

order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weekly = city_df.groupby("Weekday")["AQI"].mean().reindex(order)
print(weekly.round(1))

fig, ax= plt.subplots(figsize=(10,5))
ax.bar(weekly.index, weekly.values, color="tab:green")
ax.set_xlabel("Weekday")
ax.set_ylabel("Avg AQI")
ax.grid(True, axis="y", alpha=0.3)

ax.set_ylim(weekly.min()-10, weekly.max()+10)

fig.tight_layout()
fig.savefig(f"charts/weekday_{city.lower()}.png", dpi= 150)
plt.show()
