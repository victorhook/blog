dev:
	xdg-open http://127.0.0.1:4000/blog/
	bundle exec jekyll serve

run: dev

new:
	scripts/new_post.py

push:
	git add _posts/
	git commit -m "New post"
	git push

update:
	git add _posts/
	git commit --no-edit --amend
	git push -f
