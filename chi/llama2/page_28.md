```markdown
## Figure 16: Context Distillation Analysis

### (a) Impact on Safety RM Score
- **Left:** Distribution of safety RM scores from the base model, when adding a generic preprompt, and when adding a preprompt based on the risk category with tailored answer template. While a generic preprompt increases safety RM scores, a preprompt with tailored answer template helps even more.

### (b) Targeted Context Distillation
- **Right:** Context distillation increases the RM score significantly for samples that initially have a low score, but can also have a detrimental effect on samples that initially have a high score. We therefore only apply context distillation on targeted samples when it increases RM score.

---

### Rejecting Context Distillation Errors with the Safety Reward Model
It is important to note that performing safety context distillation for helpful prompts can degrade model performance and lead to more false refusals (see Appendix Table 40). We therefore perform safety context distillation only on adversarial prompts. 

However, we observed that context distillation can sometimes degrade response quality, even when dealing with adversarial prompts. Specifically, if the model responses are already of high quality, the application of context distillation can result in less pertinent replies, as the model tends to overemphasize the preprompt, often resorting to generic concerns excessively (see Appendix Table 40 for an example of vague answers due to context distillation). We thus leverage the safety reward model to decide whether to use safety context distillation - we keep the context-distilled output only on the examples where it gets a better reward model score than the original answer. We notice that this is particularly helpful on prompts that the model is very bad at, but limits the negative impact of context distillation (see Figure 16b).

### 4.3 Red Teaming
Given how broad the capabilities of LLMs are and how varied their training data is, it is insufficient to identify risks solely via a static factor usage and analysis. Rather, as has been done for other LLMs, we perform various kinds of proactive risk identification, colloquially called "red teaming", based on the term commonly used within computer security. This kind of granular analysis is very important because safety is a long-tail issue, in which even very unrepresented edge cases can cause noticeable problems. Even if quantitative scores report good results, these types of qualitative signals allow us to recognize and target specific patterns in a more comprehensive way.

We conducted a series of red teaming with various groups of internal employees, contract workers, and external vendors. These teams included over 350 people, including domain experts in cybersecurity, electronic fraud, social media misinformation, legal, policy, civil rights, ethics, software engineering, machine learning, responsible AI, and creative writing. They also included individuals representative of a variety of socioeconomic, gender, ethnicity, and racial demographics.
```
