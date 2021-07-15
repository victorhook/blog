---
layout: home
---

{% assign words = content | number_of_words %}

<div class="home">
  <ul>
    {% for post in site.posts limit:3 %}
      <li>
        <div class="post-preview">
          <a href="{{ post.url }}"><h3 class="post-preview-title">{{ post.title }}</h3></a>
          <p class="post-preview-body">{{ post.excerpt }}</p>
        <div class="post-preview-footer d-flex align-items-center justify-content-start">
          <span class="post-footer-item">{{ post.date | date_to_string }}</span>
          <span class="post-footer-item read-time">
            <i class="bi bi-clock"></i>
            {% include read_time.html %}
          </span>
        </div>
        </div>
      </li>
    {% endfor %}
  </ul>
</div>
