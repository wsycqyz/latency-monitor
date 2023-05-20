import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import tftpy
import sys

database_file = "/root/latency_database.txt"

# Read the database file and extract data for the last 1 day
latencies = []
timestamps = []

# Calculate the datetime range for the last 1 day
one_day_ago = datetime.datetime.now() - datetime.timedelta(days=1)

with open(database_file, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        timestamp, latency = row
        timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

        if timestamp >= one_day_ago:
            timestamps.append(timestamp)
            latencies.append(int(latency))

# Calculate the percentage of non-zero latencies
total_latencies = len(latencies)
non_zero_latencies = len([l for l in latencies if l != 0])
percentage_non_zero = round((non_zero_latencies / total_latencies) * 100, 2)

# Set the figure size to 1080p (1920x1080)
plt.figure(figsize=(19.2, 10.8))

# Generate a graph
plt.plot(timestamps, latencies)
plt.xlabel("Time")
plt.ylabel("Latency")
plt.title(f"{datetime.datetime.now().date()} Latency Graph\n({percentage_non_zero}% Non-Zero)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Set the Y range from 0 to 100
plt.ylim(0, 100)

# Set the x-axis interval to half an hour (30 minutes) and align with whole hours
hours = mdates.HourLocator(interval=1)
halfhours = mdates.MinuteLocator(byminute=[0, 30])
date_fmt = mdates.DateFormatter("%H:%M")

plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gca().xaxis.set_major_locator(hours)
plt.gca().xaxis.set_minor_locator(halfhours)
plt.gca().xaxis.set_major_formatter(date_fmt)

# Set the y-axis interval to 5 seconds
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(5))

# Save the graph as an image
image_file = f"latency_graph_{datetime.datetime.now().date()}.png"
plt.savefig("/root/data/onedrive/Attachments/"+image_file)

# Delete the database file
if "-d" in sys.argv:
    if os.path.exists(database_file):
        os.remove(database_file)
    print(f"The database file '{database_file}' has been deleted.")

