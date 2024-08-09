
### Table 6: Statistics of human preference data for reward modeling

| Dataset                 | Num. of Comparisons per Dialogue | Avg. # Turns | Avg. # Tokens | Avg. # Tokens in Prompt | Avg. # Tokens in Response |
|------------------------|-----------------------------------|--------------|---------------|-------------------------|---------------------------|
| Anthropic Helpful      | 122,387                           | 3.0          | 251.5         | 177                     | 88.4                      |
| Anthropic Harmless     | 49,563                            | 3.0          | 152.5         | 157.5                   | 6.4                       |
| OpenAI Summarize       | 176,665                           | 1.0          | 371.1         | 336.0                   | 36.0                      |
| OpenAI WebGPT          | 13,333                            | 1.0          | 227.2         | 48.3                    | 189.9                     |
| StackExchange           | 1,038,480                         | 1.0          | 440.2         | 200.1                   | 240.2                     |
| Stanford SHP           | 74,892                            | 1.0          | 138.3         | 199.5                   | 138.3                     |
| Synthetic GPT-J       | 33,199                            | 1.0          | 123.3         | 130.0                   | 110.3                     |
| Meta (Safety & Helpfulness) | 1,418,091                  | 3.9          | 798.5         | 31.4                    | 234.1                     |
| **Total**              | **2,919,326**                     | **1.6**      | **595.7**     | **108.2**               | **216.9**                 |

*Note: We list both the open-source and internally collected human preference data used for reward modeling. Note that a binary human preference comparison contains 2 responses (chosen and rejected) sharing the same prompt (and previous dialogue). Each example consists of a prompt (including previous dialogue if available) and a response, which is the input of the reward model. We report the number of comparisons, the average number of turns per dialogue, the average number of tokens per example, per prompt and per response. More details on Meta helpfulness and safety data per batch can be found in Appendix A.3.1.*

---

### Training Objectives

To train the reward model, we convert our collected pairwise human preference data into a binary ranking label format (i.e., chosen and rejected) and enforce the chosen response to have a higher score than its counterpart. We used a binary ranking loss consistent with Ouyang et al. (2022):

\[
L_{ranking} = -\log(\sigma(r(y_i) - r(y_j)))
\]

where \( r(y_i) \) is the scalar score output for prompt \( x \) and completion \( y \), \( g \) is the preferred response that annotators chose and \( y_j \) is the rejected counterpart.

Built on top of this binary ranking loss, we further modify it separately for better helpfulness and safety reward models as follows. Given that our preference ratings is decomposed as a scale of four points (e.g., significantly better), as presented in Section 3.2.1, it can be useful to leverage this information to explicitly teach the reward model to assign more disparate scores to the generations that have more differences. To do so, we further add a margin component in the loss:

\[
L_{margin} = -\log(\sigma(r(y_i) - r(y_j) - m(y)))
\]

where \( m(y) \) is a discrete function of the preference rating. Naturally, we use a large margin for pairs with distinct responses, and a smaller one for those with similar responses (shown in Table 27). We found this margin component can improve Helpfulness reward model accuracy especially on samples where two responses are more separable. More detailed ablation and analysis can be found in Table 28 in Appendix A.3.3.

### Data Composition

We combine our newly collected data with existing open-source preference datasets to form a larger training dataset. Initially, open-source datasets were used to bootstrap our reward models while we were in the process of collecting preference annotation data. We noted that in this context, the role of reward signals is to learn human preference for LLaMA 2-Chat outputs rather than any model outputs. However, in our experiments, we do not observe negative transfer from the open-source preference datasets. Thus, we have decided to keep them in our data mixture, as they could enable better generalization for the reward model and prevent reward hacking, i.e., LLaMA 2-Chat taking advantage of some weaknesses of our reward, and so artificially linking the score despite performing less well.

With training data available from different sources, we experimented with different mixing recipes for both Helpfulness and Safety reward models to ascertain the best settings. After extensive experimentation, the ...
