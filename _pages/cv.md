---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

<style>
.cv-section {
  margin: 40px 0;
}

.section-title {
  font-size: 1.8em;
  font-weight: 700;
  margin-bottom: 20px;
  color: #52adc8;
  border-left: 5px solid #52adc8;
  padding-left: 15px;
}

.timeline-item {
  position: relative;
  padding-left: 30px;
  margin-bottom: 30px;
  border-left: 2px solid #e0e0e0;
}

.timeline-item:before {
  content: '';
  position: absolute;
  left: -6px;
  top: 0;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #667eea;
  border: 2px solid #fff;
  box-shadow: 0 0 0 2px #667eea;
}

.timeline-date {
  font-size: 0.9em;
  color: #666;
  font-weight: 600;
  margin-bottom: 5px;
}

.timeline-position {
  font-size: 1.2em;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 5px;
}

.timeline-org {
  font-size: 1.05em;
  color: #52adc8;
  font-weight: 600;
  margin-bottom: 8px;
}

.timeline-manager {
  font-size: 0.95em;
  color: #666;
  font-style: italic;
  margin-bottom: 8px;
}

.timeline-desc {
  font-size: 0.95em;
  line-height: 1.6;
  color: #555;
}

.education-item {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 15px;
  border-left: 4px solid #667eea;
}

.education-degree {
  font-size: 1.15em;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 5px;
}

.education-school {
  font-size: 1.05em;
  color: #52adc8;
  font-weight: 600;
  margin-bottom: 5px;
}

.education-date {
  font-size: 0.9em;
  color: #666;
}

.education-advisor {
  font-size: 0.95em;
  color: #666;
  font-style: italic;
  margin-top: 5px;
}

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

.research-interests {
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

.service-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin: 20px 0;
}

.service-card {
  background: #f8f9fa;
  padding: 15px;
  border-radius: 8px;
  border-top: 3px solid #52adc8;
}

.service-card h4 {
  color: #2c3e50;
  margin-bottom: 10px;
  font-size: 1.1em;
}

.service-card ul {
  margin: 0;
  padding-left: 20px;
}

.service-card li {
  font-size: 0.95em;
  margin-bottom: 5px;
}

.awards-list {
  list-style: none;
  padding: 0;
}

.awards-list li {
  background: #f8f9fa;
  padding: 12px 15px;
  margin-bottom: 10px;
  border-radius: 6px;
  border-left: 3px solid #ffc107;
  font-size: 0.95em;
}

.talks-list {
  list-style: none;
  padding: 0;
}

.talks-list li {
  background: #f8f9fa;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 8px;
  border-left: 3px solid #667eea;
}

.talk-date {
  font-size: 0.9em;
  color: #666;
  font-weight: 600;
  margin-bottom: 5px;
}

.talk-title {
  font-size: 1.1em;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 8px;
}

.talk-venue {
  font-size: 0.95em;
  color: #555;
}

.skills-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin: 20px 0;
}

.skill-badge {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.95em;
  font-weight: 600;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.selected-pubs {
  margin: 20px 0;
}

.pub-item {
  background: #f8f9fa;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 8px;
  border-left: 3px solid #52adc8;
  font-size: 0.95em;
  line-height: 1.6;
}

.pub-item strong {
  color: #2c3e50;
}

.pub-venue {
  color: #667eea;
  font-weight: 600;
}

@media (max-width: 768px) {
  .research-interests, .service-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="highlight-box">
  <strong>Download Full CV:</strong> <a href="/files/cv_yizhezhang.pdf">Available in PDF format</a>
</div>

---

## Research Interests

<div class="research-interests">
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
      <strong>RAG & Reasoning</strong>
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

<div class="cv-section">
  <div class="section-title">Professional Experience</div>

  <div class="timeline-item">
    <div class="timeline-date">May 2022 – Present</div>
    <div class="timeline-position">Staff Research Scientist</div>
    <div class="timeline-org">Apple MLR, Cupertino, CA</div>
    <div class="timeline-manager">Manager: Navdeep Jaitly</div>
    <div class="timeline-desc">
      Using code domain as a testbed for planning and reasoning. Recent work includes DiffuCoder (diffusion-based code generation) and SWE-Agent (autonomous code agents).
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">September 2021 – May 2022</div>
    <div class="timeline-position">Research Scientist</div>
    <div class="timeline-org">Facebook AI (Meta AI), Menlo Park, CA</div>
    <div class="timeline-manager">Manager: Yashar Mehdad</div>
    <div class="timeline-desc">
      Worked on retrieval-augmented generation (RAG) and summarization systems.
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">February 2018 – September 2021</div>
    <div class="timeline-position">Senior Researcher</div>
    <div class="timeline-org">Microsoft Research, Redmond, WA</div>
    <div class="timeline-manager">Manager: Bill Dolan</div>
    <div class="timeline-desc">
      Worked on generative dialogue models. Created DialoGPT, an open-sourced pretrained chat model.
    </div>
  </div>
</div>

---
<!-- 
<div class="cv-section">
  <div class="section-title">Education</div>

  <div class="education-item">
    <div class="education-degree">Ph.D. in Computational Biology</div>
    <div class="education-school">Duke University, Durham, NC</div>
    <div class="education-date">August 2013 – February 2018</div>
    <div class="education-advisor">Advisor: Lawrence Carin</div>
    <div class="timeline-desc" style="margin-top: 8px;">
      Dissertation: "Efficient and Scalable Markov Chain Monte Carlo Methods"<br>
      Focus: VAE, GAN, MCMC for text generation
    </div>
  </div>

  <div class="education-item">
    <div class="education-degree">M.Sc. in Statistics</div>
    <div class="education-school">Duke University, Durham, NC</div>
    <div class="education-date">August 2015 – February 2018</div>
  </div>

  <div class="education-item">
    <div class="education-degree">B.Sc. in Physics</div>
    <div class="education-school">Nanjing University, Nanjing, China</div>
    <div class="education-date">August 2007 – June 2011</div>
    <div class="timeline-desc" style="margin-top: 8px;">
      Kuang Yaming Honors School
    </div>
  </div>
</div> -->



<div class="cv-section">
  <div class="section-title">Recent Talks</div>

  <ul class="talks-list">
    <li>
      <div class="talk-date">October 2025</div>
      <div class="talk-title">Towards Understanding and Building Intuition for Language Model</div>
      <div class="talk-venue">
        • University of Pennsylvania, Guest lecturer<br>
        • BAIR NLP workshop, UC Berkeley, Invited speaker<br>
        • University of Washington, NLP seminar, Invited speaker
      </div>
    </li>
    <li>
      <div class="talk-date">July 2025</div>
      <div class="talk-title">Bidirectional Language Model</div>
      <div class="talk-venue">Apple Natural Language Understanding workshop, Invited speaker</div>
    </li>
  </ul>
</div>

---

<div class="cv-section">
  <div class="section-title">Selected Preprints</div>

  <div class="selected-pubs">
    <div class="pub-item">
      <strong>Jie He, Richard He Bai, Sinead Williamson, Jeff Z. Pan, Navdeep Jaitly, Yizhe Zhang.</strong>
      CLaRa: Bridging Retrieval and Generation with Continuous Latent Reasoning.
      <span class="pub-venue">arXiv (2025)</span>
      [<a href="https://arxiv.org/abs/2511.18659">paper</a>]
    </div>

    <div class="pub-item">
      <strong>Haoqiang Kang, Yizhe Zhang, Nikki Lijing Kuang, Nicklas Majamaki, Navdeep Jaitly, Yi-An Ma, Lianhui Qin.</strong>
      LaDiR: Latent Diffusion Enhances LLMs for Text Reasoning.
      <span class="pub-venue">arXiv (2025)</span>
      [<a href="https://arxiv.org/abs/2510.04573">paper</a>]
    </div>

    <div class="pub-item">
      <strong>Huangjie Zheng, Shansan Gong, Ruixiang Zhang, Tianrong Chen, Jiatao Gu, Mingyuan Zhou, Navdeep Jaitly, Yizhe Zhang.</strong>
      Continuously Augmented Discrete Diffusion Model for Categorical Generative Modeling.
      <span class="pub-venue">arXiv (2025)</span>
    </div>

    <div class="pub-item">
      <strong>Amin Karimi Monse, Nikhil Bhendawade, Manuel Rafael Ciosici, Dominic Culver, Yizhe Zhang, Irina Belousova.</strong>
      FS-DFM: Fast and Accurate Long Text Generation with Few-Step Diffusion Language Models.
      <span class="pub-venue">arXiv (2025)</span>
    </div>

    <div class="pub-item">
      <strong>Shansan Gong, Ruixiang Zhang, Huangjie Zheng, Jiatao Gu, Navdeep Jaitly, Lingpeng Kong, Yizhe Zhang.</strong>
      DiffuCoder: Understanding and Improving Masked Diffusion Models for Code Generation.
      <span class="pub-venue">arXiv (2025)</span>
      [<a href="https://arxiv.org/abs/2506.20639">paper</a>]
    </div>

    <div class="pub-item">
      <strong>Wei Liu, Ruochen Zhou, Yiyun Deng, Yuzhen Huang, Junteng Liu, Yuntian Deng, Yizhe Zhang, Junxian He.</strong>
      Learn to Reason Efficiently with Adaptive Length based Reward Shaping.
      <span class="pub-venue">arXiv (2025)</span>
    </div>

    <div class="pub-item">
      <strong>Deepro Choudhury, Sinead Williamson, Adam Goliński, Ning Miao, Freddie Bickford Smith, Michael Kirchhof, Yizhe Zhang, Tom Rainforth.</strong>
      BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design.
      <span class="pub-venue">arXiv (2025)</span>
    </div>

    <div class="pub-item">
      <strong>Yizhe Zhang, Richard Bai, Zijin Gu, Ruixiang Zhang, Jiatao Gu, Emmanuel Abbe, Samy Bengio, Navdeep Jaitly.</strong>
      What makes the preferred thinking direction for LLM in Multi-choice Questions?
      <span class="pub-venue">arXiv (2025)</span>
    </div>

    <div class="pub-item">
      <strong>Xiaogeng Liu, Zhiyuan Yu, Yizhe Zhang, Ning Zhang, Chaowei Xiao.</strong>
      Automatic and Universal Prompt Injection Attacks Against Large Language Models.
      <span class="pub-venue">arXiv (2024)</span>
    </div>
  </div>
</div>

---

<div class="cv-section">
  <div class="section-title">Professional Services</div>

  <div class="service-grid">
    <div class="service-card">
      <h4>Area Chair / Senior PC</h4>
      <ul>
        <li>NeurIPS (since 2020)</li>
        <li>ICML (since 2022)</li>
        <li>ICLR (since 2023)</li>
        <li>ACL (2020-2021)</li>
        <li>EMNLP (2022)</li>
        <li>NAACL (2023)</li>
        <li>AAAI (2018-2021)</li>
      </ul>
    </div>

    <div class="service-card">
      <h4>Editorial Roles</h4>
      <ul>
        <li>Action Editor, TMLR (since 2023)</li>
        <li>Action Editor, ARR (since 2023)</li>
      </ul>
    </div>

    <div class="service-card">
      <h4>Organization</h4>
      <ul>
        <li>Organization Committee Member, ACL 2020</li>
      </ul>
    </div>

    <div class="service-card">
      <h4>Reviewer</h4>
      <ul>
        <li>NeurIPS, ICML, ICLR</li>
        <li>ACL, EMNLP, NAACL</li>
        <li>AISTATS, AAAI</li>
      </ul>
    </div>
  </div>
</div>

---

<div class="cv-section">
  <div class="section-title">Awards & Honors</div>

  <ul class="awards-list">
    <li>Stanford Top 2% Scientists (since 2023)</li>
    <li>NeurIPS Top 5% Reviewer Award (2018)</li>
    <li>Department Fellowship, Duke University (2013-2014)</li>
    <li>National Excellent Graduate Scholarship - Top 1% (2012)</li>
    <li>Travel Awards: NeurIPS (2015, 2016), ICML (2017), ICDM (2016), IJCAI (2016), AAAI (2016)</li>
  </ul>
</div>

---

<div class="cv-section">
  <div class="section-title">Teaching Experience</div>

  <div class="education-item">
    <div class="education-degree">Advanced Machine Learning (STA571)</div>
    <div class="education-school">Duke University</div>
    <div class="timeline-desc" style="margin-top: 8px;">Instructor: Katherine Heller</div>
  </div>

  <div class="education-item">
    <div class="education-degree">Probabilistic Machine Learning (CS571)</div>
    <div class="education-school">Duke University</div>
    <div class="timeline-desc" style="margin-top: 8px;">Instructor: Cynthia Rudin</div>
  </div>
</div>

---

<div class="cv-section">
  <div class="section-title">Technical Skills</div>

  <div class="skills-container">
    <span class="skill-badge">PyTorch</span>
    <span class="skill-badge">TensorFlow</span>
    <span class="skill-badge">Python</span>
    <span class="skill-badge">C/C++</span>
    <span class="skill-badge">Java</span>
    <span class="skill-badge">Lua</span>
    <span class="skill-badge">MATLAB</span>
    <span class="skill-badge">R</span>
  </div>
</div>
