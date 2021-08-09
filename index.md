---
layout: base
---

<div id="computer">
  <p id="computer-text">
  ASD
  </p>
</div>

<div class="home">
  <ul>
    {% for post in site.posts limit:site.front_page_posts %}
      <li>
        <div class="post-preview">
          <a href="{{ post.url }}">
            <h3 class="post-preview-title">{{ post.title }}</h3>
          </a>
          <p class="post-preview-body">{{ post.excerpt }}</p>
          {% include post_footer.html %}
        </div>
      </li>
    {% endfor %}
  </ul>
</div>
