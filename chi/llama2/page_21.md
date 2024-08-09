```markdown
# Gender Pronouns and Grammatical Person

| Gender Pronouns | Percentage |
|------------------|------------|
| She (she, her, hers, herself) | 28.45% |
| He (he, him, his, himself)   | 50.73% |
| Unspecified (they, them, their, ...) | 56.38% |
| Total Documents Containing Gendered Pronouns | 75.23% |
| Grammatical Person | 94.47% |
| 1st (I, me, my, mine, myself, ...) | 90.71% |
| 2nd (you, your, yours, ...) | 61.80% |
| 3rd (it, its, itself, she, her, he, him, ...) | 93.07% |

### (a) Percentage of documents containing gender pronouns and grammatical person. 

75% of all documents contain gendered pronouns. Within this subset, 28% of all documents contain She pronouns; 94% of all documents contain pronouns in general. See full details in Appendix A.4.3.

# Demographic Representations

| Descriptor | % Doc |
|------------|-------|
| **Gender and Sex** | 59.1% |
| Female | 50.0% |
| Male | 39.5% |
| Feminine | 5.4% |
| Transgender | 4.2% |
| Masculine | 3.1% |

| Descriptor | % Doc |
|------------|-------|
| **Sexual Orientation** | 6.67% |
| Gay | 14.8% |
| Lesbian | 4.3% |
| LGBT | 4.0% |
| Queer | 3.6% |

| Descriptor | % Doc |
|------------|-------|
| **Nationality** | 14.83% |
| American | 69.4% |
| Indian | 16.5% |
| Chinese | 16.3% |
| Korean | 5.1% |
| Mexican | 4.9% |

| Descriptor | % Doc |
|------------|-------|
| **Race and Ethnicity** | 19.15% |
| African | 11.5% |
| Asian | 7.4% |
| Latinx | 6.2% |
| Indigenous | 3.7% |
| Jewish | 13.0% |

| Descriptor | % Doc |
|------------|-------|
| **Religion** | 7.93% |
| Christian | 33.25% |
| Religious | 28.5% |
| Spiritual | 20.6% |
| Catholic | 15.4% |

### (b) The percentage listed below each demographic axis represents the percentage of all documents that mention any descriptor in this axis. The percentage listed for each demographic descriptor represents the documents that mention a descriptor in the given demographic axis, the percentage that mention this specific descriptor.

# Data Toxicity

We measure the prevalence of toxicity in the English-language portion of the pretraining corpus using a HateBERT classifier fine-tuned on the Tox21 dataset (Hartvigsen et al., 2022). We score each line of a document separately and average them to assign a document score. About 0.2% of documents evaluated are assigned a likelihood score of 0.5 or higher, meaning there is a small amount of toxicity in our pretraining data.

# Language Identification

While our pretraining data is mostly English, it also includes text from a small number of other languages. Table 10 shows the distribution of languages in our corpus, subsetted to those found in more than 0.005% of the documents. Our analysis uses fastText (Bojanowski et al., 2016) language identification tool and a threshold of 0.5 for the language detection. A training corpus with a majority in English means that the model may not be suitable for use in other languages.
```