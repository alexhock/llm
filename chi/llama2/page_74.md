
|       |         |         |         |         |         |         |         |         |         |         |         |         |         |         |
|-------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
|       |  Meta   |  Slicing|  Hashtag|  Copilot|  FBA     |  AdRe  |  Source |  Elicitation|  Base  |  NLM   |  Refinement |  Evaluators|  Engineers|  User    |  Copilot |  Industrial |
|-------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| Preset|  Summer |  0.00   |  0.00   |  0.00   |  0.00   |  0.10   |  0.12   |  0.00   |  0.00   |  0.30   |  0.32   |  0.00   |  0.00   |  0.00   |  1.00   |
| Item  |  0.00   |  0.06   |  0.00   |  0.08   |  0.00   |  0.10   |  0.12   |  0.16   |  0.17   |  0.30   |  0.32   |  0.34   |  0.00   |  0.00   |  1.00   |
| ...   |  ...    |  ...    |  ...    |  ...    |  ...    |  ...    |  ...    |  ...    |  ...    |  ...    |  ...    |  ...    |  ...    |  ...    |  ...    |
|       |         |         |         |         |         |         |         |         |         |         |         |         |         |         |         |

Table 50: Distribution of mean sentiment scores across groups under the profession domain from the BOLD prompts.

---

### A.5.2 Negative User Experience Categories
There are different kinds of responses that could cause a negative user experience when interacting with our models. We have instructed the annotators to avoid writing responses that violate our safety guidelines, for example, we ask that prompts they write do not:

1. Promote or enable criminal activities.
2. Promote or enable dangerous behaviors to the user or other people.
3. Contain, promote or enable offensive and abusive behavior towards the user or other people.
4. Contain, promote or enable sexually explicit content.

### A.5.3 Quality Assurance Process
We have implemented a quality assurance process to ensure we only use high quality annotations for training the model. For this process, a team of highly skilled content managers manually reviewed the annotations and approved the ones that would be used.

During the quality assurance step, reviewers were asked to only approve those annotations that matched our guidelines: (a) they are consistent with the dialogue history, (b) follow instructions in the prompt, (c) are free of grammatical, spelling and other writing errors, and (d) do not fall into any of the categories described in Section A.5.2. If an annotation needed small changes to be approved, due to grammar or spelling mistakes, or to improve the structure, cohesiveness and style of the text, reviewers could edit it to fix the issues and approve it. If the answer could not be approved without major changes, the reviewers were asked to reject it and write the feedback necessary to improve it.

### A.5.4 Annotator Selection
To select the annotators who could work on our different data collection tasks, we conducted a multi-step assessment process where we tested their understanding of our guidelines, the alignment with our quality assessment criteria, the alignment with our sensitive topics guidelines and their reading and writing skills.

The process included 4 tests:

- The first test consists of 3 sections of testing to evaluate grammar, reading comprehension and writing style. Each section is timed and the test should take a total of 50 minutes to complete. A candidate must score 90% on part I to continue on to parts II and III, and an average score of 4 on part II and III to pass the test.

- The second test consisted of 42 questions split into sensitive topics alignment, answer ranking and two examples of answer writing, which were manually reviewed by us. To pass the test, annotators needed to agree with our criteria on 80% of the answers, and pass the written examples with a score of 4 out of 5.
