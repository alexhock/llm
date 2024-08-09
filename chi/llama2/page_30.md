```markdown
# Overall safety measures

## Figure 17: Overall safety measures
- **Left:** LLAMA 2-CHAT has low violation percentage overall across model sizes.
- **Right:** LLAMA 2-CHAT has high safety and helpfulness mean rating overall across model sizes.

### (a) Overall violation percentage
![Overall violation percentage](#)

### (b) Overall safety and helpfulness mean rating
![Overall safety and helpfulness mean rating](#)

## 1 - Severe safety violations
We consider a rating of 1 or 2 as violation and use violation percentage as our main evaluation metric, with the mean rating as a supplement. Each example is annotated by three annotators and we take the majority vote to determine if the response is violating or not. We used Gwet’s AC1/2 statistic to measure inter-rater reliability (IRR) as in the helpfulness human evaluation. The IRR scores range from 0.70 to 0.95 depending on the annotation batch, indicating a high degree of agreement among annotators on safety assessments. 

On LLAMA 2-CHAT annotations, the average IRR is 0.90 according to Gwet’s AC2 measure. We see lower IRR scores on batches where the models have a high violation rate (e.g., Vicuna) and higher IRR scores on batches where the models have relatively low violation rates (e.g., LLAMA 2-CHAT, Falcon, and ChatGPT).

## Figure 18: Single-turn and multi-turn violation percentage
We show the overall violation percentage and safety rating of various LLMs in Figure 17. LLAMA 2-CHAT has comparable or lower overall violation percentage across model sizes, while ChatGPT and Falcon (Almazrouei et al., 2023) come next, then MPT (Masaoloff et al., 2023) and Vicuna (Chang et al., 2023). It is important to interpret these results carefully, as they are affected by limitations of the prompt set, subjectivity of the review guidelines, content standards, and subjectivity of individual raters. 

Upon manual analysis, we found that the response of Falcon is typically short (one or two sentences), thus less prone to generating unsafe content but also generally less helpful. This is reflected by a large number of responses of Falcon with rating = 3. As a result, we note that in Figure 17b the average rating of Falcon is much lower than LLAMA 2-CHAT (34B) although their violation percentages look similar (3.8 vs 4.5).
```