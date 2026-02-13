---
title: "LaDiR: Latent Diffusion Enhances LLMs for Text Reasoning"
collection: publications
permalink: /publication/2025-12-02-LaDiR-Latent-Diffusion-Enhances-LLMs
date: 2026-10-01
venue: 'ICLR 2026'
paperurl: 'https://arxiv.org/abs/2510.04573'
citation: 'Haoqiang Kang, <b>Yizhe Zhang</b>, Nikki Lijing Kuang, Nicklas Majamaki, Navdeep Jaitly, Yi-An Ma, Lianhui Qin'
topics: ['rag-reasoning', 'text-diffusion']
description: "Latent diffusion with VAE for iterative refinement and diverse reasoning trajectories"
abstract: "Large Language Models (LLMs) demonstrate reasoning through chain-of-thought (CoT) generation. However, LLM's autoregressive decoding may limit the ability to revisit and refine earlier tokens holistically, leading to inefficient exploration for diverse solutions. We propose LaDiR, combining a Variational Autoencoder and latent diffusion model to create iterative refinement capabilities for reasoning. It encodes reasoning steps into thought tokens and uses blockwise bidirectional attention for parallel generation of diverse reasoning trajectories, showing improvements in accuracy, diversity, and interpretability across mathematical reasoning and planning benchmarks."
---

[Download paper here](https://arxiv.org/abs/2510.04573)

Recommended citation:
```bibtex
@article{kang2025ladir,
  title={LaDiR: Latent Diffusion Enhances LLMs for Text Reasoning},
  author={Kang, Haoqiang and Zhang, Yizhe and Kuang, Nikki Lijing and Majamaki, Nicklas and Jaitly, Navdeep and Ma, Yi-An and Qin, Lianhui},
  journal={arXiv preprint arXiv:2510.04573},
  year={2025}
}
```
