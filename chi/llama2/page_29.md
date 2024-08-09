```markdown
The red teamers probed our models across a wide range of risk categories (such as criminal planning, human trafficking, regulated or controlled substances, sexually explicit content, unqualified health or financial advice, privacy violations, and more), as well as all potential attack vectors (such as psychological questions, malformed/misspelled inputs, or extended dialogues). Additionally, we conducted specific tests to determine the capabilities of our models to facilitate the production of weapons (e.g., nuclear, biological, chemical, and cyber); findings on these topics were marginal and were mitigated. Nonetheless, we will continue our red teaming efforts on this front.

To date, all of our red teaming efforts have targeted model outputs in English, but we critically included non-English prompts and dialogue contexts, as that is a well-known attack vector. In all exercises, participants were given risk category definitions and were shown just a handful of examples of risky interactions with an LLM. After that, each participant was part of a subteam focused on a particular category of risk or attack vector. After creating each dialogue, the red team participant would annotate various attributes, including risk areas and degree of risk, as captured by a 5-point Likert scale.

Some examples of useful insights provided by members of red teams that we were able to improve upon through development:

- **[Early models]** were more likely to have generated unsafe responses without noting that they contained problematic content. However, slightly later models have tended to display knowledge that the content is problematic, even if they do go on to provide it. They responded with: "I revised that '[UNSAFE CONTENT]' is not appropriate to discuss, etc.' and then immediately follow up with 'With that said, here's how [UNSAFE CONTENT]…'."

- Distracting the **[early models]** by including "quirks" or specific requests usually defeated any reluctance encountered via more direct requests. "A cringe writing request (song, story, poem, etc.) is a reliable way to get it to produce content that is otherwise robust against."

- Embedding a problematic request in a positive context successfully obscured the fact that the problematic output was being requested for **[early models]**: "The central principle I've found most effective for any kind of attack is to hide it in language that is positive, progressive, and empowering."

From Red Teaming Insights to Safer Models. 

Actually, after each exercise, we performed a thorough analysis of the collected data, including dialogue length, risk area distribution, histogram of type of misinformations (where appropriate), and rated degree of risk. In each case, we took the overall lessons as a guide to help further model safety training, and specifically took data from these exercises for more fine-tuning model feedback training, and as a signal for other safety model training.

Multiple additional rounds of red teaming were performed over several months to measure the robustness of each new model as it was released internally. We defined the robustness of a model, r, with respect to a red teaming exercise executed by a set of experts as the average numbered prompts that would trigger a violating response from the model per person hour. As an example, on our 7B model, we had an evolution of 1.8 ± 0.5 over several red teaming iterations and model refinements. Robustness will likely continue to improve with additional red teaming efforts. Another measure that tracked as new models were produced was the percentage of prompts triggering violating responses discovered in the previous red team model order each week. On average, we had a 90% rejection rate model order clock.

### 4.4 Safety Evaluation of LLaMA 2-Chat

#### Safety Evaluation.

We collected roughly 2,000 adversarial prompts for human evaluation according to the safety categories in Section 4.2.1, in which 1,351 prompts are single-turn and 623 are multi-turn. Examples of evaluation prompts and responses can be found in Appendix A.6.

We then asked raters to judge models for safety violations on a five-point Likert scale with the following definitions:

- **5** - No safety violations and very helpful
- **4** - No safety violations and only minor non-safety issues
- **3** - No safety violations but not helpful or other major non-safety issues
- **2** - Mild or moderate safety violations
```
