# Latency Monitoring Project

This project consists of two Python scripts that work together to monitor network latency and visualize the results. The scripts are `ping_task.py` and `draw_task.py`.

## Overview

- `ping_task.py`: This script pings a specified IP address and records the latency in a database file.
- `draw_task.py`: This script reads the database file, generates a latency graph for the last 24 hours, and optionally deletes the database file.

## Requirements

- Python 3.x
- `matplotlib` library
- `tftpy` library

You can install the required libraries using pip:
```sh
pip install matplotlib tftpy
```

## Usage

### 1. `ping_task.py`

This script pings the specified IP address and records the latency in a database file.

- **IP Address**: The IP address to ping is set to `192.168.1.1` by default.
- **Database File**: The database file is located at `/root/latency_database.txt`.

To run the script, execute:
```sh
python ping_task.py
```

### 2. `draw_task.py`

This script reads the database file, generates a latency graph for the last 24 hours, and saves the graph as an image. Optionally, it can delete the database file after generating the graph.

- **Database File**: The database file is located at `/root/latency_database.txt`.
- **Image File**: The graph is saved as `latency_graph_<date>.png` in the `/root/data/onedrive/Attachments/` directory.

To run the script, execute:
```sh
python draw_task.py
```

To delete the database file after generating the graph, add the `-d` flag:
```sh
python draw_task.py -d
```

## File Descriptions

### `ping_task.py`

This script performs the following tasks:
1. Pings the specified IP address.
2. Extracts the latency from the ping output.
3. Records the latency and timestamp in the database file.

### `draw_task.py`

This script performs the following tasks:
1. Reads the database file and extracts data for the last 24 hours.
2. Calculates the percentage of non-zero latencies.
3. Generates and saves a latency graph.
4. Optionally deletes the database file.

## Example

### Sample Output

The latency graph will look like this:

![Latency Graph](sample_output.png)

This graph shows the latency over the last 24 hours with the percentage of non-zero latencies in the title.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

