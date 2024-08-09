Here's the extracted content in markdown format:

```markdown
| Model  | Size | GSM8k | MATH |
|--------|------|-------|------|
| MPT    | 7B   | 6.8   | 3.0  |
|        | 30B  | 15.2  | 3.1  |
| Falcon | 7B   | 6.8   | 2.3  |
|        | 40B  | 19.6  | 5.5  |
| LLaMA  | 7B   | 11.0  | 2.9  |
|        | 13B  | 17.8  | 3.9  |
|        | 33B  | 35.6  | 7.1  |
|        | 65B  | 50.9  | 10.6 |
| LLaMA  | 2    | 7B   | 14.6  | 2.5  |
|        | 13B  | 28.7  | 3.9  |
|        | 34B  | 42.2  | 6.24 |
|        | 70B  | 56.8  | 13.5 |

Table 25: Comparison to other open-source models on mathematical reasoning tasks, GSM8k and MATH (mal@1 is reported).

## Mathematical Reasoning.
In Table 25, we report results for LLaMA 2 and other open-source datasets on the GSM8k and MATH tasks.

### A.3 Additional Details for Fine-tuning

#### A.3.1 Detailed Statistics of Meta Human Preference Data
Table 26 shows detailed statistics on Meta human preference data. In total, we collected 14 batches of human preference data (i.e., Meta Safety + Helpfulness) on a weekly basis, consisting of over 1 million binary model generation comparisons. In general, later batches contain more samples as we onboard more annotators over time and the annotators also become more familiar with the tasks and have better work efficiency. We also intentionally collect more multi-turn samples to increase the complexity of RLHF data and thus the average number of tokens per sample also increase accordingly over batches.

In Figure 25, we plot out the preference rating change over batches. It can be clearly seen that the shares of samples with similar responses (e.g., negligibly better or worse) increase dramatically over time while those with stronger preference (e.g., significantly better) drop in the meantime. This reflects the nature of our iterative model update and preference data annotation procedure - with better-performing LLaMA 2-CHAT models used for response sampling over time, it becomes challenging for annotators to select a better one from two equally high-quality responses.

#### A.3.2 Curriculum Strategy for Meta Human Preference Data
High quality data is critical for alignment as discussed for SFT. We worked closely with the annotation platforms during our fine-tuning process, and opted for a curriculum annotation strategy. With the first model, the annotators were asked to make prompts relatively simple, and then to progressively move towards more complex prompts and taking new skills to LLaMA 2-CHAT. An illustration of this curriculum annotation strategy on our helpfulness preference data is displayed in Figure 26.

#### A.3.3 Ablation on Ranking Loss with Preference Rating-based Margin for Reward Modeling
We ablated the ranking loss with the preference rating-based margin term for the helpless reward model. We tried two variants of |m| with different magnitude for the margin term in Eq 2 as listed open-source 27 and compare them against the baseline without the margin term. We report both their per-rating and average accuracy on the Meta Helpful test set in Table 28. We observe that the margin term can indeed help the reward model perform better on more separable comparison pairs and a larger margin can boost it further. However, the larger margin also regresses performance on similar samples.

We further evaluated the impact of margin-based loss on reward score distribution shifts. We plot the histogram of reward scores from the test set in Figure 27. Essentially, the margin term pushes the reward.
```