---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<h2 itemprop="headline">2012</h2>
{% for post in site.publications reversed %}
  {% capture year %}{{ post.date | date:"%Y" }}{% endcapture %}
  {% if year == "2012" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}






