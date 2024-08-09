
| Category                         | Prompt                                                                                          |
|----------------------------------|-------------------------------------------------------------------------------------------------|
| Creative writing                 | Write a short story about a dragon who was evil and then saw the error in [sic] it's ways      |
| Identity / Personas              | You are a unicorn. Explain how you are actually real.                                         |
| Identity / Personas              | You are one of Santa’s elves. What is the big guy like the rest of the year, not in the holiday season? |
| Factual Questions                | How was Anne Frank's diary discovered?                                                         |
| Personal & professional development | I sit in front of a computer all day. How do I manage and mitigate eye strain?             |
| Casual advice & recommendations   | I keep losing my keys. How can I keep track of them?                                          |
| Reasoning (math/problem-solving) | User: A jar contains 60 jelly beans, if 35% of the jelly beans are removed how many are left in the jar?<br> Assistant: If 35% of the jelly beans are removed, then the number of jelly beans left in the jar is 60 - (35% of 60) = 60 - 21 = 39.<br> User: can you expand your answer to show your reasoning?  |

Table 33: Examples of helpfulness prompts

---

Figure 30: Impact of system prompt on human evaluation results for ChatGPT (Left). Win rate per category for LLaMA 2-CHAT 70B compared to ChatGPT using system prompts for both models (Right).

Evaluation Methodology. For evaluations, the human annotators are presented with a prompt and generations from two models side-by-side. They are asked to answer the following question:

Considering both model responses, which is better (helpful while also being safe and honest), Model A or Model B? 

The annotators answer this question on a seven-point scale with the following labels:
- A is much better
- A is better
- A is slightly better
- About the same
- B is slightly better
- B is better
- B is much better.

One of the model generations is a LLaMA 2-CHAT model and the other generation is one of the open source or closed source models. Responses from the two models are randomized in Model A or Model B when presented to the annotators. From this data, we report wins, ties, and losses in our results. Three annotators rate each generation pair. Prior experiments with five annotators did not change the results or inter-annotator agreement significantly.
