---
layout: page
title: archive
---

<link href="{{ site.static_url }}css/archive.css" rel="stylesheet">


<ul class="archive" id="archive-list">
  {% for post in site.posts %}
    <li class="archive-post d-flex align-items-center justify-content-between">
      <a class="archive-preview" href="{{ site.baseurl }}{{ post.url }}">
        <div class="archive-post-data">
          {{ post.title }}
          <div>
          <span class="post-footer-item">{% include post_footer.html %}</span>
          </div>
        </div>
      </a>
      {% if forloop.last == false %}
        <span class="chain"></span>
      {% endif %}
    </li>
  {% endfor %}
</ul>

<script>
  console.log(document.getElementById('archive-list').children)
</script>