import pandas as pd
import matplotlib.pylab as plt

dateparse = lambda x: pd.datetime.strptime(x, '%Y/%d/%m %H:%M:%S')

raw_data = pd.read_csv("./speed_frame.csv", parse_dates=['Time'], date_parser=dateparse)

temp_color = []

for line in raw_data["location"]:

	if line == "0":

		temp_color.append("grey")

	elif "Austin" in line:

		temp_color.append("green")

	else:

		temp_color.append("red")

raw_data["temp_color"] = temp_color

raw_data["Time"] = pd.to_datetime(raw_data["Time"])

plt.scatter(range(len(raw_data["Time"])), raw_data["Download"], color = raw_data["temp_color"], alpha = 0.8)

#TODO add units and parse time correctly
plt.title("Moontower Internet Speed")
plt.xlabel("Time")
plt.ylabel("Speed")

plt.show()
plt.close()
