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
        <div class="post-preview">
          <a href="{{ site.baseurl }}{{ post.url }}">
            <h3 class="post-preview-title">{{ post.title }}</h3>
          </a>
          <p class="post-preview-body">{{ post.excerpt }}</p>
          {% include post_footer.html %}
        </div>
      </li>
    {% endfor %}
  </ul>
</div>
