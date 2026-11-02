# Project notes



## Oct 26

* Created project folder and GitHub repo
* Installed pandas, matplotlib, streamlit

## Oct 31
* Dataset:
Rows per city:
City
Ahmedabad             2009
Bengaluru             2009
Chennai               2009
Delhi                 2009
Lucknow               2009
Mumbai                2009
Hyderabad             2006
Patna                 1858
Gurugram              1679
Visakhapatnam         1462
Amritsar              1221
Jorapokhar            1169
Jaipur                1114
Thiruvananthapuram    1112
Amaravati              951
Brajrajnagar           938
Talcher                925
Kolkata                814
Guwahati               502
Coimbatore             386
Shillong               310
Chandigarh             304
Bhopal                 289
Ernakulam              162
Kochi                  162
Aizawl                 113
* AQI summary:
count    24850.000000
mean       166.463581
std        140.696585
min         13.000000
25%         81.000000
50%        118.000000
75%        208.000000
max       2049.000000

## Nov 1
* Cleaned data saved as data/city_day_clean.csv
* Dropped rows with missing AQI
* Kept PM2.5/PM10 NaN values, did not fill
