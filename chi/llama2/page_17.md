
# GAt Evaluation

We applied GAt after RLHF V3. We report a quantitative analysis indicating that GAt is consistent up to 20+ turns, until the maximum context length is reached (see Appendix A3.5). We tried to set constraints not present in the training of GAt at inference time, for instance "Always answer with Haiku," for which the model remained consistent as illustrated in Appendix Figure 28.

## Attention Visualization

Figure 10: Attention visualization for a dialogue with and without GAt. We considered the maximum activations across the network and bin neighboring tokens together.

To illustrate how GAt helped reshape attention during fine-tuning, we display the maximum attention activations of the model in Figure 10. The left-hand side of each figure corresponds to the system message ("Act as Oscar Wilde"). We can see that the GAt-equipped model (right) maintains large attention activations with respect to the system message for a larger portion of the dialogue, as compared to the model without GAt (left).

Despite its utility, the current implementation of GAt is vanilla, and more development and iteration on this technique could likely further benefit the model. For instance, we could teach the model to change the system message during the conversation by integrating such data during fine-tuning.

## RLHF Results

### Model-Based Evaluation

Evaluating LLMs is a challenging open-research problem. Human evaluation, while a gold standard, can be complicated by various HCI considerations (Clark et al., 2021; Gehrmann et al., 2023), and is not always scalable. Thus, to select the best-performing models among several ablations at each iteration from RLHF-V1 to V5, we first observed the improvement of the rewards from the latest reward models, to save costs and increase iteration speed. We later validated major model versions with human evaluations.

#### How Far Can Model-Based Evaluation Go?

To measure the robustness of our reward model, we collected a test set of prompts for both helpfulness and safety, and asked three annotators to judge the quality of the answers based on a 7-point Likert scale (the higher the better). We observe that our reward models overall are well calibrated with our human preference annotations, as illustrated in Figure 29 in the appendix. This confirms the relevance of using our reward as a point-wise metric, despite being trained with a Pairwise Ranking Loss.

Still, as Goodhart’s Law states, when a measure becomes a target, it ceases to be a good measure. To ensure our measure won’t diverge from the human preferences, we additionally used a more general reward, trained...
