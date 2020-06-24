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
  {% if (post.date | default: "1900-01-01" | date: "%Y") == '2012' %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}






