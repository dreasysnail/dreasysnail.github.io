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
</style>

You can also find my publication list from <u><a href="https://scholar.google.com/citations?user=WDVMfggAAAAJ&hl=en">my Google Scholar profile</a>.</u>

{% include base_path %}

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






