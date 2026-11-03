import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/city_day_clean.csv", parse_dates=["Date"])
city= "Delhi"
city_df = df[df["City"] == city]
fig, ax = plt.subplots(figsize=(12,5))
ax.plot(city_df["Date"], city_df["AQI"], linewidth=0.8, label="Daily AQI")

ax.set_title(f"AQI over the time in {city}")
ax.set_xlabel("Date")
ax.set_ylabel("AQI")
ax.grid(True, alpha=0.3)
ax.legend()

fig.tight_layout()
fig.savefig(f"charts/aqi_{city.lower()}.png", dpi=150)
plt.show()