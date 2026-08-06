---
title: "What I Want to Build: Intuition, Latent Reasoning, and the AI Scientist"
date: 2026-08-05
permalink: /posts/2026/08/what-i-want-to-build/
excerpt: "The goal that ties my research together: AI with strong intuition—systems that see the answer before they argue for it, and close the loop between hypothesis and result."
tags:
  - research vision
  - intuition
  - latent reasoning
  - AI scientist
  - self-improvement
---

The goal that ties my research together is simple to state and hard to build: **AI with strong intuition**—systems that guess well *before* they reason at length, and that use reasoning to **verify** the guess rather than to substitute for it. I want to build machines that **see the answer before they argue for it**.

## Thinking out loud has a cost

People solve hard problems fast. The answer often arrives before the argument does; the write-up comes later. Today's models do the opposite: they think out loud, at length. Long chains of thought are expensive, and past a point they actively hurt—the model overthinks, contaminates its own context, and talks itself out of an answer it already had.

## Experts see first, then verify

Expertise is not deliberating for longer. It is having **better first guesses**. AlphaGo's search existed to confirm the intuition of its policy network, not to replace it: *see, then check.* I want models that can see a blurry version of the answer directly, then spend compute sharpening and verifying it—instead of paying full price for every step of a trajectory that a good intuition would have skipped.

## So what is actually missing?

Predicting the next token of human text teaches a model to **reproduce** reasoning rather than to **compress** it. And forcing every intermediate thought through a single discrete token squeezes it through a very narrow channel. Both are design choices—not laws of nature—and both can be changed.

## From reproducing knowledge to creating it

Strong intuition is, I believe, the missing ingredient for AI that **creates** knowledge instead of reproducing it: systems that form their own hypotheses, explore on their own initiative, and generalize into genuinely new territory. That is the loop I care about most—the one that turns a question into an experiment, an experiment into a result, and a result into the next question.

## How I'm building it

Five threads, one question—where does intuition come from, and how do we train it?

- **Text diffusion.** Generation that is bidirectional and global rather than left-to-right. Any-order prediction gives a model *implicit lookahead*: a form of planning that never has to be spelled out in tokens. ([DiffuCoder](https://github.com/apple/ml-diffucoder), CADD)

- **Latent reasoning.** Thinking in continuous space instead of in text. Latent thoughts are compressed, more diverse, and far cheaper than a long chain of tokens, and they sidestep the *diversity collapse* that reinforcement learning inflicts on token policies. Fewer words, more thought. ([LaDiR](https://arxiv.org/abs/2510.04573), [LaDi-RL](https://arxiv.org/abs/2602.01705), [CLaRa](https://github.com/apple/ml-clara))

- **Code, agents, and verifiers.** Code is where intuition becomes *measurable*—a good engineer predicts what a program will do before running it. I train coding models and software agents, and the verifiers and environments that let them check a hunch cheaply. ([SWE-Gym](https://github.com/SWE-Gym/SWE-Gym), CodeAct)

- **The AI scientist.** Agents that *discover* rather than retrieve: forming hypotheses, designing the experiment that would discriminate between them, running it, and being honest about the result. The target domains are the sciences, where a wrong answer is checkable. ([BED-LLM](https://arxiv.org/abs/2508.21184))

- **Recursive self-improvement.** A model that manufactures its own training signal—self-distillation, future-aware data creation, and search folded back into weights—so that yesterday's slow deliberation becomes today's instant judgment. ([SSD](https://github.com/apple/ml-ssd))

## The bet

Put together, this is one bet: the next big gains come not from thinking *longer*, but from thinking *better*—seeing first, verifying fast, and **closing the loop between hypothesis and result**. That is what I want to build.
