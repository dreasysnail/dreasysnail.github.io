---
title: "POINTER: Constrained Text Generation via Insertion-based Generative Pre-training."
collection: publications
permalink: /publication/2020-09-16-POINTER:-Constrained-Text-Generation-via-Insertion-based-Generative-Pre-training
date: 2020-09-16
venue: 'EMNLP'
paperurl: 'https://arxiv.org/abs/2005.00558'
citation: '<b>Yizhe Zhang</b>, Guoyin Wang, Chunyuan Li, Zhe Gan, Chris Brockett, Bill Dolan'
description: "Non-autoregressive insertion-based generation with logarithmic time complexity and coarse-to-fine hierarchy"
abstract: "We introduce POINTER, a model designed for text generation under lexical constraints. The approach operates through progressive insertion of new tokens between existing tokens in a parallel manner, applied recursively until completion. This generates a coarse-to-fine hierarchy that enhances interpretability. We pre-train on Wikipedia and achieve state-of-the-art results on constrained generation tasks. The non-autoregressive decoding strategy produces logarithmic time complexity during inference, offering efficiency advantages over traditional methods."
---

[Download paper here](https://arxiv.org/abs/2005.00558)

Recommended citation:
```bibtex
@inproceedings{zhang2020pointer,
  title={POINTER: Constrained Text Generation via Insertion-based Generative Pre-training},
  author={Zhang, Yizhe and Wang, Guoyin and Li, Chunyuan and Gan, Zhe and Brockett, Chris and Dolan, Bill},
  booktitle={Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  year={2020}
}
```