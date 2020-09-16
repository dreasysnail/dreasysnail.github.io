---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my publication list from <u><a href="https://scholar.google.com/citations?user=WDVMfggAAAAJ&hl=en">my Google Scholar profile</a>.</u>

{% include base_path %}



<h2 itemprop="headline">Preprint</h2>
{% for post in site.publications reversed %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% capture day %}{{ post.date | date:"%d" }}{% endcapture %}
  {% if month == "12" and day == "01"%}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}


<h2 itemprop="headline">2020</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% capture day %}{{ post.date | date:"%d" }}{% endcapture %}
  {% if year == "2020" and month != "12" and day != "01" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2 itemprop="headline">2019</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% if year == "2019" and month == "10" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2 itemprop="headline">2018</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% if year == "2018" and month == "10" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2 itemprop="headline">2017</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% if year == "2017" and month == "10" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2 itemprop="headline">2016</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% if year == "2016" and month == "10" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2 itemprop="headline">2015</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% if year == "2015" and month == "10" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2 itemprop="headline">2012</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% capture month %}{{ post.date | date:"%m" }}{% endcapture %}
  {% if year == "2012" and month == "10" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}






