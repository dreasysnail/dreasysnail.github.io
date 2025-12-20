---
title: "DART: Denoising Autoregressive Transformer for Scalable Text-to-Image Generation"
collection: publications
permalink: /publication/2024-10-02-DART-Denoising-Autoregressive-Transformer
date: 2024-10-02
venue: 'ICLR'
paperurl: 'https://arxiv.org/abs/2410.08159'
citation: 'Jiatao Gu, Yuyang Wang, <b>Yizhe Zhang</b>, Qihang Zhang, Dinghuai Zhang, Navdeep Jaitly, Josh Susskind, Shuangfei Zhai'
topics: ['text-diffusion']
description: "Unifies autoregressive and diffusion in non-Markovian framework for scalable text-to-image generation"
abstract: "We introduce DART, a transformer-based approach for text-to-image generation that unifies autoregressive (AR) and diffusion within a non-Markovian framework, allowing it to iteratively denoise image patches using an architecture similar to standard language models. Unlike traditional diffusion models limited by their Markovian property, DART overcomes this constraint without requiring image quantization, enabling more effective image modeling. The model handles both text and image data in a single unified architecture through unified training. DART demonstrates competitive performance on class-conditioned and text-to-image tasks, providing a scalable, efficient alternative to traditional diffusion models that establishes a new benchmark for scalable, high-quality image synthesis."
---

[Download paper here](https://arxiv.org/abs/2410.08159)

Recommended citation:
```bibtex
@inproceedings{gu2024dart,
  title={DART: Denoising Autoregressive Transformer for Scalable Text-to-Image Generation},
  author={Gu, Jiatao and Wang, Yuyang and Zhang, Yizhe and Zhang, Qihang and Zhang, Dinghuai and Jaitly, Navdeep and Susskind, Josh and Zhai, Shuangfei},
  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2024}
}
```
