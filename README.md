
This code is a demo of how to use Django to hit an external API for the data you want to represent in a server-rendered web app.

For you, it's also a light introduction to some of the cool ways you can leverage Django's template system, form models, and class-based views.

A `requirements.txt` file is included in this repo so you can install all the python dependencies via pip.

First, Create a virtual environment and then fire it up. Then, run `pip install -r requirements.txt` to get all the goodies.

Because this app is for searching saved board game collection data from the Board Game Geek site, I assume you'll need a username for the search functionality (unless you're a game collector like I am. Then let's get together and play something after class!) Feel free to use `lucegoose100`, which is my BGG username.

`user_collection` is the app to look at for guidance on making your own template-driven application. Things to check out:

1. `forms.py`, where a very simple example of a form model resides
1. `views.py`, where I use methods in the view classes to generate the data that gets bound to the proper templates
1. The `templates` directory. Note how `index.html` is the parent template that is rendered on its own by the SearchView, but how it also is reused in `collection_list.html`, which extends `index` to carry over the header tag and the footer without having to create those elements again in the `collection_list` template.
1. `static/` is the place to put static assets like css files, images, etc. As long as that folder is called `static`, Django can find it and load those assets into any template you need. See `index.html` for how that works to make the css file available.
1. Visit https://docs.djangoproject.com/en/2.0/ref/templates/builtins/ for a ton more cool stuff you can do with Django templates and feel the power surging through your veins. Or something like that.
