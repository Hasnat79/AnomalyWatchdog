import json
import os
from pathlib import Path
from collections import OrderedDict
prompt1_result_dir = Path("./")


merge_data = OrderedDict()

json_files = sorted(prompt1_result_dir.glob("*.json"),key=lambda x: int(x.stem.split('_')[0]))
for file in json_files:
    print(file)
    with open(file, 'r') as f: 
        data = json.load(f)

    for key, value in data.items():
        merge_data[key] = value
    # merge_data.update(data)

with open("./merged_results_0_4711.json", 'w') as f: 
    json.dump(merge_data,f,indent=4)
# print(merge_data)