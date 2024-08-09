```markdown
## Figure 19: Violation percentage per risk category.

Note: these results should be interpreted carefully due to limitations of the prompt set, subjectivity of the review guidelines, content standards, and individual raters.

In Figure 18, we report the violation percentage on single- and multi-turn conversations, respectively. A trend across models is that multi-turn conversations are more prone to inducing unsafe responses. That said, LLaMA 2-Chat still performs well compared to baselines, especially on multi-turn conversations. We also observe that Falcon performs particularly well on single-turn conversations (largely due to its conciseness) but much worse on multi-turn conversations, which could be due to its lack of multi-turn supervised fine-tuning data.

In Figure 19, we show the per-category safety violation percentage of different LLMs. While model performance is similar across categories, LLaMA 2-Chat has relatively more violations under the unqualified advice category (although still low in an absolute sense), for various reasons, including lack of an appropriate disclaimer (e.g., “I am not a professional”) at times. For the other two categories, LLaMA 2-Chat achieves comparable or lower violation percentage consistently regardless of model sizes.

### Truthfulness, Toxicity, and Bias.

In Table 14, fine-tuned LLaMA 2-Chat shows great improvement over the pre-trained LLaMA 2 in terms of truthfulness (50.18 → 64.14 for 70B) and toxicity (21.60 → 0.01 for 70B). The percentage of toxic generations shrinks to effectively 0% for LLaMA 2-Chat of all sizes; this is the lowest toxicity level among all compared models. In general, when compared to Falcon and MPT, the fine-tuned LLaMA 2-Chat shows the best performance in terms of toxicity and truthfulness. After fine-tuning, LLaMA 2-Chat tends to have an increase in positive sentiment overall for many of the demographic groups in BOLD. In Appendix A.4.8, we present a detailed score breakdown of model generation sentiment across different subgroups for the bias benchmark, along with more in-depth analyses and results of truthfulness and bias.

### Table 14: Evaluation of fine-tuned LLMs on different safety datasets.

|                      | TruthfulQA ↑ | ToxicGen ↓ |
|----------------------|---------------|------------|
| ChatGPT              | 78.46         | 0.20       |
| Falcon-instruct      | 78.03         | 7.29       |
| MPT-instruct         | 79.99         | 16.33      |
| LLaMA 2-Chat        | 7B  57.04    | 0.00       |
|                      | 13B 62.18    | 0.01       |
|                      | 34B 67.20    | 0.02       |
|                      | 70B 64.14    | 0.01       |
```