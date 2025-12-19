---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<style>
.pub-year-section {
  margin: 40px 0;
}

.year-title {
  font-size: 1.8em;
  font-weight: 700;
  color: #52adc8;
  border-left: 5px solid #52adc8;
  padding-left: 15px;
  margin-bottom: 20px;
}

.preprint-title {
  font-size: 1.8em;
  font-weight: 700;
  color: #667eea;
  border-left: 5px solid #667eea;
  padding-left: 15px;
  margin-bottom: 20px;
}

/* Topic section styles */
.topic-section {
  margin: 50px 0;
  scroll-margin-top: 80px;
}

.topic-title {
  font-size: 2em;
  font-weight: 700;
  color: #667eea;
  border-left: 5px solid #667eea;
  padding-left: 15px;
  margin-bottom: 25px;
  scroll-margin-top: 80px;
}

.topic-description {
  font-size: 1.1em;
  color: #666;
  margin-bottom: 20px;
  padding-left: 20px;
  font-style: italic;
}

.pub-description {
  font-size: 0.95em;
  color: #555;
  margin-top: 5px;
  padding-left: 5px;
  line-height: 1.5;
}

.all-publications-section {
  margin-top: 60px;
  padding-top: 40px;
  border-top: 3px solid #e0e0e0;
}

/* Quick navigation */
.topic-nav {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  margin: 30px 0;
  border-left: 4px solid #667eea;
}

.topic-nav h3 {
  margin-top: 0;
  color: #2c3e50;
  font-size: 1.2em;
}

.topic-nav-links {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 15px;
}

.topic-nav-link {
  background: white;
  padding: 8px 16px;
  border-radius: 20px;
  border: 2px solid #667eea;
  color: #667eea;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.2s;
}

.topic-nav-link:hover {
  background: #667eea;
  color: white;
}
</style>

You can also find my publication list from <u><a href="https://scholar.google.com/citations?user=WDVMfggAAAAJ&hl=en">my Google Scholar profile</a>.</u>

{% include base_path %}

<!-- Quick Navigation -->
<div class="topic-nav">
  <h3>Jump to Research Topics:</h3>
  <div class="topic-nav-links">
    <a href="#code-llm-agents" class="topic-nav-link">Code LLM & Agents</a>
    <a href="#long-horizon-planning" class="topic-nav-link">Long-Horizon Planning</a>
    <a href="#rag-reasoning" class="topic-nav-link">RAG & Reasoning</a>
    <a href="#text-diffusion" class="topic-nav-link">Text Diffusion</a>
    <a href="#coding-ai-scientist" class="topic-nav-link">AI Scientist</a>
    <a href="#all-publications" class="topic-nav-link">All Publications</a>
  </div>
</div>

<!-- 1. Code LLM & Agents -->
<div class="topic-section" id="code-llm-agents">
  <h2 class="topic-title">Code LLM & Agents</h2>
  <div class="topic-description">
    Building intelligent coding assistants and autonomous agents that understand and generate code
  </div>
  {% assign code_pubs = site.publications | where_exp: "pub", "pub.topics contains 'code-llm-agents'" | sort: "date" | reverse %}
  {% for post in code_pubs %}
    {% include archive-single.html %}
    {% if post.description %}
    <div class="pub-description">{{ post.description }}</div>
    {% endif %}
  {% endfor %}
</div>

<!-- 2. Long-Horizon Planning -->
<div class="topic-section" id="long-horizon-planning">
  <h2 class="topic-title">Long-Horizon Planning</h2>
  <div class="topic-description">
    Enabling LLMs to perform complex, multi-step reasoning and planning over extended sequences
  </div>
  {% assign planning_pubs = site.publications | where_exp: "pub", "pub.topics contains 'long-horizon-planning'" | sort: "date" | reverse %}
  {% for post in planning_pubs %}
    {% include archive-single.html %}
    {% if post.description %}
    <div class="pub-description">{{ post.description }}</div>
    {% endif %}
  {% endfor %}
</div>

<!-- 3. RAG & Reasoning with Continuous Tokens -->
<div class="topic-section" id="rag-reasoning">
  <h2 class="topic-title">RAG & Reasoning with Continuous Tokens</h2>
  <div class="topic-description">
    Retrieval-augmented generation and reasoning systems using continuous token representations
  </div>
  {% assign rag_pubs = site.publications | where_exp: "pub", "pub.topics contains 'rag-reasoning'" | sort: "date" | reverse %}
  {% for post in rag_pubs %}
    {% include archive-single.html %}
    {% if post.description %}
    <div class="pub-description">{{ post.description }}</div>
    {% endif %}
  {% endfor %}
</div>

<!-- 4. Text Diffusion Models -->
<div class="topic-section" id="text-diffusion">
  <h2 class="topic-title">Text Diffusion Models</h2>
  <div class="topic-description">
    Advancing non-autoregressive generation through diffusion-based approaches
  </div>
  {% assign diffusion_pubs = site.publications | where_exp: "pub", "pub.topics contains 'text-diffusion'" | sort: "date" | reverse %}
  {% for post in diffusion_pubs %}
    {% include archive-single.html %}
    {% if post.description %}
    <div class="pub-description">{{ post.description }}</div>
    {% endif %}
  {% endfor %}
</div>

<!-- 5. Coding-Based AI Scientist -->
<div class="topic-section" id="coding-ai-scientist">
  <h2 class="topic-title">Coding-Based AI Scientist</h2>
  <div class="topic-description">
    Developing AI systems that can autonomously discover knowledge through code
  </div>
  {% assign scientist_pubs = site.publications | where_exp: "pub", "pub.topics contains 'coding-ai-scientist'" | sort: "date" | reverse %}
  {% for post in scientist_pubs %}
    {% include archive-single.html %}
    {% if post.description %}
    <div class="pub-description">{{ post.description }}</div>
    {% endif %}
  {% endfor %}
</div>

<!-- All Publications (Chronological) -->
<div class="all-publications-section" id="all-publications">
  <h2 class="topic-title" style="color: #52adc8; border-left-color: #52adc8;">All Publications (Chronological)</h2>
</div>

<div class="pub-year-section">
<h2 class="preprint-title">Preprint</h2>
{% for post in site.publications reversed %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% capture day %}{{ post.date | date:"%d" }}{% endcapture %}
  {% if month == "12" and day == "01"%}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}
</div>

<div class="pub-year-section">
<h2 class="year-title">2025</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% capture day %}{{ post.date | date:"%d" }}{% endcapture %}
  {% if year == "2025" and month != "12" and day != "01" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}
</div>

<div class="pub-year-section">
<h2 class="year-title">2024</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% capture day %}{{ post.date | date:"%d" }}{% endcapture %}
  {% if year == "2024" and month != "12" and day != "01" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}
</div>

<div class="pub-year-section">
<h2 class="year-title">2023</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% capture day %}{{ post.date | date:"%d" }}{% endcapture %}
  {% if year == "2023" and month != "12" and day != "01" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}
</div>

<div class="pub-year-section">
<h2 class="year-title">2022</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% capture day %}{{ post.date | date:"%d" }}{% endcapture %}
  {% if year == "2022" and month != "12" and day != "01" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}
</div>

<div class="pub-year-section">
<h2 class="year-title">2021</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% capture day %}{{ post.date | date:"%d" }}{% endcapture %}
  {% if year == "2021" and month != "12" and day != "01" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}
</div>

<div class="pub-year-section">
<h2 class="year-title">2020</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% capture day %}{{ post.date | date:"%d" }}{% endcapture %}
  {% if year == "2020" and month != "12" and day != "01" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}
</div>

<div class="pub-year-section">
<h2 class="year-title">2019</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% if year == "2019" and month == "10" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}
</div>

<div class="pub-year-section">
<h2 class="year-title">2018</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% if year == "2018" and month == "10" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}
</div>

<div class="pub-year-section">
<h2 class="year-title">2017</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% if year == "2017" and month == "10" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}
</div>

<div class="pub-year-section">
<h2 class="year-title">2016</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% if year == "2016" and month == "10" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}
</div>

<div class="pub-year-section">
<h2 class="year-title">2015</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% if year == "2015" and month == "10" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}
</div>

<div class="pub-year-section">
<h2 class="year-title">2012</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% if year == "2012" and month == "10" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}
</div>






