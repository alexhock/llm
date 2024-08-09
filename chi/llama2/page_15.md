Here's the extracted content in Markdown format:

```markdown
regression in some capabilities. For example, RLHF V3 struggled more than previous versions to compose rhyming lines in poems, as discovered through qualitative analysis, suggesting that further investigation into the causes and mitigations for forgetting (Kirkpatrick et al., 2017; Nguyen et al., 2019; Ramasehsan et al., 2021) could be a fruitful area for additional future research.

In response, on subsequent iterations, we modified our strategy, incorporating top-performing samples from all prior iterations, such as those used in RLHF-V1 and RLHF-V2. Although we do not present specific figures, this adjustment demonstrated considerable enhancements in performance and effectively addressed the previously noted issues. This mitigation can be seen as analogous to Synnaeve et al. (2019) and Vinyals et al. (2019) in the RL literature.

We illustrate the benefit of Rejection Sampling in Figure 7. The delta between the maximum and median curves can be interpreted as the potential gain of fine-tuning on the best output. As expected, this delta increases with more samples, since the maximum increases (i.e., more samples, more opportunities to generate a good trajectory), while the median remains stationary. There is a direct connection between exploration and the maximum reward we can obtain among the samples. The temperature parameter also plays an important role for exploration, as a higher temperature enables us to sample more diverse outputs.

In Figure 8, we report for a LAMA-2-CHAR-SFT (left) and a LAMA-2-CHAR-RLHF (right), the maximum reward curves among N samples (with N ∈ [1...100]), for different temperatures. We can observe that the optimal temperature is not constant during the iterative model updates. RLHF has a direct impact on rescaling the temperature. For LAMA-2-CHAR-RLHF, the optimal temperature when sampling between 10 and 100 outputs is T ∈ [1.2, 1.3]. Given a finite compute budget, it is therefore necessary to re-adjust the temperature progressively. Note that this temperature rescaling happens for a constant number of steps for each model, and always starting from the base model on each new KLHF version.

PPO. Before we train our language model following the RL scheme of Stiennon et al. (2020), which uses the reward model as an estimate for the true reward function (human preference) and the pretrained language model as the policy to optimize. During this phase, we seek to optimize the following objective:

$$
\text{arg} \max_{E_{p \sim D_{p_\theta}}} [R(g) | p]
$$

We iteratively improve the policy by sampling prompts p from our dataset D and generations from the policy g and use the PPO algorithm and loss function to achieve this objective.

The final reward function we use during optimization,

$$
R(g) = \hat{R}_{g}(\pi_{g}) - BDKL(\pi_{g} || \text{arg} \pi(g))
$$

contains a penalty term for diverging from the original policy $\pi_g$. As was observed in other works (Stiennon et al., 2020; Ouyang et al., 2022), we find this constraint is useful for training stability, and to reduce reward hacking whereby we would achieve high scores from the reward model but low scores from human evaluation.

We define $R_b$ to be a piecewise combination of the safety ($R_s$) and helpfulness ($R_h$) reward models. We have tagged prompts in our dataset that might elicit potentially unsafe responses and prioritize the scores from the safety model. The threshold of 0.1 is chosen for filtering unsafe responses, corresponding to a precision of 0.80 and a recall of 0.55 evaluated on the Meta Safety test set. We also find it important to weigh the final linear scores (shown here by reversing the sigmoid with the logistic function) in order to increase stability and balance properly with the KL penalty term ($\beta$) above.

- For all models, we use the AdamW optimizer (Loshchilov and Hutter, 2017), with $\beta_1 = 0.9$, $\beta_2 = 0.95$, eps = $10^{-5}$. 
- We use a weight decay of 0.1, gradient clipping of 1.0, and a constant learning rate of $10^{-5}$. 
- For each PPO iteration we use a batch size of 512, a PPO clip threshold of 0.2, a mini-batch size of 64, and take one gradient step per mini-batch. For the 7B and 13B models, we set $\alpha = 0.01$ (KL penalty), and for the 34B and 70B models, we set $\alpha = 0.005$.
```
