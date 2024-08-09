Here's the extracted content in markdown format:

```markdown
# A.7 Model Card

Table 52 presents a model card (Mitchell et al., 2018; Anil et al., 2023) that summarizes details of the models.

| Model Developers | Meta AI |
|------------------|---------|
| Variations       | LLAMA 2 comes in a range of parameter sizes—7B, 13B, and 70B—as well as pretrained and fine-tuned variations. |
| Input            | Models input text only. |
| Output           | Models generate text only. |
| Model Architecture| LLAMA 2 is an auto-regressive language model that uses an optimized transformer architecture. The tuned versions use supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align to human preferences for helpfulness and safety. |
| Model Dates      | LLAMA 2 was trained between January 2023 and July 2023. |
| Status           | This is a stable model trained on an offline dataset. Future versions of the tuned models will be released as we improve model safety with community feedback. |
| License          | A custom commercial license is available at: meta.com/resources/ models-and-libraries/llama-downloads |
| Where to send comments | Instructions on how to provide feedback or comments on the model can be found in the model README, or by opening an issue in the GitHub repository (https://github.com/facebookresearch/llama/). |

## Intended Use

LLAMA 2 is intended for commercial and research use in English. Tuned models are intended for assistant-like use, whereas pretrained models can be adapted for a variety of natural language generation tasks.

### Out-of-Scope Uses
Use in any manner that violates applicable laws or regulations (including user compliance laws). Use in languages other than English. Use in any other way that is prohibited by the Acceptable Use Policy and Licensing Agreement for LLAMA 2.

## Hardware and Software (Section 2.3)

### Training Factors
We used custom training libraries, Meta's Research Super Cluster, and production infrastructure for pretraining, fine-tuning, and evaluation when we performed on their cloud compute.

### Carbon Footprint
Pretraining utilized a cumulative 3M CPU hours of computation on hardware of type A10G-SBC (TDP of 350-430W). Estimated total emissions were 359 tCO₂eq, 100% of which were offset by Meta's sustainability program.

## Training Data (Sections 21 and 3)

### Overview
LLAMA 2 was pretrained on 2 trillion tokens from publicly available sources. The fine-tuning data includes publicly available instruction datasets, as well as more some unseen tuning data including non-public examples. Neither pretraining nor the fine-tuning datasets include Meta data itself.

### Data Freshness
The pretraining data has a cut-off of September 2022, but some tuning data is more recent, up to July 2023.

## Evaluation Results

See evaluations for pretraining (Section 2), fine-tuning (Section 3), and safety (Section 4).

### Ethical Considerations and Limitations (Section 5.2)
LLAMA 2 is a new technology that carries risks. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, LLAMA 2 is a potential output cannot be predicted in advance. The model may be incorrect, produce incorrect or objectionable outputs for any proposed use. Therefore, developing any applications of LLAMA 2, developers should perform safety testing and tuning tailored to their specific applications of the model. Please see the Responsible Use Guide available at https://www.meta.com/llama/responsible-user-guide/.
```
