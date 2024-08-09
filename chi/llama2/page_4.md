
## Figure 3: Safety human evaluation results for LLaMA 2-Chat compared to other open-source and closed-source models.

Human raters judged model generations for safety violations across ~2,000 adversarial prompts consisting of both single and multi-turn prompts. More details can be found in Section 4.4. It is important to caveat these safety results with the inherent bias of LLM evaluations due to limitations of the prompt set, subjectivity of the review guidelines, and subjectivity of individual raters. Additionally, these safety evaluations are performed using content standards that are likely to be biased towards the LLaMA 2-Chat models.

We are releasing the following models to the general public for research and commercial use†:

1. **LLaMA 2**, an updated version of LLaMA 1, trained on a new mix of publicly available data. We also increased the size of the pretraining corpus by 40%, doubled the context length of the model, and adopted grouped-query attention (Ainslie et al., 2023). We are releasing variants of LLaMA 2 with 7B, 13B, and 70B parameters. We have also trained 34B variants, which we report on in this paper but are not releasing.‡

2. **LLaMA 2-Chat**, a fine-tuned version of LLaMA 2 that is optimized for dialogue use cases. We release variants of this model with 7B, 13B, and 70B parameters as well.

We believe that the open release of LLMs, when done safely, will be of net benefit to society. Like all LLMs, LLaMA 2 is a new technology that carries potential risks with use (Bender et al., 2021; Weidinger et al., 2022; Solaiman et al., 2023). Testing conducted to date has been in English and has not — and could not — cover all scenarios. Therefore, before deploying any applications of LLaMA 2-Chat, developers should perform safety testing and tuning tailored to their specific applications of the model. We provide a responsible use guide† and code examples† to facilitate the safe deployment of LLaMA 2 and LLaMA 2-Chat. More details of our responsible release strategy can be found in Section 5.3.

The remainder of this paper describes our pretraining methodology (Section 2), fine-tuning methodology (Section 3), approach to model safety (Section 4), key observations and insights (Section 5), relevant related work (Section 6), and conclusions (Section 7).

† [source](https://ai.meta.com/resources/models-and-libraries/llamas/)  
‡ We are delaying the release of the 34B model due to a lack of time to sufficiently red team.  
† [source](https://ai.meta.com/llama)  
† [source](https://github.com/facebookresearch/llama)
