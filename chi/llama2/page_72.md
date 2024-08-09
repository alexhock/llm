Here’s the extracted content in markdown format:


# Table 47: Distribution of mean sentiment scores across groups under the gender domain among the BOLD prompts.

|                        | American actors | American actresses |
|------------------------|-----------------|--------------------|
| Pretrained             |                 |                    |
| MPT                    | 7B 0.30 0.43    |                    |
| 30B                    | 0.29 0.41       |                    |
| Falcon                 | 7B 0.21 0.33    |                    |
| 40B                    | 0.29 0.37       |                    |
|                        |                 |                    |
|                        | 7B 0.31 0.46    |                    |
| LLAMA 1                | 13B 0.29 0.43   |                    |
| 23B                    | 0.26 0.44       |                    |
| 65B                    | 0.30 0.44       |                    |
|                        |                 |                    |
| LLAMA 2                | 7B 0.29 0.42    |                    |
| 13B                    | 0.32 0.44       |                    |
| 34B                    | 0.25 0.45       |                    |
| 70B                    | 0.28 0.44       |                    |
|                        |                 |                    |
| Fine-tuned             |                 |                    |
| ChatGPT                | 0.55 0.65       |                    |
| MPT-instruct           | 7B 0.31 0.38    |                    |
| Falcon-instruct        | 7B 0.32 0.36    |                    |
|                        |                 |                    |
| 7B                     | 0.48 0.56       |                    |
| LLAMA 2-Chat          | 13B 0.46 0.53   |                    |
| 34B                    | 0.44 0.47       |                    |
| 70B                    | 0.44 0.49       |                    |

Additionally, benchmarks typically assess language understanding and generation based on individual sentences or prompts, but in chat scenarios, context is important. The ability of a fine-tuned chat model to maintain context, handle nuanced situations, and avoid generating toxic content within a conversation may not be thoroughly evaluated by existing benchmarks. In the BOLD dataset, the prompts extracted from Wikipedia are taken to be the first five words plus the domain term, resulting in prompts in BOLD having six to nine words, depending on the domain and demographic group (Dhamala et al., 2021).

After deployment, safety in chat models involves user experience and long-term effects, which are not captured by benchmarks alone. Therefore, to assess safety effectively, additional testing of how they are integrated in a product deployment, how they are used, and what metrics accurately capture safety risks given the product context is essential for a comprehensive evaluation of safety. Our future work will conduct more comprehensive evaluations that encompass some dimensions not yet addressed in the cases mentioned above.

## A.5 Data Annotation

We have relied on human annotators in order to collect annotations for the supervised fine-tuning stage and human preferences to train the reward models. In this section, we provide details about the data annotation process.

### A.5.1 SFT Annotation Instructions

We have collected single-turn and multi-turn dialogue annotations from our pool of annotators. We asked the annotators to write responses that are informative, truthful, relevant, clear and harmless. We also asked annotators to prioritize harmlessness over informativeness and helpfulness in cases of prompts that could lead the responses to be problematic in any way. We categorized the kind of responses that could lead to negative user experiences and shared these categories and examples with the annotators. A summary of these categories can be seen in Section A.5.2.
