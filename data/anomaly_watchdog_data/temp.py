import os
import json


# oops published description of val videos: (total videos: 3593)
    # 1. goal of the video
    # 2. what went wrong? 
# with open("/scratch/user/hasnat.md.abdullah/AnomalyWatchdog/data/anomaly_watchdog_data/val.json") as f:
#     data = json.load(f)

#     print(len(list(data.keys())))
# -----------------------------------------------


# There are 1805 data points with failure 0 and 2906 data points with failure 1 in the dataset.
# with open("/scratch/user/hasnat.md.abdullah/AnomalyWatchdog/data/anomaly_watchdog_data/anomaly_watchdog_data.json", 'r') as f: 
#     dataset = json.load(f)

# failure_0 = sum([video["failure"] == 0 for video in dataset.values()])
# failure_1 = sum([video["failure"] == 1 for video in dataset.values()])

# # Print the results
# print(f"There are {failure_0} data points with failure 0 and {failure_1} data points with failure 1 in the dataset.")
# -----------------------------------------------------

