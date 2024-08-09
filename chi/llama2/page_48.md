```markdown
| Task                | BoolQ | PIQA | SIQA | Hella-Swag | ARC-C | ARC-H | NQ  | TQA | MMLU | CSM8K | Human-Eval |
|---------------------|-------|------|------|------------|-------|-------|-----|-----|-------|-------|------------|
| MHA                 | 71.0  | 79.3 | 48.2 | 75.1       | 71.2  | 43.0  | 12.4| 44.7| 28.0  | 4.9   | 7.9        |
| MQA                 | 70.6  | 79.0 | 47.9 | 74.5       | 71.6  | 41.9  | 14.5| 26.5| 4.8   | 7.3   |            |
| QQA                 | 69.4  | 78.8 | 48.6 | 75.4       | 72.1  | 42.5  | 14.0| 46.2| 26.9  | 5.3   | 7.9        |

### Figure 18: Attention architecture ablations.
We report 0-shot results for all tasks except MMLU(5-shot) and GSM8K(8-shot). For GSM8K and Human-Eval we report maj@1 and pass@1 results. For NQ and TriviaQA we report EM. For all other tasks we report accuracy.

### Figure 24: Multi-query variants enable higher throughput with larger batch sizes, and show similar latency on smaller batches.
Output length is fixed at 128 tokens. The first data point corresponds to batch size 1, and then we double it until the model runs out of memory. The MHA variant triggers an out-of-memory error at a batch size of 1024 for a context of 256 tokens and at a batch size of 128 for 2k context, whereas MQA and QQA have successful runs in those settings.

Therefore, based on the ablation results and ease of scaling inference, for the 34B and 70B LLaMA 2 models we chose to use QGA instead of MQA.

### Additional Details for Pretrained Models Evaluation

**MMLU Details.** In Table 19, we report details of the MMLU (Hendrycks et al., 2020) evaluation for LLaMA 2 models and others open-source models.

**Standard Benchmarks.** In Table 20, we show results on several standard benchmarks.

**Code Generation.** In Table 21, we compare results of LLaMA 2 with popular open source models on the Human-Eval and MBPP code generation benchmarks.

**World Knowledge.** We evaluate the LLaMA 2 model together with other open-source models on the NaturalQuestions and TriviaQA benchmarks (Table 22).

**Reading Comprehension.** In Table 23 we report zero-shot and few-shot results on SQUAD and zero-shot one-shot experiments on QUAC. Here LLaMA 2 performs best on all evaluation settings and models except the QUAC 0-shot where LLaMA 3 30B performs slightly better.

**Exams.** In Table 24, we present fine-grained results from the English part of the AGI Eval (Zhong et al., 2023) benchmark. AGI Eval is a collection of standardized exams in different subjects.
```