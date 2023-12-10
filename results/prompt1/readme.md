## update

- results are obtained. Total videos: 4711
- some videollama_outputs does not have yes/no in them.
  - need to figure out how many cases are like this: 355
  - Filtered out videos that has "yes" or "no" in videollama output
    - Total filtered videos: 4356

  - tp: 2528
  - tn: 117 (performed bad)
  - Total videos: 4356
  - Precision: 0.62
  - Recall: 0.94
  - F1 Score: 0.75
  - AUC-ROC: 0.5
  - Average Precision (AP): 0.62
    ![Alt text](results/prompt1/roc_curve.png)