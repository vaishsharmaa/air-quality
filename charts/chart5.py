import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/city_day_clean.csv", parse_dates=["Date"])

city = "Delhi"
city_df = df[df["City"] == city].sort_values("Date")

mean = city_df["AQI"].mean()
std = city_df["AQI"].std()
threshold = mean + 2 * std

high = city_df[city_df["AQI"] > threshold]

print(f"Mean AQI: {mean:.1f}, std: {std:.1f}, threshold: {threshold:.1f}")
print(f"High days: {len(high)} out of {len(city_df)}")
print(high[["Date", "AQI", "PM2.5", "PM10"]].sort_values("AQI", ascending=False).head(10))

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(city_df["Date"], city_df["AQI"], linewidth=0.8, label="Daily AQI")
ax.axhline(threshold, color="orange", linestyle="--", label=f"Threshold ({threshold:.0f})")
ax.scatter(high["Date"], high["AQI"], color="red", s=15, label="Unusually high", zorder=3)

ax.set_title(f"Unusually high AQI days in {city}")
ax.set_xlabel("Date")
ax.set_ylabel("AQI")
ax.grid(True, alpha=0.3)
ax.legend()

fig.tight_layout()
fig.savefig(f"charts/high_days_{city.lower()}.png", dpi=150)
plt.show()