Sure! Here’s the extracted content in markdown format:

```markdown
### Table 26: Statistics of Meta human preference data (Safety & Helpfulness) per batch.

| Batch | Num. of Comparisons | Avg. # Turns per Dialogue | Avg. # Tokens per Example | Avg. # Tokens in Prompt | Avg. # Tokens in Response |
|-------|---------------------|---------------------------|----------------------------|-------------------------|---------------------------|
| 1     | 5,561               | 4.4                       | 547.1                      | 25.2                    | 159.3                     |
| 2     | 1,072               | 4.0                       | 554.6                      | 22.4                    | 170.7                     |
| 3     | 30,146              | 3.9                       | 603.3                      | 19.6                    | 195.5                     |
| 4     | 36,206              | 3.9                       | 632.8                      | 45.3                    | 182.9                     |
| 5     | 49,375              | 3.7                       | 609.9                      | 46.7                    | 163.1                     |
| 6     | 57,746              | 4.1                       | 654.5                      | 28.2                    | 198.1                     |
| 7     | 84,388              | 3.9                       | 662.2                      | 27.5                    | 210.0                     |
| 8     | 95,235              | 3.6                       | 670.4                      | 32.9                    | 212.1                     |
| 9     | 12,735              | 3.6                       | 674.9                      | 31.3                    | 214.8                     |
| 10    | 146,729             | 3.7                       | 723.9                      | 30.5                    | 230.2                     |
| 11    | 136,868             | 3.8                       | 811.9                      | 32.2                    | 251.1                     |
| 12    | 181,893             | 3.9                       | 817.0                      | 30.8                    | 259.0                     |
| 13    | 210,881             | 4.2                       | 905.9                      | 30.3                    | 255.6                     |
| 14    | 249,356             | 4.3                       | 1008.0                     | 31.6                    | 258.9                     |

**Total** | **1,418,091**           | **3.9**                   | **798.5**                  | **31.4**                | **234.1**                 |

---

### Table 27: Two variants of preference rating based margin with different magnitude.

| Margin Small | 1          | 2/3          | 1/3            | 0              | 
|--------------|------------|--------------|----------------|----------------|
| Margin Large | 3          | 2            | 1              | 0              |

---

### Table 28: Ablation on preference rating-based margin in Helpful reward model ranking loss.

| Significantly Better | Slightly Better | Negligibly Better | Better / Unsure | Avg |
|----------------------|------------------|-------------------|------------------|-----|
| No margin            | 79.1             | 66.9              | 59.8             | 54.5 | 62.5 |
| Margin Small         | 80.4             | 67.3              | 60.4             | 55.0 | 63.0 |
| Margin Large         | 80.7             | 67.5              | 60.5             | 54.3 | 62.9 |

---

### A3.4 Ablation on Ranking Loss with Safety Auxiliary Loss for Reward Modeling

We ablated the impact of the safety auxiliary loss with results on the Meta Safety test set shown in Table 29. As expected, the customized loss improves the recall of unsafe responses when we use a reward score of 0.5 as the threshold (negative before Sigmoid) and thus offers a better safety reward signal for RLHF. Teaching the model to discriminate between safe and unsafe model generations also improves model accuracy on three subcategories.
```

Feel free to modify or expand upon it as needed!