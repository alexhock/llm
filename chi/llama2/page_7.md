Here’s the extracted content in markdown format:

```markdown
## Table 2: CO₂ emissions during pretraining

| Time        | Power (GPU Hour) Consumption (W) | Carbon Emitted (tCO₂eq) |
|-------------|------------------------------------|--------------------------|
| LLaMA 7B   | 381320                                 | 400                      | 31.32                    |
| LLaMA 13B  | 368640                                 | 400                      | 62.44                    |
| LLaMA 34B  | 1083360                                | 350                      | 153.90                   |
| LLaMA 70B  | 1272160                                | 400                      | 291.42                   |
| **Total**   | **131616**                            |                          | **539.00**              |

Carbon Footprint of Pretraining. Following preceding research (Bender et al., 2012a; Patterson et al., 2021; Wu et al., 2022; Dodge et al., 2022) and using power consumption estimates of GPU devices and carbon efficiency, we aim to calculate the carbon emissions resulting from the pretraining of LLaMA 2 models. The actual power usage of a GPU is dependent on its utilization and is likely to vary from the Thermal Design Power (TDP) that we employ as an estimation for GPU power. It is important to note that our calculations do not account for further power demands, such as those from interconnect or non-GPU server power consumption, nor from datacenter cooling systems. Additionally, the carbon output related to the production of AI hardware, like GPUs, could add to the overall carbon footprint as suggested by Gu et al. (2022a).

Table 2 summarizes the carbon emission for pretraining the LLaMA 2 family of models. A cumulative of 3.3M GPU hours of computation was performed on hardware of type A100-80GB (TDP of 400W). We estimate the total emissions for training to be 539 tCO₂eq, of which 100% were directly offset by Meta’s sustainability program. Our open release strategy also means that these pretraining costs will not need to be incurred by other companies, saving more global resources.

## 2.3 LLaMA 2 Pretrained Model Evaluation

In this section, we report the results for the LLaMA 1 and LLaMA 2 base models, MosaicML Pretrained Transformer (MPT)* models, and Falcon (Almazroi et al., 2023) models on standard academic benchmarks. For all the evaluations, we use our internal evaluations library. We reproduce results for the MPT and Falcon models internally. For these models, we always pick the best score between our evaluation framework and any publicly reported results.

In Table 3, we summarize the overall performance across a suite of popular benchmarks. Note that safety benchmarks are shared in Section 4.1. The benchmarks are grouped into the categories listed below. The results for all the individual benchmarks are available in Section A.2.

- **Code.** We report the average pass@1 scores of our models on HumanEval (Chen et al., 2021) and MBPP (Austin et al., 2021).
- **Commonsense Reasoning.** We report the average of PIQA (Bisk et al., 2020), SQuAD (Rajpurkar et al., 2016), HellaSwag (Zellers et al., 2019a), WinOGRAD (Sakaguchi et al., 2021), ARC easy and challenge (Clark et al., 2018), OpenBookQA (Mihaylov et al., 2018), and CommonsenseQA (Talmor et al., 2018). We report 7-shot results for CommonsenseQA and 0-shot results for all other benchmarks.
- **World Knowledge.** We evaluate the 5-shot performance on NaturalQuestions (Kwiatkowski et al., 2019) and TriviaQA (Joshi et al., 2017) and report the average.
- **Reading Comprehension.** For reading comprehension, we report the 0-shot average on SQuAD (Rajpurkar et al., 2018), QuAC (Choi et al., 2018), and BoolQ (Clark et al., 2019).
- **MATH.** We report the average of the CSMK8 (8 shot) (Cobbe et al., 2021) and MATH (4 shot) (Hendrycks et al., 2021) benchmarks at tip 1.

*https://sustainability.fb.com/2021-sustainability-report/
*https://www.mosaicml.com/blog/mpt-7b
```

This markdown includes the table and the related text extracted from the image.