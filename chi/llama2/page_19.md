Sure! Here’s the extracted content in Markdown format:

```markdown
## Figure 12: Human evaluation results for LLaMA 2-Chat models compared to open- and closed-source models across ~4,000 helpfulness prompts with three raters per prompt.

The largest LLaMA 2-Chat model is competitive with ChatGPT. LLaMA 2-Chat 70B model has a win rate of 36% and a tie rate of 31.5% relative to ChatGPT. LLaMA 2-Chat 70B model outperforms PaLM-bison chat model by a large percentage on our prompt set. More results and analysis is available in Section A.3.7.

### Inter-Rater Reliability (IRR)

In our human evaluations, three independent annotators provided independent assessments for each model generation comparison. High IRR scores (closer to 1.0) are typically seen as better from a data quality perspective; however, context is important. Highly subjective tasks like evaluating the overall helpfulness of LLM generations will usually have lower IRR scores than more objective labeling tasks. There are relatively few public benchmarks for these contexts, so we feel sharing our analysis here will benefit the research community.

We used Gwet’s AC1/2 statistic (Gwet, 2008, 2014) to measure inter-rater reliability (IRR), as we found it to be the most usable metric across different measurement scenarios. On the 7-point Likert scale helpfulness task that is used in our analysis, Gwet’s AC2 score varies between 0.37 and 0.55 depending on the specific model comparison. We see scores on the lower end of that range for ratings from model comparisons with similar win rates to each other (like the LLaMA 2-Chat-70B-chat vs. ChatGPT comparison). We see scores on the higher end of that range for ratings from model comparisons with a more clear winner (like the LLaMA 2-Chat-34B-chat vs. Falcon-40B-instruct).

### Limitations of Human Evaluations

While our results indicate that LLaMA 2-Chat is on par with ChatGPT on human evaluations, it is important to note that human evaluations have several limitations.

- By academic and research standards, we have a large prompt set of 4k prompts. However, it does not cover real-world use cases for these models, which will likely cover a significantly larger number of use cases.
- Diversity of the prompts could be another factor in our results. For example, our prompting set does not include any coding- or reasoning-related prompts.
- We only evaluate the final generation of a multi-turn conversation. A more interesting evaluation could be to ask the models to complete a task and rate the overall experience with the model over multiple turns.
- Human evaluation for generative models is inherently subjective and noisy. As a result, evaluation on a different set of prompts or with different instructions could result in different results.
```

Feel free to use or modify as needed!