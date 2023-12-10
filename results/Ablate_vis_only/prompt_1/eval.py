import json
import os
from sklearn.metrics import precision_recall_fscore_support
from matplotlib import pyplot as plt
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

def auc_roc_curve(filtered_res):
    # saves a auc_roc_curve plot in the current working folder
    # each data dict has a key called 'pred_failure'
    ground_truth = [value['gt_failure'] for value in filtered_res.values()]
    predictions = [value['pred_failure'] for value in filtered_res.values()]
    
    tp = sum(1 for entry_id, entry in filtered_res.items() if entry['pred_failure'] == 1 and entry['gt_failure'] == 1)
    tn = sum(1 for entry_id, entry in filtered_res.items () if entry['pred_failure'] == 0 and entry['gt_failure'] == 0)
    
    print(f"tp: {tp}")
    print(f"tn: {tn}")
    # calculate precision, recall and f1 score
    precision, recall, f1_score, support = precision_recall_fscore_support(ground_truth, predictions, average='binary')
    auc_roc_curve = roc_auc_score(ground_truth, predictions)
    print(f"auc_roc_curve: {auc_roc_curve}")
    saves_auc_roc_curve_plot(ground_truth,predictions,auc_roc_curve, "./auc_roc_")

def saves_auc_roc_curve_plot(ground_truth,predictions,auc, file_name):
    fpr, tpr, thresholds = roc_curve(ground_truth, predictions, pos_label=1)
    # saves a auc_roc_curve plot in the current working folder
    plt.figure()
    plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % auc)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.savefig(file_name + ".png")
    plt.close()
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
     

def filter_results(merged_res_dict):
    # each data dict has a key called 'pred_failure'
    # this function filters out the results dictionary that has a key called 'pred_failure': 'na'
    filtered_results = {}
    for key, value in merged_res_dict.items():
        if value['pred_failure']!= 'na':
            filtered_results[key] = value
    print(len(filtered_results))
    return filtered_results

def calculate_precision_recall_f1(filtered_res):
    # extract ground truth and predictions
    ground_truth = [value['gt_failure'] for value in filtered_res.values()]
    predictions = [value['pred_failure'] for value in filtered_res.values()]
    # calculate precision, recall and f1 score
    precision, recall, f1_score, support = precision_recall_fscore_support(ground_truth, predictions, average='binary')
    # print(f"precision: {precision}, recall: {recall}, f1_score: {f1_score}, support: {support}")
    print(f"precision: {round(precision,2)}, recall: {round(recall,2)}, f1_score: {round(f1_score,2)}, support: {support}")
    return precision, recall, f1_score, support


merged_res = files_merger("./")
filtered_res = filter_results(merged_res) # total videos after filtering: 4317
auc_roc_curve(filtered_res)


calculate_precision_recall_f1(filtered_res)
# auc_roc_curve: 0.5183118745612152
# precision: 0.63, recall: 0.76, f1_score: 0.69, support: None





