import os
from json_utils.json_utils import read_json,write_json
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, auc, roc_curve, roc_auc_score, average_precision_score


import numpy as np 



path = "./filtered_videollama_output_data.json"

filtered_videollama_output_data = read_json(path)
# assert len(filtered_videollama_output_data.keys()) == 4365

data = filtered_videollama_output_data

gt_labels = []
pred_labels = []

for entry_id, entry_data in data.items():
    gt_labels.append(entry_data["gt_failure"])
    pred_labels.append(entry_data["pred_failure"])


data = filtered_videollama_output_data

total_cases = len(data)
tp = sum(1 for entry_id, entry in data.items() if entry['gt_failure'] == 1 and entry['pred_failure'] == 1)
fp = sum(1 for entry_id, entry in data.items() if entry['gt_failure'] == 0 and entry['pred_failure'] == 1)
fn = sum(1 for entry_id, entry in data.items() if entry['gt_failure'] == 1 and entry['pred_failure'] == 0)
tn = sum(1 for entry_id, entry in data.items() if entry['gt_failure'] == 0 and entry['pred_failure'] == 0)

print(f"tp: {tp}")
print(f"tn: {tn}")
precision = tp / (tp + fp) if (tp + fp) > 0 else 0
recall = tp / (tp + fn) if (tp + fn) > 0 else 0
f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

# Calculate mean average precision (meanAP) - Assuming precision and recall are available for each data point
# You may need to modify this part based on how you compute precision and recall in your specific case
# precision_recall_pairs = [(entry['precision'], entry['recall']) for entry in data]
# mean_ap = sum(precision for precision, _ in precision_recall_pairs) / len(precision_recall_pairs)

print("Total Cases:", total_cases)
print("Precision:", round(precision,2))
print("Recall:", round(recall,2))
print("F1 Score:", round(f1,2))
# Calculate AUC-ROC
auc_roc = roc_auc_score(gt_labels, pred_labels)
print("AUC-ROC:", round(auc_roc,2))

# Calculate Average Precision (AP)
average_precision = average_precision_score(gt_labels, pred_labels)
print("Average Precision (AP):", round(average_precision,2))

# Calculate ROC curve
fpr, tpr, _ = roc_curve(gt_labels, pred_labels)
# Calculate Precision-Recall curve
precision, recall, _ = precision_recall_curve(gt_labels, pred_labels)

# Plot ROC curve
plt.figure(figsize=(8, 8))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'AUC-ROC = {auc_roc:.2f}')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.grid(True)
plt.savefig('roc_curve.png')
plt.show()



# Total Cases: 4365
# Precision: 0.62
# Recall: 0.94
# F1 Score: 0.74
# AUC-ROC: 0.5
# Average Precision (AP): 0.62



