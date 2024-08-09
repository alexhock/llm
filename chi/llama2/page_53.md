```markdown
### Figure 25: Distribution of human preference data rating over batches

Over time, the share of samples with an unsure or negligibly better rating become larger with better performing LLaMA 2-Chat trained and available for preference data annotation.

| Meta Preference Data Batch Stage | Significantly Better | Slightly Better | Better | Negligibly Better / Unsure |
|----------------------------------|----------------------|------------------|--------|----------------------------|
| 1                                |                      |                  |        |                            |
| 2                                |                      |                  |        |                            |
| 3                                |                      |                  |        |                            |
| 4                                |                      |                  |        |                            |
| 5                                |                      |                  |        |                            |
| 6                                |                      |                  |        |                            |
| 7                                |                      |                  |        |                            |
| 8                                |                      |                  |        |                            |
| 9                                |                      |                  |        |                            |
| 10                               |                      |                  |        |                            |
| 11                               |                      |                  |        |                            |
| 12                               |                      |                  |        |                            |
| 13                               |                      |                  |        |                            |
| 14                               |                      |                  |        |                            |

---

### Table 29: Ablation on safety auxiliary loss term for safety reward modeling

The safety auxiliary loss boosts accuracy on all 3 categories as well as the recall of unsafe response, measured by the percentage of unsafe responses captured with a reward score threshold of 0.5 (i.e., negative values before Sigmoid).

|                    | Avg  | Safe Chosen Unsafe Rejected | Safe Chosen Safe Rejected | Unsafe Chosen Unsafe Rejected | Unsafe Response Recall |
|--------------------|------|-----------------------------|---------------------------|-------------------------------|------------------------|
| Baseline            | 63.7 | 93.0                        | 56.0                      | 59.5                          | 73.0                   |
| + Auxiliary Safety Loss | 64.5 | 94.3                        | 56.9                      | 59.9                          | 90.4                   |

---

### A.3.5 Additional Results for GAtt

### Figure 26: Annotation curriculum

Evolution for each new batch of the maximum and median score given a reward model for prompts samples with a model trained on each of the batches. We can see that the score progressively decrease, suggesting that the prompts are on average harder in the most recent batches.

| Reward Annotation Stage | Max w/ 20 samples | Med w/ 20 samples |
|------------------------|--------------------|-------------------|
| 1                      | 0.80               |                   |
| 2                      | 0.70               |                   |
| 3                      | 0.60               |                   |
| 4                      | 0.50               |                   |
| 5                      | 0.40               |                   |
```
