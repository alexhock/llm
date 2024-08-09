Sure! Here’s the extracted content in markdown format:

```markdown
## 4.2.2 Safety Supervised Fine-Tuning

In accordance with the established guidelines from Section 4.2.1, we gather prompts and demonstrations of safe model responses from trained annotators, and we use the data for supervised fine-tuning in the same manner as described in Section 3.1. An example can be found in Table 5.

The annotators are instructed to initially come up with prompts that they think could potentially induce the model to exhibit unsafe behavior, i.e., perform red teaming, as defined by the guidelines. Subsequently, annotators are tasked with crafting a safe and helpful response that the model should produce.

## 4.2.3 Safety RLHF

We observe early in the development of LLaMA 2-Chat that it is able to generalize from the clean demonstrations in supervised fine-tuning. The model quickly learns to write detailed safe responses, address safety concerns, explain why the topic might be sensitive, and provide additional helpful information. In particular, when the model outputs safe responses, they are often more detailed than what the average annotator writes. Therefore, after gathering only a few thousand supervised demonstrations, we switched entirely to RLHF to teach the model how to write more nuanced responses. Comprehensive tuning with RLHF has the added benefit that it may make the model more robust to jailbreak attempts (Bai et al., 2022a).

We conduct RLHF by first collecting human preference data for safety similar to Section 3.2.2: annotators write a prompt that they believe can elicit unsafe behavior, and then score multiple model responses to the prompts, selecting the response that is safest according to a set of guidelines. We then use the human preference data to train a safety reward model (see Section 3.2.2), and also reuse the adversarial prompts to sample from the model during the RLHF stage.

### Better Long-Tail Safety Robustness without Hurting Helpfulness

Safety is inherently a long-tail problem, where the challenge comes from a small number of very specific cases. We investigate the impact of Safety RLHF by taking two intermediate LLaMA 2-Chat checkpoints—one without adversarial prompts in the RLHF stage and one with them—and score their responses on our sets using our helpfulness reward models. In Figure 14, we plot the score distribution of the safety RM on the safety test set (left) and that of the helpfulness RM on the helpfulness test set (right). In the left-hand side of the figure, we observe that the distribution of safety RM scores on the safety test shifts to higher reward scores after safety tuning with RLHF, and that the long tail of the distribution near zero thins out. A clear cluster appears on the top-left corner suggesting the improvements in model safety. On the right side, we do not observe any shrinking pattern below the y = x line on the right hand side of Figure 14, which indicates that the helpfulness score distribution is preserved after safety tuning with RLHF. But another way, we distinguish helpfulness training data, the addition of an additional stage of safety augmentation does not negatively impact model performance on helpfulness in any notable degradation. A qualitative example is shown in Table 12.

### Impact of Safety Data Scaling

A tension between helpfulness and safety of LMs has been observed in previous studies (Bai et al., 2022a). To better understand how the addition of safety training data affects general model performance, especially helpfulness, we investigate the trends in safety data scaling by adjusting the amount of safety data used in the RLHF stage. In this ablation experiment, we keep the amount of helpfulness training data unchanged (≈ 0.9M samples) and gradually increase the amount of safety data used in model tuning, ranging from 0% to 100% (≈ 0.1M samples). For the specific training data mix recipe, we follow the procedure described in Section 3.1 and fine-tune LLaMA 2: a pretrained model for 2 epochs.

We eventually obtain 6 model variants trained with 0%, 1%, 10%, 25%, 50%, and 100% of the total safety data. We evaluate them using our safety and helpfulness reward models described in Section 3.2.2 for
```
