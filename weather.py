
import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv("weather.csv", skiprows=90, skipfooter=1, engine="python")
weather["ob_end_time"] = pd.to_datetime(weather["ob_end_time"])
coldest = weather.loc[weather["min_air_temp"].idxmin()]
hottest = weather.loc[weather["max_air_temp"].idxmax()]
weather["month"] = weather["ob_end_time"].dt.month
max_monthly_average = weather.groupby("month")["max_air_temp"].mean()
min_monthly_average = weather.groupby("month")["min_air_temp"].mean()
max_mtemp = weather.groupby("month")["max_air_temp"].max()
min_mtemp = weather.groupby("month")["min_air_temp"].min()
weather["average_temp"] = (weather["max_air_temp"] + weather["min_air_temp"]) / 2
monthly_average = weather.groupby("month")["average_temp"].mean()

month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
min_monthly_average.index = min_monthly_average.index.map(month_names)
max_monthly_average.index = max_monthly_average.index.map(month_names)
monthly_average.index = monthly_average.index.map(month_names)

range = max_mtemp-min_mtemp
highest_range = range.max()
hr_month = range.idxmax()

#data_poi
print("\nAverage temperatures by month:")
print(monthly_average)
print(f"Hottest day: {hottest['ob_end_time'].date()} at {hottest['max_air_temp']}°C")
print(f"Coldest day: {coldest['ob_end_time'].date()} at {coldest['min_air_temp']}°C")
print(f"The month with the greatest range was {month_names[hr_month]}", f"range {highest_range:.1f}°C" )

#graph
plt.figure(figsize=(12,5))
plt.plot(weather["ob_end_time"], weather["average_temp"])
plt.title("Average Daily Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig("temperature_over_time.png", dpi=300, bbox_inches="tight")
plt.show()
