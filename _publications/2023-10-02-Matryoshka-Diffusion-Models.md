---
title: "Matryoshka Diffusion Models"
collection: publications
permalink: /publication/2023-10-02-Matryoshka-Diffusion-Models
date: 2023-10-02
venue: 'ICLR'
paperurl: 'https://arxiv.org/abs/2310.15111'
citation: 'Jiatao Gu, Shuangfei Zhai, <b>Yizhe Zhang</b>, Joshua M Susskind, Navdeep Jaitly'
topics: ['text-diffusion']
description: "Multi-resolution diffusion with NestedUNet achieves 1024x1024 generation with strong zero-shot generalization"
abstract: "We introduce an innovative framework for high-resolution image and video generation. Our approach proposes a diffusion process that processes inputs across multiple resolutions simultaneously, utilizing a NestedUNet architecture where smaller-scale features are embedded within larger-scale parameters. A key innovation is the progressive training approach that moves from lower to higher resolutions, substantially enhancing optimization for high-resolution outputs. The method demonstrates capabilities across diverse applications including class-conditioned image generation, high-resolution text-to-image synthesis, and text-to-video tasks. Notably, the approach enables training a single pixel-space model at resolutions up to 1024x1024 pixels, achieving strong zero-shot generalization using the CC12M dataset, which contains only 12 million images."
---

[Download paper here](https://arxiv.org/abs/2310.15111)

Recommended citation:
```bibtex
@inproceedings{gu2023matryoshka,
  title={Matryoshka Diffusion Models},
  author={Gu, Jiatao and Zhai, Shuangfei and Zhang, Yizhe and Susskind, Joshua M and Jaitly, Navdeep},
  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2023}
}
```
