---
layout: base
---

<div class="home d-flex flex-column">

  <div id="computer">
    <p id="computer-text">
      {% for post in site.posts limit:1 %}
        Latest post: {{ post.date | date_to_string }}
      {% endfor %}
    </p>
  </div>

  <ul class="front-list">
    {% for post in site.posts limit:site.front_page_posts %}
      <li>
        <a href="{{ site.baseurl }}{{ post.url }}">
        <div class="post-preview">
            <h3 class="post-preview-title">{{ post.title }}</h3>
          {% if post.image %}
          <img class="preview-image" src="{{site.static_url}}images/{{post.image}}" alt="{{ post.title }} image}">
          {% endif %}
          <p class="post-preview-body">{{ post.content | strip_html | truncatewords: 50 }}</p>
          {% include post_footer.html %}
        </div>
        </a>
      </li>
    {% endfor %}
  </ul>
</div>
