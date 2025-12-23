---
title: "Training Software Engineering Agents and Verifiers with SWE-Gym"
collection: publications
permalink: /publication/2025-10-01-Training-Software-Engineering-Agents-SWE-Gym
date: 2025-10-01
venue: 'ICML'
paperurl: 'https://arxiv.org/abs/2412.21139'
citation: 'Jiayi Pan, Xingyao Wang, Graham Neubig, Navdeep Jaitly, Heng Ji, Alane Suhr, <b>Yizhe Zhang</b>'
topics: ['code-llm-agents']
description: "602 GitHub stars - Training framework for software engineering agents with real-world GitHub tasks"
code: 'https://github.com/SWE-Gym/SWE-Gym'
abstract: "We introduce SWE-Gym, a new training environment containing 2,438 real-world Python tasks, each with an executable codebase, unit tests, and natural language specifications. Fine-tuning language model-based software engineering agents on this dataset achieves up to 19% absolute gains in resolve rate on SWE-Bench Verified and Lite test sets. We further explore inference-time scaling via verifiers trained on agent trajectories, reaching state-of-the-art results for open-weight agents: 32.0% and 26.0% on the respective benchmarks. SWE-Gym, trained models, and agent trajectories are publicly available to support future research."
---

[Download paper here](https://arxiv.org/abs/2412.21139)

Recommended citation:
```bibtex
@inproceedings{pan2025swegym,
  title={Training Software Engineering Agents and Verifiers with SWE-Gym},
  author={Pan, Jiayi and Wang, Xingyao and Neubig, Graham and Jaitly, Navdeep and Ji, Heng and Suhr, Alane and Zhang, Yizhe},
  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},
  year={2025}
}
```
