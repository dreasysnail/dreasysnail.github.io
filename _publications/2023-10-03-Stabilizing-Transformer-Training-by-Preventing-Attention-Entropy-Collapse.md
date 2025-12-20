---
title: "Stabilizing Transformer Training by Preventing Attention Entropy Collapse"
collection: publications
permalink: /publication/2023-10-03-Stabilizing-Transformer-Training-by-Preventing-Attention-Entropy-Collapse
date: 2023-10-03
venue: 'ICML'
paperurl: 'https://arxiv.org/abs/2303.06296'
citation: 'Shuangfei Zhai, Tatiana Likhomanenko, Etai Littwin, Dan Busbridge, Jason Ramapuram, <b>Yizhe Zhang</b>, Jiatao Gu, Joshua M Susskind'
description: "σReparam prevents attention entropy collapse, enabling stable training without warmup or adaptive optimizers"
abstract: "We investigate training instability in Transformers by analyzing attention layer dynamics. Our research found that low attention entropy is accompanied by high training instability, which can take the form of oscillating loss or divergence. We propose σReparam, a technique that reparametrizes linear layers using spectral normalization plus a learned scalar to prevent entropy collapse. We provide theoretical grounding by proving that attention entropy decreases exponentially with the spectral norm of attention logits. Experimental validation spans multiple domains—vision, machine translation, speech recognition, and language modeling—demonstrating that σReparam enables competitive performance while eliminating common training requirements like warmup, weight decay, layer normalization, and adaptive optimizers."
---

[Download paper here](https://arxiv.org/abs/2303.06296)

Recommended citation:
```bibtex
@inproceedings{zhai2023sigmareparam,
  title={Stabilizing Transformer Training by Preventing Attention Entropy Collapse},
  author={Zhai, Shuangfei and Likhomanenko, Tatiana and Littwin, Etai and Busbridge, Dan and Ramapuram, Jason and Zhang, Yizhe and Gu, Jiatao and Susskind, Joshua M},
  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},
  year={2023}
}
```
