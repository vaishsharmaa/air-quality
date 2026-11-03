import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("data/city_day_clean.csv", parse_dates=["Date"])

avg_aqi = df.groupby("City")["AQI"].mean().sort_values()
print(avg_aqi.round(1))
fig, ax = plt.subplots(figsize=(8,8))
ax.barh(avg_aqi.index, avg_aqi.values, color="steelblue")

ax.set_title("Avg AQI by city")
ax.set_xlabel("Avg AQI")
ax.grid(True, axis="x", alpha=0.3)

fig.tight_layout()
fig.savefig("charts/avg_aqi_by_city.png", dpi=150)
plt.show()
print(df.groupby("City")["Date"].agg(["min","max","count"]))
