```markdown
| Model            | Parameters | % (true + info) | % true | % info |
|------------------|------------|------------------|--------|--------|
| **Pretrained**    |            |                  |        |        |
| MPT              | 7B         | 29.13           | 36.72  | 92.04  |
|                  | 30B        | 35.25           | 40.27  | 94.74  |
| Falcon           | 7B         | 25.95           | 29.01  | 96.03  |
|                  | 40B        | 40.90           | 44.80  | 95.23  |
|                  | 7B         | 27.42           | 32.71  | 94.16  |
| LLAMA 1          | 13B        | 41.74           | 48.75  | 95.72  |
|                  | 33B        | 44.19           | 51.87  | 95.23  |
|                  | 65B        | 48.71           | 51.29  | 96.82  |
| LLAMA 2          | 7B         | 33.29           | 39.53  | 93.02  |
|                  | 13B        | 41.86           | 46.65  | 96.08  |
|                  | 34B        | 43.45           | 46.14  | 96.7   |
|                  | 70B        | 50.18           | 53.37  | 96.21  |
| **Fine-tuned**    |            |                  |        |        |
| ChatGPT          |            | 78.46           | 79.92  | 98.53  |
| MPT-instruct     | 7B         | 29.99           | 31.37  | 94.37  |
| Falcon-instruct  | 7B         | 28.03           | 41.00  | 85.65  |
| LLAMA 2-CHAT     | 13B        | 57.04           | 61.09  | 96.45  |
|                  | 34B        | 67.2            | 70.01  | 97.06  |
|                  | 70B        | 64.14           | 67.07  | 97.06  |

**Table 44:** Evaluation results on TruthfulQA across different model generations.

**Limitations of Benchmarks.** It is important to note that these evaluations using automatic metrics are by no means fully comprehensive, due to the complex nature of toxicity and bias in LLMs, but the benchmarks selected are representative of our understanding that LLAMA 2-CHAT improves on critical aspects of LLM safety. Benchmark evaluation is important for assessing all models, including chat-oriented LLMs, because benchmarks provide a standardized and measurable way to compare different models and track progress in the field. 

However, it's crucial to be aware of the benchmarks' limitations in evaluating safety. Most of them were initially developed for pretrained LLMs, and there are certain limitations to consider when using them to measure the safety of fine-tuned/chat-oriented models. For example, the benchmarks may not adequately cover adversarial inputs or toxic content specifically designed to exploit vulnerabilities, and they may not cover all demographic categories. It is advisable to monitor disaggregated metrics and benchmarks in order to better understand and analyze the varied behavior exhibited by LLMs across different demographic groups.
```