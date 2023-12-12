import json
import os


def files_traverse_fix_res(dir_name):
    # takes a directory name and merger all json files in that directory according to the number_ of file names
    files = os.listdir(dir_name)
    files = [file for file in files if file.endswith(".json")]
    files.sort(key=lambda x: int(x.split(".")[0].split("_")[0]))
    # print(files)
    merged_results = {}
    for file in files:
        print(file)
        with open(dir_name + "/" + file, "r") as f:
            data = json.load(f)
        # with open(dir_name + "/" + file.split(".")[0] + ".json", "w") as f:
        #     json.dump(data, f, indent=4)
        # os.remove(dir_name + "/" + file)

        #fixing the data dictionary 
        for key, value in data.items():
            if "yes" in value["videollama_ouput"][:3].lower():
                value['pred_failure'] = 1
            elif "no" in value["videollama_ouput"][:2].lower():
                value['pred_failure'] = 0
            else:
                value['pred_failure'] = 'na'
        with open(dir_name + "/" + file.split(".")[0] + ".json", "w") as f:
            json.dump(data, f, indent=4)


     



files_traverse_fix_res("./")






