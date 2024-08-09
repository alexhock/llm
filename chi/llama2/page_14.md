```markdown
### Figure 7: Max and median reward among N samples, N ∈ [1, ..., 100] averaged over our training set of prompts. 

The delta between max and median can be interpreted as potential gain with Rejection Sampling.

![Figure 7](attachment-link)

The highest reward score is considered the new gold standard. Similar to Scaloni et al. (2020a), we then fine-tune our model on the new set of ranked samples, reinforcing the reward.

The two RL algorithms mainly differ in:

- **Breadth** — In Rejection Sampling, the model explores K samples for a given prompt, while only one generation is done for PPO.
- **Depth** — In PPO, during training at step t the sample is a function of the updated model policy from t-1 after the gradient update of the previous step. In Rejection Sampling fine-tuning, we sample all the outputs given the initial policy of our model to collect a new dataset, before applying the fine-tuning similar to SFT. However, since we applied iterative model updates, the fundamental differences between the two RL algorithms are less pronounced.

Until RLHF (V4), we used only Rejection Sampling fine-tuning, and after that, we combined the two sequentially, applying PPO on top of the resulted Rejection Sampling checkpoint before sampling again.

### Figure 8: RLHF impact of the temperature when sampling N outputs and scoring them with a reward model.

![Figure 8](attachment-link)

#### Rejection Sampling
We perform rejection sampling only with our largest 708 LLaMA-2-Chat. All smaller models are fine-tuned on rejection sampled data from the larger model, thus distilling the large-model capabilities into the smaller ones. We leave further analysis of the effect of this distillation for future work.

At each iterative stage, we sample K answers for each prompt from the most recent model. We score each sample given the best reward model accessible at the time of the experiment, and then select the best answer for a given prompt. In earlier versions of our model, up to RLHF V3, our approach was to combine answer selection solely to the "bag" of samples gathered from the preceding iteration. For example, RLHF V3 was trained using only samples from RLHF V2. However, despite continuous improvement, this method led to a
```
