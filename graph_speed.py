__author__ = "Jared B Bowden"
__version__ = 1.2
"""
Plot of internet speed
"""

import matplotlib.pylab as plt
import pandas as pd
from matplotlib.dates import DateFormatter

data_path = "/Users/jaredbowden/Google Drive/cave_in_a_lake/data/"

dateparse = lambda x: pd.datetime.strptime(x, '%Y/%d/%m %H:%M:%S')

raw_data = pd.read_csv(data_path + "speed_frame.csv",
                       parse_dates=['Time'],
                       date_parser=dateparse)

location_tag = []

for line in raw_data["location"]:

    if line == "0":

        location_tag.append("Empty")

    elif "Austin" in line:

        location_tag.append("Time Warner")

    else:

        location_tag.append("VPN")

raw_data["location_tag"] = location_tag

# Plot things up
fig, ax = plt.subplots()

location = ["Empty", "Time Warner", "VPN"]
marker_color = ["0.75", "g", "r"]

for color, plot_layer in enumerate(location):
    ax.plot_date(
        x=raw_data[raw_data["location_tag"] == plot_layer]["Time"],
        y=raw_data[raw_data["location_tag"] == plot_layer]["Download"],
        marker="o",
        fillstyle="full",
        linestyle='None',
        alpha=0.5,
        markeredgewidth=0.0,
        fmt=marker_color[color])

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
