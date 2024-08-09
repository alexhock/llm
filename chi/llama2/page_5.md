
## Figure 4: Training of LLaMA 2-Chat

This process begins with the pretraining of LLaMA 2 using publicly available online sources. Following this, we create an initial version of LLaMA 2-Chat through the application of supervised fine-tuning. Subsequently, the model is iteratively refined using Reinforcement Learning with Human Feedback (RLHF) methodologies, specifically through rejection sampling and Proximal Policy Optimization (PPO). Throughout the RLHF stage, the accumulation of iterative reward modeling data in parallel with model enhancements is crucial to ensure the reward models remain within distribution.

## 2 Pretraining

To create the new family of LLaMA 2 models, we began with the pretraining approach described in Touvron et al. (2023), using an optimized auto-regressive transformer, but made several changes to improve performance. Specifically, we performed more robust data cleaning, updated our data mixes, trained on 40% more total tokens, doubled the context length, and used grouped-query attention (GQA) to improve inference scalability for our larger models. Table 1 compares the attributes of the new LLaMA 2 models with the LLaMA 1 models.

### 2.1 Pretraining Data

Our training corpus includes a new mix of data from publicly available sources, which does not include data from Meta's products or services. We made an effort to remove data from certain sites known to contain a high volume of personal information about private individuals. We trained on 2 trillion tokens of data as this provides a good performance-cost trade-off, up-sampling the most factual sources in an effort to increase knowledge and diminish hallucinations.

We performed a variety of pretraining data investigations so that users can better understand the potential capabilities and limitations of our models; results can be found in Section 4.1.

### 2.2 Training Details

We adopt most of the pretraining setting and model architecture from LLaMA 1. We use the standard transformer architecture (Vaswani et al., 2017), apply pre-normalization using RMSNorm (Zhang and Sennrich, 2019), use the SiLU activation function (Shazeer, 2020), and utilize positional embeddings (RoPE, Su et al. 2022). The primary architectural differences from LLaMA 1 include increased context length and grouped-query attention (GQA). We detail in Appendix Section A.2 each of these differences with ablation experiments to demonstrate their importance.

#### Hyperparameters

We trained using the AdamW optimizer (Loshchilov and Hutter, 2017), with β₁ = 0.9, β₂ = 0.95, ε = 10⁻⁷. We use a cosine learning rate schedule, with a warmup of 2000 steps, and decay the final learning rate down to 10% of the peak learning rate. We use a weight decay of 1.0 and gradient clipping of 1.0. Figure 5 (a) shows the training loss for LLaMA 2 with these hyperparameters.
