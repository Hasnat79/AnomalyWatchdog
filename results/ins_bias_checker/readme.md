- Prompt-1: Does the video contain only normal activities? Or does this video contain any unusual activities? Reply 'Yes' if it contains any unusual activities. Otherwise, reply 'No' if it only contains normal activities.
- Prompt-2: Does the video contain any unusual activities? Or does this video contain only normal activities? Reply 'Yes' if it contains any unusual activities. Otherwise, reply 'No' if it contains only normal activities.
- Prompt-3: Does the video contain any unusual activities? Or does this video contain only normal activities? Reply 'Yes' if it contains only normal activities. Otherwise, reply 'No' if it contains any unusual activities.


---
### Tasks
- [X] Run Videollama over the above 3 prompts. Results are in each folders: p1, p2, p3 
- [X] In each folder:
    *  used `semi_auto_labeler.py` to manually label "pred_failure" 
        * merged & lableled outputs: `p*_merged_results.json`
    *  `eval_.py` is used to evaluate from the `p*_merged_results.json` files
- [X] Prompt 1 results
    * tp: 322
    * tn: 1607
    * fp: 198
    * fn: 2583
    * auc_roc_curve: 0.5005740413176251
    * precision: 0.62, recall: 0.11, f1_score: 0.19, support: None
- [X] Prompt 2 results
    * tp: 2077
    * tn: 550
    * fp: 1255
    * fn: 828
    * auc_roc_curve: 0.5098416618591501
    * precision: 0.62, recall: 0.71, f1_score: 0.67, support: None* 