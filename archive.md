---
layout: archive
---

<ul class="archive">
  {% for post in site.posts %}
    <li>
      <a class="archive-preview" href="{{ post.url }}">
        <div class="d-flex align-items-center justify-content-between">
            <h3>{{ post.title }}</h3>
            <h6>{{ post.date | date_to_string }} </h6>
        </div>
      </a>
    </li>
  {% endfor %}
</ul>