import json
import os
from pathlib import Path

oops_transition_times_path = "../oops_dataset/annotations/transition_times_fixed.json"




oops_dataset_val_dir = "../oops_dataset/oops_video/val"
filtered_vids_path = "../oops_dataset/annotations/filtered_vids.txt"
val_vids_path ="../oops_dataset/annotations/val_filtered.txt"

# for file in path.glob("*.mp4"):
#     print(file)
#     c+=1

with open(oops_transition_times_path,'r') as f: 
    transition_times_data = json.load(f)

anomaly_data = {}
c =0
k = 0
id = 0
with Path(val_vids_path).open() as f: # open the file
    for line in f: # loop over the lines
        __data = {}
        video_path = "data/oops_dataset/oops_video/val/"+line.rstrip('\n')+".mp4"
        __data['path']=video_path
        if transition_times_data[line.rstrip('\n')]["n_notfound"] == 0:
            __data['failure'] = 1
            c+=1
        else: 
            __data['failure'] = 0
            k+=1
        anomaly_data[id] = __data
        id+=1

# print(anomaly_data)
print(f"total failure videos: {c}")
print(f"total not failure videos: {k}")
print(f"total videos: {len(anomaly_data.keys())}")

with open("./_anomaly_watchdog_data.json",'w') as f: 
    json.dump(anomaly_data,f,indent = 4)