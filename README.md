# AnomalyWatchdog

```bash
Baseline: run videollama for yes or no answer to determine whether a given video contains unusual activities, get the baseline numbers for the oops datasets Get the baseline number with VLM
Baseline with vision-only model
For the videos that were detected as unusual, ask for the “why? Question” / “describe why this video is unusual” in a separate exp.
(oops dataset paper has a pre-trained model that can be used as another baseline)
```
## Notes
- Some videollama_outputs does not have yes/no in them. Those videos were annotated as 'na'
- Those videos were filtered out before the evaluation.


## Experiment table 1 (Audio+visual features)
| Prompt|filtered videos|tp|tn|Precision | Recall | F1| Auc-roc|
| ---|---  |---|--- |--- |---|---|---|
|1.  "Does this video contain any unusual activities? Please reply Yes or No only."| 4356/4711| 2528|117|0.62|0.94|0.75|0.5|
|2.  "Let's look at this video frame by frame. Does this video contain any unusual activities? Please reply Yes or No only."|4490/4711 |2369|314 |0.63|0.94|0.75|0.52|
<!-- ![Alt text](results/Ablate_vis_only/prompt_1/auc_roc_.png) -->
<div style="display: flex; justify-content: space-between;">
  <div style="flex: 1; padding-right: 5px;">
  <img src="results/prompt1/auc_roc_.png" alt="Image 1" width="100%">
  </div>
    <div style="flex: 1; padding-right: 5px;">
  <img src="results/prompt2/auc_roc_.png" alt="Image 2" width="100%">
  </div>
</div>


## Experiment table 2 (Only Visual features w/o audio)
<!-- tp: 2025
tn: 458
auc_roc_curve: 0.5183118745612152
precision: 0.63, recall: 0.76, f1_score: 0.69, support: None -->
| Prompt|filtered videos|tp|tn|Precision | Recall | F1| Auc-roc|
| ---|---  |---|--- |--- |---|---|---|
|1.  "Does this video contain any unusual activities? Please reply Yes or No only."|3518/4711 | 2024|131 |0.63| 0.92|0.75|0.51|
|2.  "Let's look at this video frame by frame. Does this video contain any unusual activities? Please reply Yes or No only."|3083/4711|1759|161 |0.64|0.9|0.75|**0.52**|

<!-- precision: 0.64, recall: 0.66, f1_score: 0.65, support: None
tp: 1765
tn: 650
auc_roc_curve: 0.5311649750777898 -->
<div style="display: flex; justify-content: space-between;">
  <div style="flex: 1; padding-right: 5px;">
    <img src="results/Ablate_vis_only/prompt_1/auc_roc_.png" alt="Image 1" width="100%">
  </div>
  <div style="flex: 1; padding-right: 5px;">
    <img src="results/Ablate_vis_only/prompt_2/auc_roc_.png" alt="Image 2" width="100%">
  </div>
</div>


## Experiment table 3 (Prompt2 + visual only (8 vs 16 vs 32 frames)
| Prompt|Frames | filtered videos|tp|tn|Precision | Recall | F1| Auc-roc|
| ---|-- |---  |---|--- |--- |---|---|---|
|2.  "Let's look at this video frame by frame. Does this video contain any unusual activities? Please reply Yes or No only."| 8|3083/4711|1759|161 |0.64|0.9|0.75|**0.52**|
|2.  "Let's look at this video frame by frame. Does this video contain any unusual activities? Please reply Yes or No only."| 16|2636/4711|1368|192 |0.63|0.83|0.72|0.51|
|2.  "Let's look at this video frame by frame. Does this video contain any unusual activities? Please reply Yes or No only."|32|1317/4711|749|56 | 0.64| 0.89,|0.75|0.50|

## Experiment table 3 (Instruction Bias Checker)
| Prompt|fp | fn|Precision | Recall | F1| Auc-roc|
| ---|--- |---  |---|--- |--- |---|
|"Does the video contain only normal activities? Or does this video contain any unusual activities? Reply 'Yes' if it contains any unusual activities. Otherwise, reply 'No' if it only contains normal activities."|198|2583 (means for most of the videos: the model predicted as that is a  normal video)|0.62|0.11|0.19|0.5005|
|“Does the video contain any unusual activities? Or does this video contain only normal activities? Reply 'Yes' if it contains any unusual activities. Otherwise, reply 'No' if it contains only normal activities.”| 1255 (means for most of the videos: the model predicted as that is an unusual video)|828|0.62|0.71|0.67|0.5098|
