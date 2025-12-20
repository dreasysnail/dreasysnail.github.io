---
title: "Kaleido Diffusion: Improving Conditional Diffusion Models with Autoregressive Latent Modeling"
collection: publications
permalink: /publication/2024-10-06-Kaleido-Diffusion
date: 2024-10-06
venue: 'NeurIPS'
paperurl: 'https://arxiv.org/abs/2405.21048'
citation: 'Jiatao Gu, Ying Shen, Shuangfei Zhai, <b>Yizhe Zhang</b>, Navdeep Jaitly, Joshua M. Susskind'
topics: ['text-diffusion']
description: "Integrates autoregressive language model to generate enriched conditioning signals for diverse image generation"
abstract: "We introduce Kaleido, a method for enhancing image generation diversity in conditional diffusion models. Diffusion models often exhibit limited diversity in the sampled images, particularly when sampling with a high classifier-free guidance weight. Our solution integrates an autoregressive language model that processes captions and generates intermediate latent representations—including textual descriptions, bounding boxes, object blobs, and visual tokens. These diverse latent variables serve as enriched conditioning signals for the diffusion process. Our experimental findings demonstrate that Kaleido successfully increases the variety of generated images while preserving quality and maintaining fidelity to the generated latent guidance signals, thereby enabling improved control over image generation outcomes."
---

[Download paper here](https://arxiv.org/abs/2405.21048)

Recommended citation:
```bibtex
@inproceedings{gu2024kaleido,
  title={Kaleido Diffusion: Improving Conditional Diffusion Models with Autoregressive Latent Modeling},
  author={Gu, Jiatao and Shen, Ying and Zhai, Shuangfei and Zhang, Yizhe and Jaitly, Navdeep and Susskind, Joshua M},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2024}
}
```
