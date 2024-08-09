
# Table 15: Performance with tool use

| Model       | ASDiv | SVAMP | MAWPS |
|-------------|-------|-------|-------|
| OPT-66B    | 6.0   | 4.9   | 7.9   |
| GPT-1      | 7.5   | 5.2   | 9.9   |
| GPT-3 CC   | 9.6   | 5.0   | 9.3   |
| GFT-3      | 14.0  | 10.0  | 19.8  |
| Toolformer  | 40.4  | 29.4  | 44.0  |
| LLaMA-2-Chat | 67.1  | 69.2  | 82.4  |

*Evaluation on the math datasets used in Toolformer. For different baselines, we report the scores from Schick et al. (2023).*

---

# Figure 23: Tool use emergence 

*LLaMA-2-Chat is able to understand the tool's applications, and the API arguments, just through the semantics, despite never having been trained to use tools.*

The release of OpenAI's plugins has incited substantial discourse within the academic community, igniting questions such as: 

- *How can we effectively teach models to utilize tools?* 
- *Does the process necessitate a substantial dataset?*

Our experiments indicate that tool usage can spontaneously emerge from alignment in a zero-shot manner. Although we never explicitly annotated tool-use usage, **Figure 23** exhibits an instance where the model demonstrated the capability to utilize a sequence of tools in a zero-shot context.

In addition, our study extended to evaluating the LLaMA 2-Chat with access to a calculator. The results from this particular experiment are documented in Table 15. LLM tool use, while exciting, can also cause some safety concerns. We encourage more community research and red teaming in this area.

## 5.2 Limitations and Ethical Considerations

LLaMA 2-Chat is subject to the same well-recognized limitations of other LLMs, including a cessation of knowledge updates post-pretraining, potential for non-factual generation such as unqualified advice, and a propensity towards hallucinations.

Furthermore, our initial version of LLaMA 2-Chat predominantly concentrated on English-language data. While our experiment observations suggest that the tool usage has garnered some proficiency in other languages, its proficiency is limited, due primarily to the limited amount of pretraining data available in non-English languages (as documented in Table 10). Consequently, the model's performance in languages other than English remains fragile and should be used with caution.

Like other LLMs, LLaMA 2 may generate harmful, offensive, or biased content due to its training on publicly available online datasets. We attempted to mitigate this via fine-tuning, but some issues may remain, particularly for languages other than English where publicly available datasets are not available. We will continue to fine-tune and release updated versions in the future as we progress on addressing these issues.

*Source: [OpenAI ChatGPT Plugins](https://openai.com/blog/chatgpt-plugins)*
