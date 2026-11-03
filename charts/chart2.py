import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/city_day_clean.csv", parse_dates=["Date"])
cities=["Delhi","Mumbai","Jaipur"]
fig, ax = plt.subplots(figsize=(12,5))

for city in cities:
    city_df = df[df["City"] == city].sort_values("Date")

    smooth= city_df["AQI"].rolling(30,min_periods=10).mean()
    ax.plot(city_df["Date"], smooth, label=city, linewidth=1.5)
ax.set_title("AQI over time: city comparision (30-day average)")
ax.set_xlabel("Date")
ax.set_ylabel("AQI")
ax.grid(True, alpha=0.3)
ax.legend()

fig.tight_layout()
fig.savefig("charts/aqi_comparison.png", dpi=150)
plt.show()