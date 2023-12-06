import os
from json_utils.json_utils import read_json,write_json

merged_0_4711_oops_val_path = "./merged_results_0_4711.json"

merged_0_4711_oops_val_res = read_json(merged_0_4711_oops_val_path)
# with open(merged_0_4711_oops_val_path,'r') as f: 
#     merged_0_4711_oops_val_res = json.load(f)

#filtering out wo_yes_no vieollama output from the merge_results_0_4711.json file
filtered_videollama_output_data ={} 
wo_yes_no_counter = 0
wo_yes_no_list = []
for k,v in merged_0_4711_oops_val_res.items(): 
    # print(k)
    # print(v)
    if "yes" in v['videollama_ouput'][:3].lower():
        # print("ok")
        filtered_videollama_output_data[k]=v
        
        
    elif "no" in v['videollama_ouput'][:2].lower(): 
        # print("ok - no")
        filtered_videollama_output_data[k]=v
    else: 
        # print(f"k: {k}\nv: {v}")
        wo_yes_no_counter+=1


print(f"Total filtered videos: {len(filtered_videollama_output_data.keys())}")#4365
print(f"Total cases w/o yes|no: {wo_yes_no_counter}") #346
assert len(merged_0_4711_oops_val_res.keys()) == len(filtered_videollama_output_data.keys())+ wo_yes_no_counter

# assert len(filtered_videollama_output_data.keys()) == 4365
write_json("./filtered_videollama_output_data.json",filtered_videollama_output_data)
# with open("./filtered_videollama_output_data.json",'w') as f: 
#     json.dump(filtered_videollama_output_data,f,indent=4)

# Total filtered videos: 4041
# Total cases w/o yes|no: 670





 





# with open("./merged_results_0_4711.json", 'w') as f: 
#     json.dump(merge_data,f,indent=4)
# print(merge_data)