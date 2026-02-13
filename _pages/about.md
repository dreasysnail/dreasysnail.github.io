---
permalink: /
title: "Yizhe Zhang"
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
.highlight-box {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
  border-radius: 10px;
  margin: 25px 0;
  color: white;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.highlight-box a {
  color: #fff;
  text-decoration: underline;
  font-weight: bold;
}

.news-items {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin: 20px 0;
}

.news-item {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  border-left: 3px solid #52adc8;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.news-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(82, 173, 200, 0.15);
  border-left: 3px solid #667eea;
}

.news-date-badge {
  display: inline-block;
  background: #52adc8;
  color: white;
  padding: 4px 12px;
  border-radius: 15px;
  font-size: 0.85em;
  font-weight: 600;
  margin-bottom: 10px;
}

.news-item strong {
  font-size: 1.05em;
  color: #2c3e50;
  display: block;
  margin-bottom: 8px;
}

.news-item a {
  color: #52adc8;
  text-decoration: none;
  font-weight: 500;
}

.news-item a:hover {
  text-decoration: underline;
}

.section-heading {
  font-size: 1.5em;
  font-weight: 700;
  margin-top: 30px;
  margin-bottom: 15px;
  color: #52adc8;
  border-left: 4px solid #52adc8;
  padding-left: 15px;
}

.research-topics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 15px;
  margin: 20px 0;
}

.research-card {
  background: #f8f9fa;
  padding: 18px;
  border-radius: 8px;
  border-left: 3px solid #667eea;
  transition: transform 0.2s, box-shadow 0.2s;
  font-size: 0.95em;
  cursor: pointer;
}

.research-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.15);
}

.research-card-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.research-card-link:hover .research-card {
  transform: translateY(-4px);
  box-shadow: 0 6px 16px rgba(102, 126, 234, 0.25);
  border-left: 3px solid #52adc8;
}

.research-card strong {
  font-size: 1.05em;
  color: #2c3e50;
  display: block;
  margin-bottom: 5px;
}

.bio-section {
  line-height: 1.8;
  font-size: 1.05em;
}

.service-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 15px 0;
}

.badge {
  background: #e9ecef;
  padding: 5px 12px;
  border-radius: 15px;
  font-size: 0.9em;
  color: #495057;
  border: 1px solid #dee2e6;
}
</style>

## About Me

<div class="bio-section">

I am a <strong>Staff Research Scientist</strong> at <a href="https://machinelearning.apple.com">Apple MLR</a>, primarily working on <strong>Natural Language Processing</strong> and <strong>Machine Learning</strong>. Before joining Apple, I have been at <a href="https://ai.facebook.com/research/NLP/">Meta AI</a> and <a href="https://www.microsoft.com/en-us/research/group/natural-language-processing/">Microsoft Research</a>, working on natural language generation and NLP pre-training.

I received my <strong>Ph.D.</strong> and <strong>M.S.</strong> degrees from <a href="https://gradschool.duke.edu">Duke University</a>. Before that, I received my <strong>B.Sc. degree in Physics</strong> from <a href="http://dii.nju.edu.cn/kuangym/?lang=en">Nanjing University</a>, Kuang Yaming Honors School, in 2011.

</div>

---

<div class="section-heading">News</div>

<div class="news-items">
  <div class="news-item">
    <div class="news-date-badge">Feb 2026</div>
    <strong>LaDi-RL Released</strong>
    Latent reasoning + RL achieving 20.5 on AIME25 and 52.7 on LCB v6 for an 8B model with 2x faster reasoning. Surprisingly, RL for latent reasoning doesn't suffer from entropy/diversity collapse! <a href="https://arxiv.org/abs/2602.01705">Paper</a>
  </div>

  <div class="news-item">
    <div class="news-date-badge">Jan 2026</div>
    <strong>6 Papers Accepted to ICLR 2026</strong>
    Our work on diffusion-based language models continues to advance, covering masked diffusion for code generation (<a href="https://arxiv.org/abs/2506.20639">DiffuCoder</a>), latent diffusion for text reasoning (<a href="https://arxiv.org/abs/2510.04573">LaDiR</a>), few-step diffusion for long text generation (<a href="https://arxiv.org/abs/2509.20624">FS-DFM</a>), continuous augmentation for discrete diffusion (<a href="https://arxiv.org/abs/2510.01329">CADD</a>), adaptive reward shaping for efficient reasoning (<a href="https://arxiv.org/abs/2505.15612">LASER</a>), and Bayesian experimental design with LLMs (<a href="https://arxiv.org/abs/2508.21184">BED-LLM</a>).
  </div>

  <div class="news-item">
    <div class="news-date-badge">Dec 2025</div>
    <strong>CLaRa Released</strong>
    CLaRa bridges retrieval and generation with continuous latent reasoning. 1k+ GitHub stars! <a href="https://github.com/apple/ml-clara">GitHub</a> <img src="https://img.shields.io/github/stars/apple/ml-clara?style=social" alt="GitHub stars" style="vertical-align: middle; margin-left: 5px;">
  </div>

  <div class="news-item">
    <div class="news-date-badge">Jul 2025</div>
    <strong>DiffuCoder Released</strong>
    Masked diffusion for code generation with Coupled-GRPO, achieving +4.4% on EvalPlus. <a href="https://github.com/apple/ml-diffucoder">GitHub</a> <img src="https://img.shields.io/github/stars/apple/ml-diffucoder?style=social" alt="GitHub stars" style="vertical-align: middle; margin-left: 5px;">
  </div>
</div>

---

<div class="highlight-box">
<strong>Seeking Research Interns and FTE</strong><br>
Please send me an <a href="mailto:yizzhang@apple.com">email</a> with your latest CV if you are working on <strong>text diffusion, continuous token representations, coding LLMs/agent, AI scientist and lookahead training</strong> and are interested in a research internship or FTE position at Apple MLR.
</div>

---

<div class="section-heading">Research Interests</div>

My recent research focuses on **pushing LLMs to gain more intuition and strong generalization**, especially in the **code domain**:

<div class="research-topics">
  <a href="/publications/#code-llm-agents" class="research-card-link">
    <div class="research-card">
      <strong>Code LLM & Agents</strong>
      Building intelligent coding assistants and autonomous agents that understand and generate code
    </div>
  </a>

  <a href="/publications/#long-horizon-planning" class="research-card-link">
    <div class="research-card">
      <strong>Long-Horizon Planning</strong>
      Enabling LLMs to perform complex, multi-step reasoning and planning over extended sequences
    </div>
  </a>

  <a href="/publications/#rag-reasoning" class="research-card-link">
    <div class="research-card">
      <strong>RAG & Reasoning with Continuous Tokens</strong>
      Retrieval-augmented generation and reasoning systems using continuous token representations
    </div>
  </a>

  <a href="/publications/#text-diffusion" class="research-card-link">
    <div class="research-card">
      <strong>Text Diffusion Models</strong>
      Advancing non-autoregressive generation through diffusion-based approaches
    </div>
  </a>

  <a href="/publications/#coding-ai-scientist" class="research-card-link">
    <div class="research-card">
      <strong>Coding-Based AI Scientist</strong>
      Developing AI systems that can autonomously discover knowledge through code
    </div>
  </a>
</div>

---

<div class="section-heading">Academic Service</div>

**Area Chair / Senior Program Committee:**

<div class="service-badges">
  <span class="badge">ICLR 2023-2025</span>
  <span class="badge">ICML 2022-2025</span>
  <span class="badge">NeurIPS 2020-2025</span>
  <span class="badge">ACL 2020-2021</span>
  <span class="badge">EMNLP 2022</span>
  <span class="badge">NAACL 2023</span>
  <span class="badge">AAAI 2018-2021</span>
</div>

**Editorial Roles:**
- **Action Editor** for Transactions on Machine Learning Research (TMLR, since 2023)
- **Action Editor** for ACL Rolling Review (ARR, since 2023)

**Organization:**
- Organization Committee Member, ACL 2020

---

<div class="section-heading">Visitor Map</div>

<div style="text-align: center; margin: 30px 0;">
<script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=BKvwLE-wb4FnDWME9A_55wQ5wkYK4jb0k6AobZ72d5o"></script>
</div>