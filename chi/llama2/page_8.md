
| Model             | Size | Code | Commonsense Reasoning | World Knowledge | Reading Comprehension | Math  | MMLU | BBH  | AGI Eval |
|-------------------|------|------|-----------------------|-----------------|-----------------------|-------|------|------|---------|
| MPT               | 7B   | 25.0 | 57.4                  | 41.0            | 57.5                  | 26.8  | 31.0 | 23.5 |         |
| Falcon            | 7B   | 5.6  | 56.1                  | 42.8            | 36.0                  | 26.2  | 28.0 | 21.2 |         |
|                   | 40B  | 15.2 | 69.2                  | 56.7            | 127.6                 | 35.4  | 37.1 | 37.0 |         |
| LLaMA 1          | 13B  | 18.9 | 61.1                  | 52.6            | 62.3                  | 39.0  | 39.3 | 33.9 |         |
| LLaMA 2          | 33B  | 26.0 | 70.0                  | 58.4            | 67.6                  | 21.4  | 37.8 | 39.8 |         |
|                   | 66B  | 30.7 | 70.5                  | 61.6            | 66.8                  | 30.8  | 43.4 | 41.7 |         |
|                   | 7B   | 16.8 | 63.9                  | 48.9            | 61.3                  | 14.6  | 53.3 | 32.6 |         |
|                   | 13B  | 24.5 | 69.6                  | 55.4            | 68.8                  | 28.7  | 54.8 | 39.1 |         |
|                   | 34B  | 27.2 | 69.9                  | 58.7            | 68.0                  | 24.2  | 62.6 | 43.4 |         |
|                   | 70B  | 37.5 | 71.9                  | 63.6            | 69.4                  | 35.2  | 68.9 | 51.2 | 54.2    |

### Popular Aggregated Benchmarks
We report the overall results for MMLU (5 shot) (Hendrycks et al., 2020), Big Bench Hard (BBH) (3 shot) (Suzgun et al., 2022), and AGI Eval (5-3 shot) (Zhou et al., 2023). For AGI Eval, we only evaluate on the English tasks and report the average.

As shown in Table 3, LLaMA 2 models outperform LLaMA 1 models. In particular, LLaMA 2 70B improves the results on MMLU and BBH by 25 and 8 points, respectively, compared to LLaMA 1 66B. LLaMA 2 78B and 30B models outperform MPT models of the corresponding size on all categories based on benchmarks. For Falcon models, LLaMA 2 78B and 34B outperform Falcon 78 and 40B models on all categories of benchmarks. Additionally, LLaMA 2 70B models outperform all open-source models.

In addition to open-source models, we also compare LLaMA 2 70B results to closed-source models. As shown in Table 4, LLaMA 2 70B is close to GPT-3.5 (OpenAI, 2023) on MMLU and GSM8K, but there is a significant gap on coding benchmarks. LLaMA 2 70B results are on par or better than PaLM (540B) (Chowdhery et al., 2022) on almost all benchmarks. There is still a large gap in performance between LLaMA 2 70B and GPT-4 and PaLM-2.

### Benchmark (shots)
|                     | GPT-3.5 | GPT-4 | PaLM | PaLM-2 | LLaMA 2 |
|---------------------|---------|-------|------|--------|---------|
| MMLU (5-shot)       | 70.0    | 86.4  | 78.3 | 68.9   |         |
| TrivialQA (1-shot)  | -       | 81.4  | 86.1 | 85.0   |         |
| Natural Questions (1-shot) | - | 99.3  | 37.5 | 39.0   |         |
| GSM8K (8-shot)      | 57.1    | 92.0  | 80.7 | 56.5   |         |
| HumanEval (1-shot)  | 48.1    | 67.0  | 26.2 | 29.9   |         |
| Big-Bench Hard (3-shot) | -   | -     | 65.7 | 51.2   |         |

### 3 Fine-tuning
LLaMA 2-Chat is the result of several months of research and iterative applications of alignment techniques, including both instruction tuning and RLHF, requiring significant computational and annotation resources. In this section, we report on our experiments and findings using supervised fine-tuning (Section 3.1), as well as initial and iterative reward modeling (Section 3.2). We also share a new technique, Ghost Attention (GAt), which we find helps control dialogue flow over multiple turns (Section 3.3). See Section 4.2 for safety evaluations on fine-tuned models.
