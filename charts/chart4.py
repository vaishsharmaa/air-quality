import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/city_day_clean.csv", parse_dates=["Date"])
city ="Delhi"
city_df = df[df["City"]== city].sort_values("Date")
print(city_df[["PM2.5","PM10"]].isna().sum())

fig, (ax1, ax2)= plt.subplots(2,1, figsize=(12,8), sharex=True)
ax1.plot(city_df["Date"], city_df["PM2.5"], color="tab:red", linewidth=0.8)
ax1.set_title(f"PM2.5 in {city}")
ax1.set_ylabel("PM2.5")
ax1.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig(f"charts/pm_{city.lower()}.png", dpi=150)
