Here's the extracted content formatted in Markdown:

```markdown
## Figure 11: Evolution of LLaMA 2-Chat

We show the evolution after multiple iterations fine-tuning for the win-rate % of LLaMA 2-Chat compared to ChatGPT. Left: the judge is our reward model, which may favor our model, and right, the judge is GPT-4, which should be more neutral.

### Progression of Models
Figure 11 reports the progress of our different SFT and РLHF versions for both Safety and Helpfulness axes, measured by our in-house Safety and Helpfulness reward models. On this set of evaluations, we outperform ChatGPT on both axes after RLHF-V3 (harmlessness and helpfulness >50%). Despite the aforementioned relevance of using our reward as a point-wise metric, it can arguably be biased in favor of LLaMA 2-Chat. Therefore, for a fair comparison, we additionally compute the final results using GPT-4 to assess which generation is preferred. The order in which ChatGPT and LLaMA 2-Chat outputs appeared in GPT-4 prompt are randomly swapped to avoid any bias. As expected, the win-rate in favor of LLaMA 2-Chat is less pronounced, although obtaining more than a 60% win-rate for our latest LLaMA 2-Chat.

The prompts correspond to a validation set of 1,586 and 584 prompts for safety and helpfulness, respectively.

### 3.4.2 Human Evaluation
Human evaluation is often considered the gold standard for judging models for natural language generation, including dialogue models. To evaluate the quality of major model versions, we asked human evaluators to rate them on helpfulness and safety. We compare the LLaMA 2-Chat models to open-source models (Folks: MPT Moïsalol MML NLP Team et al. (2023), Vucuna Chang et al. (2023), as well as closed-source models: ChatGPT (OpenAI, 2023) and Palm Aml et al. (2023) on over 4,000 single and multi-turn prompts. For ChatGPT, we use gpt-3.5-turbo-0301 model in all generations. For Palm, we use that same model in all generations. The final prompt count for human evaluations for each model is shown in Table 22. See more methodology details in Appendix, Section A.3.7. The following shows helpfulness results; safety results are presented in Section 4.4.

### Results
As shown in Figure 12, LLaMA 2-Chat models outperform open-source models by a significant margin on both single turn and multi-turn prompts. Particularly, LLaMA 2-Chat 7B model outperforms MPT-7B on 60% of the prompts. LLaMA 2-Chat 34B has an overall win rate of more than 75% against equivalently sized Vicuna-33B and Falcon 60B models.
```

Feel free to modify any part if needed!