```markdown
### A.3.7  Human Evaluation

**Prompts and Generations.** To compare the models, we collect a diverse set of over 4000 single and multi-turn prompts. We manually collected single turn prompts spanning the following categories: factual questions, writing and content creation, language assistance, recommendations, and dialogue. For multi-turn prompts, annotators interacted with another model to generate a set of multi-turn prompts. To help ensure fairness, we asked annotators to collect multi-turn prompts by using four different interaction methods: (a) ChatGPT as the interaction model, (b) LLaMA 2-Chat as the interaction model, (c) best response between ChatGPT and LLaMA 2-Chat at every turn. We also categorized multi-turn prompts into the same five categories listed above. Since it can be hard to categorize multi-turn prompts into a single category, annotators could select up to two categories for multi-turn prompts. Example evaluation prompts can be seen in Table 33.

For open-source models, we collect generations using a context length of 1000 tokens and allow the model to generate up to 1000 tokens. Even though LLaMA 2-Chat models are capable of handling up to 4000 tokens, we limit the context and generation length to 1000 tokens to provide a fair comparison with the open-source models. Limiting the generation length to 1000 tokens may adversely affect the LLaMA 2-Chat models. Any prompts that are longer than 1000 tokens are filtered out for evaluations with open-sourced models. For MPT models, we use the most-recent 7b-chat model. For Falcon models, we use the Falcon-40B-Instruct model which is a chat/instruct model. For Vicuna models, we use vicuna-13b-delta-v1.1 and vicuna-7b-delta-v1.1 models from Imsys. All model weights were obtained from HuggingFace.

Since closed-source models have longer context lengths, we change the context length and generation length to 2000 tokens for these models. To evaluate with closed source models, we collect another set of generations with 2000 context and generation length.

While collecting generations, we appended a system prompt prior to the prompt for evaluation. The system prompt for each model is shown in Table 31. Since ChatGPT, PaLM, and Falcon do not provide a system prompt, we use the same system prompt as LLaMA 2-Chat model. Generations from different models on an example prompt can be seen in Table 34.

**Table 31:** System prompts for model generations for human evaluations.

| Model          | System Prompt |
|----------------|---------------|
| LLaMA 2-Chat, ChatGPT, PaLM-chat, Falcon | You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. |
| MPT | If a question does not make any sense, or is not factually correct, explain why instead of answering something not correct. If you don’t know the answer to a question, please don’t share false information. |
| Vicuna | A conversation between a user and an LLM-based AI assistant. The assistant gives helpful and honest answers. |
| Falcon | A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user’s questions. |

**Table 32:** Number of prompts for human evaluations.

| Comparison Model | Number of single turn prompts | Number of multi-turn prompts |
|------------------|-------------------------------|------------------------------|
| ChatGPT          | 1917                          | 2256                         |
| PaLM-chat        | 1869                          | 2143                         |
| Falcon           | 1917                          | 1960                         |
| MPT              | 1917                          | 1293                         |
| Vicuna           | 1917                          | 1300                         |
```
