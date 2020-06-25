---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<div>author: {{author.googlescholar}}</div>
# {% if author.googlescholar %}  
  <!-- You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u> -->
# {% endif %}

You can also find my articles on <u><a href="https://scholar.google.com/citations?user=WDVMfggAAAAJ&hl=en">my Google Scholar profile</a>.</u>

{% include base_path %}



<h2 itemprop="headline">Preprint</h2>
{% for post in site.publications reversed %}
  {% capture month %}{{ post.date | date:"%M" }}{% endcapture %}
  {% if month == "12" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}


<h2 itemprop="headline">2020</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% if year == "2020" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2 itemprop="headline">2019</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% if year == "2019" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2 itemprop="headline">2018</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% if year == "2018" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2 itemprop="headline">2018</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% if year == "2018" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}



<h2 itemprop="headline">2017</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% if year == "2017" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2 itemprop="headline">2016</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% if year == "2016" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2 itemprop="headline">2015</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% if year == "2015" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2 itemprop="headline">2012</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% if year == "2012" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}






