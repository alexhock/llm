```markdown
# Helpfulness Reward Model Training and Results

## Helpfulness Reward Model

Helpfulness reward model is eventually trained on all Meta Helpfulness data, combined with an equal parts of the remaining data uniformly sampled from Meta Safety and from the open-source datasets. The Meta Safety reward model is trained on all Meta Safety and Anthropic Harmless data, mixed with Meta Helpfulness and open-source helpfulness data in a 90/10 proportion. We found that the setting with 10% helpfulness data is especially beneficial for the accuracy on samples where both the chosen and rejected responses were deemed safe.

### Training Details

We train for one epoch over the training data. In earlier experiments, we found that training longer can lead to over-fitting. We use the same optimizer parameters as for the base model. The maximum learning rate is \( 5 \times 10^{-6} \) for the 70B parameter LLaMA 2-Chat and \( 1 \times 10^{-5} \) for the rest. The learning rate is decreased on a cosine learning rate schedule, down to 10% of the maximum learning rate. We use a warm-up of 3% of the total number of steps, with a minimum of 5. The effective batch size is kept fixed at 512 pairs, or 1024 rows per batch.

| Model             | Meta Safety    | Anthropic        | Anthropic        | OpenAI         | Standard       | Avg.          |
|-------------------|----------------|-------------------|-------------------|----------------|----------------|---------------|
|                   | Helpful        | Helpful           | Harmless          | Summ.          | SHP            |               |
| SteamSHP-XL      | 52.8           | 43.8              | 66.8              | 34.2           | 54.7           | 55.3          |
| Open Assistant    | 53.8           | 53.4              | 67.7              | 68.4           | 71.7           | 63.0          |
| GPT-4             | 58.6           | 58.1              | -                 | -              | -              | -             |
| Safety RM         | 56.2           | 64.5              | 55.4              | 74.7           | 71.7           | 65.2          |
| Helpfulness RM    | 63.2           | 62.8              | 72.0              | 75.5           | 80.0           | 70.6          |

**Table 7:** Reward model results. Performance of our final helpfulness and safety reward models on a diverse set of human preference benchmarks. Note that our model is fine-tuned on our collected data, as opposed to the other baselines that we report.

### Reward Model Results

On each batch of human preference annotation for reward modeling, we held out 1000 examples as a test set to evaluate our models. We refer to the union of all prompts for the corresponding test sets as “Meta Helpfulness” and “Meta Safety,” respectively.

As reference points, we also evaluated other publicly available alternatives as baselines: SteamSHP-XL (Ehteshami et al., 2022) based on FLAN-T5, the Open Assistant (Kopf et al., 2023) reward model based on DeBERTa V3 Large (He et al., 2020), and GPT-4 accessible through the OpenAI API. Note that inference time, as opposed to training, all the reward models can predict a scalar for a single output, without requiring access to its predicted output. For GPT-4, we prompt with a zero-shot question "Choose the best answer between A and B," where A and B are the two responses for comparison.

We report the results in terms of accuracy in Table 7. As expected, our own reward models perform the best on our internal test sets collected based on LLaMA 2-Chat, with the Helpfulness reward model performing best on the Meta Helpfulness test set, and similarly the Safety reward model performing best on the Meta Safety test set. Overall, our reward models outperform all of the baselines, including GPT-4. Interestingly, GPT-4 performs better than other non-Meta reward models, despite being trained directly for targeting specifically this reward modeling task.

**Table 8:** Granular reward model accuracy per preference rating. We report per-preference rating accuracy for both Helpfulness and Safety reward models on the Meta Helpfulness and Safety test sets. The models show superior accuracy on more distinct responses (e.g., significantly better) and lower accuracy on similar responses (e.g., negligibly better).
```