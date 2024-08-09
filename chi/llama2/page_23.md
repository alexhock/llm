
| TruthfulQA ↑ | ToxiGen ↓ |
|---------------|-----------|
| MPT           |           |
| 7B            | 29.13     | 22.32     |
| 30B           | 35.25     | 22.61     |
| Falcon        |           |
| 7B            | 25.95     | 14.83     |
| 40B           | 40.39     | 23.44     |
| LLaMA 1      |           |
| 7B            | 27.42     | 23.00     |
| 13B           | 41.74     | 23.08     |
| 33B           | 44.19     | 22.57     |
| 65B           | 48.71     | 21.77     |
| LLaMA 2      |           |
| 7B            | 33.29     | 21.25     |
| 13B           | 41.86     | 26.10     |
| 34B           | 43.45     | 21.19     |
| 70B           | 50.18     | 24.60     |

Table 11: Evaluation of pretrained LLMs on automatic safety benchmarks. For TruthfulQA, we present the percentage of generations that are both truthful and informative (the higher the better). For ToxiGen, we present the percentage of toxic generations (the smaller, the better).

---

## 4.2 Safety Fine-Tuning

In this section, we describe our approach to safety fine-tuning, including safety categories, annotation guidelines, and the techniques we use to mitigate safety risks. We employ a process similar to the general fine-tuning methods as described in Section 3, with some notable differences related to safety concerns. Specifically, we use the following techniques in safety fine-tuning:

1. **Supervised Safety Fine-Tuning**: We initialize by gathering adversarial prompts and safe demonstrations that are then included in the general supervised fine-tuning process (Section 3.1). This teaches the model to align with our safety guidelines even before RLHF, and thus lays the foundation for high-quality human preference data annotation.

2. **Safety RLHF**: Subsequently, we integrate safety in the general RLHF pipeline described in Section 3.2. This includes training a safety-specific reward model and gathering more challenging adversarial prompts for rejection sampling, safe fine-tuning, and PPO optimization.

3. **Safety Context Distillation**: Finally, we refine our RLHF pipeline with context distillation (Askell et al., 2019). This involves generating safe model responses by prefixing a prompt with a safety preprompt, e.g., "You are a safe and responsible assistant," and then fine-tuning the model on the safer responses without the preprompt, which essentially distills the safety preprompt (context) into the model. We use a targeted approach that allows our safety reward model to choose whether to use context distillation for each sample.

### 4.2.1 Safety Categories and Annotation Guidelines

Based on limitations of LLMs known from prior work, we design instructions for our annotation team to create adversarial prompts along two dimensions: **risk category**, or potential topic about which the LLM could produce unsafe content; and **attack vector**, or question style to cover different varieties of prompts that could elicit bad model behaviors.

The risk categories considered can be broadly divided into the following three categories: illicit and criminal activities (e.g., terrorism, theft, human trafficking); hateful and harmful activities (e.g., defamation, self-harm, eating disorders, discrimination); and unqualified advice (e.g., medical advice, financial advice, legal advice).
