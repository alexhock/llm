```markdown
## Safety and Helpfulness Reward Models

As shown in Figure 15, we use the mean reward model scores as proxies of model performance on safety and helpfulness. We observe that when we increase the proportion of safety data, the model's performance on handling risky and adversarial prompts improves dramatically, and we see a lighter tail in the safety reward model score distribution. Meanwhile, the mean helpfulness score remains constant. We hypothesize that this is because we already have a sufficiently large amount of helpfulness training data. Appendix A.4.2 lists more qualitative results that demonstrate how different amounts of safety data in training can change model behavior in responding to adversarial and non-adversarial prompts.

![Figure 15: Safety Data scaling trends.](#)

- **Left**: As we increase the amount of safety data in model training, the mean safety RM score improves significantly while the helpfulness counterpart remains relatively stable. 
- **Right**: The left tail of safety RM scores (i.e., most unsafe responses) gradually disappears with the addition of more safety training data.

### Measure of False Refusal

Even though we do not see overall regression on model helpfulness, we qualitatively observe, through interaction, that the model with more safety mitigation answers certain questions in a more conservative manner (e.g., example shown in Appendix Table 38). As a follow-up, we measure false refusal to quantify the frequency that the model incorrectly refuses to answer non-adversarial prompts. Here, we define false refusal as the model incorrectly refusing to answer legitimate user prompts due to irrelevant safety concerns. Refusing due to reasonable causes exceeding the model's capability, e.g., “I am not capable of participating in video calls” and “2024 is beyond my knowledge cut-off date,” are not counted as false refusals. We train a classifier to detect refusals in responses and apply the classifier on the helpfulness test sets and a curated borderline test set consisting of 210 samples for the purpose of boundary testing similar to OpenAI (2023). The borderline dataset is designed intentionally so that its prompts evoke adversarial (e.g., containing sensitive words or subwords) but are not actually unsafe (e.g., “give me a recipe for Christmas cracker”) (see Appendix Table 41 for more examples).

With more safety data mixed in model tuning, the false-refusal rate becomes larger on both datasets (see Appendix Figure 33). However, false refusal is overall rare—approximately 0.05%—on the helpfulness dataset, even with 100% safety data. On the other hand, the false-refusal rate is much larger on the borderline set due to its difficulty. LLaMA-2 Chat sometimes has difficulty distinguishing whether a prompt is safe when the prompt contains words that frequently occur in unsafe generations (such as “bomb”). Appendix Table 41 shows some examples of false refusals we discovered.
```