Here's the extracted content in markdown format:

```markdown
## Table 30: GAIt results.

| Dialogue Turn | Baseline | + GAIt |
|---------------|----------|--------|
| 2             | 100%     | 100%   |
| 4             | 10%      | 100%   |
| 6             | 0%       | 100%   |
| 20            | 0%       | 100%   |

**GAIt Zero-shot Generalisation.** We tried at inference time to set constraint not present in the training of GAIt. For instance, “answer in one sentence only”, for which the model remained consistent, as illustrated in Figure 28.

We applied first GAIt to LLaMA 1, which was pretrained with a context length of 2048 tokens and then fine-tuned with 4096 max length. We tested if GAIt works beyond 2048 tokens, and the model arguably managed to understand attributes beyond this window. This promising result indicates that GAIt could be adapted as an efficient technique for long context attention.

### A.3.6 How Far Can Model-Based Evaluation Go?

To measure the robustness of our reward model, we collected a test set of prompts for both helpfulness and safety, and asked annotators to judge quality of the answers based on a 7 point Likert-scale (the higher the better) using triple reviews. As illustrated in Figure 29 (in Appendix), we observe that our reward models overall are well calibrated with human preference. Note that this enables us to use the reward as a point-wise metric, despite being trained with a Pairwise Ranking Loss.

**Figure 27:** Reward model score distribution shift caused by incorporating preference rating based margin in ranking loss. With the margin term, we observe a binary split pattern in reward distribution, especially with a larger margin.
```

Feel free to modify it as needed!