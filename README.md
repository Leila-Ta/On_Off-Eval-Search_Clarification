# On&Off_Eval(Search-Clarification)

The effectiveness of clarification question models in engaging users within search systems is currently constrained, casting doubt on their overall usefulness. To improve the performance of these models, it is crucial to employ assessment approaches that encompass both real-time feedback from users (online evaluation) and the characteristics of clarification questions evaluated through human assessment (offline evaluation). However, the relationship between online and offline evaluations has been debated in information retrieval. This study aims to investigate how this discordance holds in search clarification. We use user engagement as ground truth and employ several offline labels to investigate to what extent the offline ranked lists of clarification resemble the ideal ranked lists based on online user engagement. Contrary to the current understanding that offline evaluations fall short of supporting online evaluations, we indicate that when identifying the most engaging clarification questions from the user's perspective, online and offline evaluations correspond with each other. We show that the query length does not influence the relationship between online and offline evaluations, and reducing uncertainty in online evaluation strengthens this relationship. We illustrate that an engaging clarification needs to excel from multiple perspectives, and SERP quality and characteristics of the clarification are equally important. We also investigate if human labels can enhance the performance of Large Language Models (LLMs) and Learning-to-Rank (LTR) models in identifying the most engaging clarification questions from the user's perspective by incorporating offline evaluations as input features. Our results indicate that Learning-to-Rank models do not perform better than individual offline labels. However, GPT, an LLM, emerges as the standout performer, surpassing all Learning-to-Rank models and offline labels.
This repository contains 2 folders. The first one includes the Phyton code that was used to generate the GPT-prompt, the second one contains the codes that were used to define various LTR features and the third one is the code to implement the NDCG evaluation in the analysis.
The second folder contains the GPT-prompts and the results of GPT engagement prediction at different temp values. 

## Citation
If you found MIMICS-Duo useful, you can cite the following article:
```
Leila Tavakoli, Johanne R. Trippas, Hamed Zamani, Falk Scholer, and Mark Sanderson. Online and Offline Evaluation in Search Clarification", TOIS 2024.
```

bibtex:
```

```

