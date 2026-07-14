
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


range = max_mtemp-min_mtemp
highest_range = range.max()
hr_month = range.idxmax()
print(f">>the_month_with_the_greatest_range_is_{month_names[hr_month]}", f">>range_{highest_range:.1f}_degC" )


