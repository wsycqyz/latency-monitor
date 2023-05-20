import subprocess
from datetime import datetime

ip_address = "192.168.1.1"
database_file = "/root/latency_database.txt"

# Ping the IP address and record latency
ping_command = ["ping", "-c", "1", "-W", "1", ip_address]
ping_process = subprocess.Popen(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ping_output, ping_error = ping_process.communicate()

# Extract latency from the ping output
if ping_process.returncode == 0:
    # Successful ping
    latency = round(float(ping_output.decode().split("time=")[1].split()[0]))
else:
    # Ping timeout
    latency = 0

# Get the current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write latency and timestamp to the database file
with open(database_file, "a") as file:
    file.write(f"{timestamp},{latency}\n")

