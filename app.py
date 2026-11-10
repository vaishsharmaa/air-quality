import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
st.set_page_config(page_title="Air Quality Dashboard", layout="wide")
@st.cache_data
def load_data():
    df = pd.read_csv("data/city_day_clean.csv", parse_dates=["Date"])
    return df.sort_values(["City", "Date"])
df = load_data()
st.title("Air Quality Dashboard")
st.write("Explore how air changes over the time in Indian cities.")

city = st.sidebar.selectbox("Choose a city", sorted(df["City"].unique()))
city_df = df[df["City"]== city]
c1,c2,c3 = st.columns(3)
c1.metric("Avg AQI", f"{city_df['AQI'].mean():.0f}")
c2.metric("Highest AQI", f"{city_df["AQI"].max():.0f}")

fig, ax = plt.subplots(figsize=(12,5))
ax.plot(city_df["Date"],city_df["AQI"], linewidth=0.8)
ax.set_title(f"AQI over time in {city}")
ax.set_xlabel("Date")
ax.set_ylabel("AQI")
ax.grid(True, alpha=0.3)
fig.tight_layout()
show_avg = st.sidebar.checkbox("Show 30-day average")
if show_avg:
    smooth = city_df["AQI"].rolling(30, min_periods=10).mean()
    ax.plot(city_df["Date"], smooth, color="red", linewidth=2, label="30-day average")
    ax.legend()
st.pyplot(fig)

st.subheader("Latest records")
st.dataframe(city_df.tail(10))
