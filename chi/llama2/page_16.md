```markdown
## Figure 9: Issues with multi-turn memory (left) can be improved with GAt (right).

We train for between 200 and 400 iterations for all our models, and use evaluations on held-out prompts for early stopping. Each iteration of PPO on the 708 model takes on average ≈ 330 seconds. To train quickly with large batch sizes, we use FSDP (Zhao et al., 2023). This was effective when using O(1) forward or backward passes, but caused a large slow down (≈ 20×) during generation, even when using a large batch size and KV cache. We were able to mitigate this by consolidating the model weights to each node once before generation and then feeding the memory after generation, resuming the rest of the training loop.

### 3.3 System Message for Multi-Turn Consistency

In a dialogue setup, some instructions should apply for all the conversation turns, e.g., to respond succinctly, or to “act as” some public figure. When we provided such instructions to LLaMA-2-Chat, the subsequent response should always respect the constraint. However, our initial RLHF models tended to forget the initial instruction after a few turns of dialogue, as illustrated in Figure 9 (left).

To address these limitations, we propose Ghost Attention (GAt), a very simple method inspired by Context Distillation (Ba et al., 2022) that hacks the fine-tuning data to help the attention focus in a multi-stage process. GAt enables dialogue control over multiple turns, as illustrated in Figure 9 (right).

#### GAt Method

Assume we have access to a multi-turn dialogue dataset between two persons (e.g., a user and an assistant), with a list of messages \(m_1, m_2, \ldots, m_t\), where \(u_t\) and \(a_t\) correspond to the user and assistant messages for turn \(t\), respectively. Then, we define an instruction, \(inst\), that should be respected throughout the dialogue. For example, this could be “act as.” We can then synthetically concatenate this instruction to all the user messages of the conversation.

Next, we can sample from this synthetic data using the latest RLHF model. We now have a context-dialogue and the sample with which to fine-tune a model, in a process analogous to Replica Sampling. Instead of augmenting all context-dialogue turns with the instruction, we can drop it in all but the first turn, but this would lead to a mismatch at training time between a system message, i.e., all the immediate assistant messages that come before the last turn, and our sample. To fix this issue, which could hinder training, we simply set the loss to 0 for all the tokens from the previous turns, including assistant messages.

For the training instructions, we created a few syntactic constraints to sample from: Hobbies (“You enjoy e.g. Tennis”), Language (“Speak in e.g. French”), or Public Figure (“Act as e.g. Napoleon”). To obtain the lists of hobbies and public figures, we asked LLaMA-2-Chat to generate it, avoiding a mismatch between the instruction and model knowledge (e.g., asking the model to act as someone it had not encountered during training). To make the instructions more complex and diverse, we constructed the final instruction by randomly combining the above constraints. When constructing the final system message for the training data, we also
```
