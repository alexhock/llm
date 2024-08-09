
# 5 Discussion

Here, we discuss the interesting properties we have observed with RLHf (Section 5.1). We then discuss the limitations of LLaMA 2-Chat (Section 5.2). Lastly, we present our strategy for responsibly releasing these models (Section 5.3).

## 5.1 Learnings and Observations

Our tuning process revealed several interesting results, such as LLaMA 2-Chat’s abilities to temporally organize its knowledge, or to call APIs for external tools.

![Figure 20: Distribution shift for progressive versions of LLaMA 2-Chat, from SFT models towards RHLF.](#)

### Beyond Human Supervision

At the outset of the project, many among us expressed a preference for supervised annotation, attracted by its denser signal. Meanwhile, reinforcement learning, known for its instability, seemed a somewhat shadowy field for those in the NLP research community. However, reinforcement learning proved highly effective, particularly given its cost and time effectiveness. Our findings underscore that the crucial determinant of RLHf’s success lies in the synergy it fosters between humans and LLMs throughout the annotation process.

Even with proficient annotators, each individual writes with significant variation. A model fine-tuned on SFT annotation learns this diversity, including, unfortunately, the tail-end of poorly executed annotation. Furthermore, the model’s performance is capped by the writing abilities of the most skilled annotators. Human annotators are arguably less subject to discrepancy when comparing two outputs’ preference annotation for RLHf. Consequently, the reward mechanism swiftly leans to assign low scores to undesirable tail-end distribution and aligns towards the human preference. This phenomenon is illustrated in Figure 20, where we can see that the worst answers are progressively removed, shifting the distribution to the right.

In addition, during annotation, the model has the potential to venture into writing trajectories that even the best annotators may not chart. Nonetheless, humans can still provide valuable feedback when comparing two answers, beyond their own writing competencies. Drawing a parallel, while we may not be accomplished artists, our ability to appreciate and critique art remains intact. We post that the superior writing abilities of LLMs, as manifested in surpassing human annotators in certain tasks, are fundamentally driven by RLHf, as documented in Gilardi et al. (2023) and Huang et al. (2023). Supervised data may no longer be the gold standard, and this evolving circumstance compels a reevaluation of the concept of “supervision.”

### In-Context Temperature Rescaling

We have observed an intriguing phenomenon related to RLHf, a feature not previously reported to the best of our knowledge: the dynamic re-scaling of temperature contingent upon the context. As indicated in Figure 8, the temperature appears to be correlated to RLHf. Intriguingly, our findings also revealed that the shifts are not uniformly applied across all prompts, as shown in Figure 21.

For instance, when it comes to prompts associated with creativity, such as “Write a poem,” an increase in temperature continues to generate diversity across our various RLHf iterations. This can be observed in the Self-BLEU slope, which mirrors a pattern comparable to that of the SFT model.

On the other hand, for prompts based on factual information, such as “What is the capital of Z?”, the Self-BLEU slope diminishes over time. This pattern suggests that despite the rising temperature, the model tends to consistently provide the same response to factual prompts.
