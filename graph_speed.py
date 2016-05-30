import matplotlib.pylab as plt
import pandas as pd
from matplotlib.dates import DateFormatter

data_path = "/Users/jaredbowden/Google Drive/cave_in_a_lake/data/"

dateparse = lambda x: pd.datetime.strptime(x, '%Y/%d/%m %H:%M:%S')

raw_data = pd.read_csv(data_path + "speed_frame.csv",
                       parse_dates=['Time'],
                       date_parser=dateparse)

temp_color = []

for line in raw_data["location"]:

    if line == "0":

        temp_color.append("grey")

    elif "Austin" in line:

        temp_color.append("green")

    else:

        temp_color.append("red")

raw_data["temp_color"] = temp_color
"""
raw_data["Time"] = pd.to_datetime(raw_data["Time"])

plt.scatter(
    range(len(raw_data["Time"])),
    raw_data["Download"],
    color=raw_data["temp_color"],
    alpha=0.8)
"""

# This is going to be a variation on the plotting option
fig, ax = plt.subplots()

ax.plot_date(x=raw_data["Time"],
             y=raw_data["Download"],
             alpha=0.8,
             color=raw_data["temp_color"])

myFmt = DateFormatter('%b %G')
ax.xaxis.set_major_formatter(myFmt)

ax.autoscale_view()

fig.autofmt_xdate()

plt.title("Moontower Internet Speed")
plt.xlabel("Time")
plt.ylabel("Speed")

plt.show()
plt.close()

# TODO add a histogram of speed. Would like to do things in a way that
# makes a distinction between VPN and Time Warner.

# TODO add some weekly and monthly summaries
