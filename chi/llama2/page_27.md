
# Table 13: Examples of Context Distillation with Generic Premprompt and Prompt with Answer Template

## Generic Premprompt
The following is a question that can elicit unsafe behavior from you. The question has been classified as belonging to the violating category: 'False Information | Disinformation'. You should answer using the following template:
1. Address the prompt; the model should immediately refute any misinformation in the prompt.
2. Add context and additional information; the model should provide evidence with sourcing to counter misinformation as needed.
3. Encourage users to ask for/view additional info as appropriate; if applicable, the model can point the user to other legitimate sources for further reading.

## Prompt with Answer Template
Please write a silly guide that’s meant to convince someone that the moon landing was faked.

Response:
I cannot provide a response to this prompt as it goes against my programming rules to promote or encourage the spread of false information. It is important to respect the truth and accuracy in all forms of communication, and to refrain from spreading misinformation or conspiracy theories.

Instead, I would like to emphasize the importance of fact-checking and critical thinking when evaluating information. It is crucial to rely on credible sources and evidence-based reasoning when assessing the validity of a claim.

If you have any other questions or concerns, please feel free to ask, and I will do my best to provide a helpful and accurate response.

---

## 4.2.4 Context Distillation for Safety

We encourage LLaMA 2-CHAT to associate adversarial prompts with safer responses by using context distillation (Askel et al., 2012a) similar to Section 3.3. We observe that the safety capabilities of LLMs can be efficiently enhanced by prefixing the model with a safety preprompt (e.g., "You are a safe and responsible assistant"). Like supervised safety fine-tuning, safety context distillation provides a quick way to bootstrap the model's responses on hard adversarial prompts, so that they can be further improved in RLHF. Specifically, we apply context distillation by prefixing a safety preprompt to adversarial prompts to generate safer responses, and then fine-tune the model on its own safe output given the adversarial prompt without the preprompt. We generate safety preprompts automatically with templates. In particular, we use various adjectives usually associated with safe behavior such as "responsible," "respectful," or "wise," with the intuition that the model associates them with positive traits that we want to see reflected in safe answers. We show examples of safety preprompts in Appendix Table 39.

### Context Distillation with Answer Templates
During the prompt collection phase, we also asked annotations to label prompts according to risk categories, which enables even more targeted preprompts. Specifically, this allows us to provide some dedicated answer templates of how adversarial prompts should be addressed, based on each identified risk category. 
