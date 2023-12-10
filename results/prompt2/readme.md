## update

- results are obtained. Total videos: 4711
- some videollama_outputs does not have yes/no in them.
  - need to figure out how many cases are like this: 670
  - Filtered out videos that has "yes" or "no" in videollama output
    - Total filtered videos: 4041

  - tp: 2363
  - tn: 133 (performed bad, but slight better than exp 1)
  - Total videos: 4041
  - Precision: 0.63
  - Recall: 0.94
  - F1 Score: 0.75
  - AUC-ROC: 0.52
  - Average Precision (AP): 0.63