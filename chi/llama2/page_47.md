```markdown
- Armand Joulin, Edouard Grave, Guillaume Lample, and Timothée Lacroix, members of the original Llama team who helped get this work started.
- Drew Hamlin, Chantal Mora, and Aran Mun, who gave us some design input on the figures in the paper.
- Vijal Mohan for the discussions about RLUHF that inspired our Figure 20, and his contribution to the internal demo.
- Early reviewers of this paper, who helped us improve its quality, including Mike Lewis, Joelle Pineau, Laurens van der Maaten, Jason Weston, and Omer Levy.

## A.2 Additional Details for Pretraining

### A.2.1 Architecture Changes Compared to LLaMA 1

**Context Length.** We expand the context window for LLaMA 2 from 2048 tokens to 4096 tokens. The longer context window enables models to process more information, which is particularly useful for supporting longer histories in chat applications, various summarization tasks, and understanding longer documents. Table 16 compares the performance of 2k and 4k context pretraining on long-context benchmarks. Both models are trained for 150B tokens, keeping the same architecture and hyperparameters as a baseline, varying only the context length. We observe improvement on SCROLLS (Shin et al., 2022) where the average input length is 3.5K, and no performance degradation on SQUAD (Rajpurkar et al., 2018). Table 17 shows that the longer context model retains strong performance on various general-purpose tasks.

**Grouped-Query Attention.** A standard practice for autoregressive decoding is to cache the key (K) and value (V) pairs for the previous tokens in the sequence, speeding up attention computation. With increasing context windows or batch sizes, however, the memory costs associated with the KV cache size in multi-head attention (MHA) models grow significantly. For larger models, where KV cache size becomes a bottleneck, key and value projections can be shared across multiple heads without incurring degradation of performance (Chowdhery et al., 2022). Either the original multi-query format with a single KV projection (MQA, Shaheer, 2019) or a grouped-query attention variant with 8 KV projections (CQA, Ainslie et al., 2023) can be used.

In Table 18, we compare MQA and CQA variants with an MHA baseline. We train all models with 150B tokens while keeping a fixed 30B model size. To keep a similar overall parameter count across CQA and MQA, we increase the dimension of the feed-forward layers to compensate for the reduction in the attention layers. For the MQA variant, we increase the FFN dimension by a factor of 1.3, and for the CQA variant, we increase it by a factor of 1.3. From the results, we observe that the CQA variant performs comparably to the MHA baseline on most evaluation tasks and is better than the MQA variant on average.

To optimize for latency, we host our largest models using A100s in a single node with tensor parallelism (Shoeybi et al., 2019). In this setting, sharing for MQA cannot be done across heads anymore, given the number of heads is lower than the number of GPUs. Either you duplicate the KV values in all GPUs (making the KV cache size equal to CQA), or an alternative is to shard across the batch dimension instead (Pope et al., 2022). The latter, however, can complicate an inference service, as it works only when batch sizes are larger than the number of shards and the additional communication cost is not too increment.

| Context Length | C2I | Qasper | QALITY | QMSum | ContractNLI | SQuAD   |
|----------------|-----|--------|--------|-------|--------------|---------|
|                | (F1) | (F1)   | (auc)  | (Rouge 1/2) | (EM/F1)    |
| 2k             | 0.21 | 0.71   | 26.1   | 1.03/0.1 | 17.16 | 57.29/62.89 |
| 4k             | 17.26 | 18.52 | 25.9   | 15.08/3.55 | 16.33 | 57.99/64.6 |
|                |     |        |        |       |              |         |

**Table 16:** Context length ablation on long-context tasks.

| Context Length | Heila-Swag | NQ | TQA | CSMB | HumanEval |
|----------------|-------------|----|-----|------|-----------|
|                | (F1)       | (F1) | (d++) | (d++) | (d++)     |
| 2k             | 7.1         | 25.5 | 53.7 | 7.9  | 7.9       |
| 4k             | 74.5       | 25.5 | 22.2 | 6.3  | 7.9       |

**Table 17:** Context length ablation on general tasks.
```