import json
import os


# scans the current directory for json files only, then merges the contents to a single file
def files_merger(dir_name):
    # takes a directory name and merger all json files in that directory according to the number_ of file names
    files = os.listdir(dir_name)
    files = [file for file in files if file.endswith(".json")]
    files.sort(key=lambda x: int(x.split(".")[0].split("_")[0]))
    # print(files)
    merged_results = {}
    for file in files:
        with open(dir_name + "/" + file, "r") as f:
            data = json.load(f)
        # with open(dir_name + "/" + file.split(".")[0] + ".json", "w") as f:
        #     json.dump(data, f, indent=4)
        # os.remove(dir_name + "/" + file)

        #updating the merged_results dictionary with data
        for key, value in data.items():
            merged_results[key] = value

    return merged_results

def write_json(output_file_name,data): # "./merged_results.json"
    with open(output_file_name,'w') as f:
        json.dump(data,f,indent =4)
def load_json(file):
    with open(file,'r') as f: 
        return json.load(f)


if __name__ == "__main__":

    # merged_res = files_merger("./")
    merged_res = load_json("../p2_merged_results.json")
    print(len(merged_res.keys()))

    phrase_list_pos = [
        "Sure, the video contains only normal activities.",
        "The video does not contain any unusual activities.",
        "The video contains normal activities such as",#164
        "Yes, the video contains normal activities.", #150
        "There are no unusual activities in the video.",
"Yes, the video contains only normal activities.",
"Yes, the video only contains normal activities.",
"The video contains normal activities.",
"The video only contains normal activities",
"There are no unusual activities in this video.",
"The video does not contain any unusual activities.",
"the video does not contain any unusual activities.",
"There is no unusual activity in the video.",
"the video only contains normal activities.",
"the video does not contain any unusual activities.",
"Yes, the video contains normal activities,",
"Yes, the video contains only normal activities such as",
"The video does not contain any unusual activities,",
"Yes, this video contains normal activities.",
"The video I saw contains only normal activities.",
"Yes, the video contains normal activities such as",
"The video contains normal activities,",
"The video contains only normal activities,",
"It does not contain any unusual activities.",
"There are no unusual activities",
"The video doesn't contain any unusual activities,",
"Yes, the video only contains normal activities such as",
"the video does not show any unusual activities.",
"Yes, the video contains only normal activities,",
"The video also contains some unusual activities",
"it contains only normal activities.",
"there are no unusual activities in the video",
"The video I saw contained only normal activities.",
"Yes, the video contains only normal activities like",
"Yes, this video contains only normal activities.",
"It's not an unusual activity",
"The video does not show any unusual activities.",
"The video I saw contained normal activities",
"No, the video contains only normal activities.",
"The video contains only normal activities.",
"Yes, the video only contains normal activities,",
"I don't see anything unusual",
"I did not see any unusual activities",
"The video contains no unusual activities.",
"There are only normal activities in the video",
"Yes, this video only contains normal activities.",
"There are normal activities",
"The video contains mostly normal activities",
"The video contains normal activities like",
"There are several normal activities",
"contains normal activities of",
"The video I saw contained only normal activities",
"The video only shows normal activities.",
"The video I've watched contains normal activities",
"Sure, the video contains normal activities",
"contains a lot of normal activities",
"There is no unusual activity",
"the video only contains normal activities",
"It doesn't contain any unusual activities",
"The video doesn't contain any unusual activities.",
"this video only contains normal activities",
"there are no unusual activities",
"The video I saw did not contain any unusual activities",
"the video contains normal activities",
"The video does contain only normal activities.",
"Overall, the video contained normal activities",
"No, the video contains no unusual activities.",
"The video contains only normal activities",
"The video I saw contains only normal activities",
"The video has no unusual activities.",
"No, this video contains only normal activities,",
"I don't see any unusual activities",
"Yes, this video contains only normal activities",
"There is nothing unusual happening",
"The video does not contain any unusual activities",
"it does not contain any unusual",
"a lot of normal activities",
"There is nothing unusual",
"The video contains several normal activities,",
"The video contains various normal activities."
    ]
    phrase_list_neg = [
    "The only unusual activity that",
    "The video contains a mix of both normal and unusual activities.",
    "there is one instance of an unusual activity",
    "The video contains both normal and unusual activities.",
    "The video also contains some unusual activities",
    "No, the video contains some unusual activities.",
    "However, there is one unusual activity",
    "there is no unusual activity",
    "which can be considered unusual",
    "The video contains a mix of normal and unusual activities.",
    "The video does contain some unusual activities",
    "The video contains several unusual activities",
    "The video does contain unusual activities.",
    "there are also some unusual activities",
    "one unusual activity",
    "No, this video does not contain any unusual activities.",
    "contains some unusual activities",
    "No, the video does not contain only normal activities",
    "There are several unusual activities in the video",
    "There are also some unusual activities",
    "the video does contain some unusual activities",
    "the video contains both normal and unusual activities.",
    "there is also an unusual activity",
    "I can see some unusual activities.",
    "These are unusual activities",
    "few unusual activities",
    "This is unusual",
    "Yes, the video contains an unusual activity.",
    "Yes, the video contains unusual activities.",
    "Yes, the video contains an unusual activity,",
    "Sure, the video contains several unusual activities,",
    "Sure, the video contains several unusual activities.",
    "Yes, the video contains several unusual activities,",
    "Yes, there are some unusual activities in the video.",
    "Yes, the video contains unusual activities,",
    "Yes, the video contains several unusual activities.",
    "an unusual activity",
    "there are some unusual activities",
    "are some unusual activities",
    "there are several unusual activities",
    "there are unusual activities in the video",
    "video contains various unusual",
    "contains a lot of unusual",
    "There are several unusual activities shown in the video,",
    "contains a series of unusual activities",
    "the video contains unusual activities.",
    "contains unusual activities such as",
    "could be considered",
    "There are several unusual activities that",
    "The video does contain unusual activities",
    "combination of normal and unusual activities."

    ]


    for k,v in merged_res.items():
        # print(v)
        for i in phrase_list_pos:
            if i in v['videollama_ouput']:
                v['pred_failure'] = 0
        for j in phrase_list_neg:
            if j in v['videollama_ouput']:
                v['pred_failure'] = 1
        if v['pred_failure'] == "tbf":
            print("key: " ,k)
            print(v['videollama_ouput'])
            n = int(input("pred_failure 0 or 1: "))
            v['pred_failure'] = n
            write_json("../p2_merged_results.json",merged_res)

    write_json("../p2_merged_results.json",merged_res)



# "pred_failure": "tbf"