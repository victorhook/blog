---
layout: page
title: archive
---

<link href="{{ site.static_url }}css/archive.css" rel="stylesheet">


<ul class="archive">
  {% for post in site.posts %}
    <li class="archive-post d-flex align-items-center justify-content-between">
      <a class="archive-preview" href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
        <div>
        <span class="post-footer-item">{% include post_footer.html %}</span>
        </div>
    </li>
  {% endfor %}
</ul>