Here’s the extracted content in markdown format:

```markdown
| Language | Percent | Language | Percent |
|----------|---------|----------|---------|
| en       | 89.70%  | uk       | 0.07%   |
| unknown  | 8.38%   | ko       | 0.06%   |
| de       | 0.17%   | ca       | 0.04%   |
| fr       | 0.16%   | sr       | 0.04%   |
| sv       | 0.15%   | id       | 0.03%   |
| zh       | 0.13%   | cs       | 0.03%   |
| es       | 0.13%   | fi       | 0.03%   |
| ru       | 0.13%   | hu       | 0.03%   |
| nl       | 0.12%   | no       | 0.03%   |
| it       | 0.11%   | ro       | 0.03%   |
| ja       | 0.10%   | bg       | 0.02%   |
| pl       | 0.09%   | da       | 0.02%   |
| pt       | 0.09%   | sl       | 0.01%   |
| vi       | 0.08%   | hr       | 0.01%   |

**Table 10:** Language distribution in pretraining data with percentage ≥ 0.005%. Most data is in English, meaning that LLaMA 2 will perform best for English-language use cases. The large unknown category is partially made up of programming code data.

### Safety Benchmarks for Pretrained Models
We evaluate the safety capabilities of LLaMA 2 on three popular automatic benchmarks, pertaining to three key dimensions of LM safety.

1. **Truthfulness**, referring to whether a language model produces known falsehoods due to inconsistency or false beliefs. We employ TruthfulQA (Lin et al., 2021) to measure how well our LLMs can generate reliable outputs that agree with factuality and common sense.

2. **Toxicity**, defined as the tendency of a language model to generate toxic, adversarial, or implicitly hateful content. We chose ToxiGen (Hartvigsen et al., 2022) to measure the amount of generation of toxic language and hate speech across different groups.

3. **Bias**, defined as how model generations reproduce existing stereotypical social biases. We use BOLD (Dhamala et al., 2021) to study how the sentiment in model generations may vary with demographic attributes.

We compare the performance of LLaMA 1 with LLaMA 2 (Touvron et al., 2023; Fan et al., 2023), and MPT (MosaicML NLP Team et al., 2023) in Table II. For decoding, we set temperature to 0.1 and use nucleus sampling (Holtzman et al., 2020) with top-p set to 0.9. For TruthfulQA, we present the percentage of generations that are both truthful and informative (the higher, the better). For ToxiGen, we present the percentage of generations that are deemed toxic by the metric (the lower, the better). Detailed descriptions of the benchmarks and metrics can be found in Appendix A.4.7. When compared to LLaMA 2-7B, LLaMA 2-7B demonstrates a 21.37% increase in truthfulness and informativeness and a 21.67% decrease in toxicity. We also observe an increase in toxicity in the pretrained 13B and 70B LLaMA 2, which may result from larger pretraining data or a different dataset mix. Some have published the existence of a relationship between pretraining dataset size and downstream model toxicity or bias (Bender et al., 2021b), but empirical work to validate this claim is still ongoing (Dodge et al., 2021; Smith and Williams, 2021; Tal et al., 2022), and further evidence from up-to-date models is still needed.

In Appendix A.4.7, we present the bias metrics, such as how the sentiment of model generations varies with demographic attributes. We note an increase in positive sentiment overall for many of the groups using BOLD prompts. More detailed results split by different demographic groups can be found in Appendix A.4.8.

LLaMA 2 does not outperform other models on toxicity metrics, and we speculate that this may be because we refrained from aggressively filtering the pretraining data. Recall that leaving pretraining data unfiltered may enable base models trained to perform well on more downstream tasks (including hate speech detection), and it carries less risk of accidentally filtering out some demographic groups. We observe that models trained from less aggressively filtered pretraining data also required fewer examples to achieve reasonable safety-alignment. We reiterate that this motivated choice does imply that additional safety mitigations should be applied before deployment of base LLaMA 2 models.
```