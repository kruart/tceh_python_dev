# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

import logging

import course10_flask.flask_examples.with_templates.config
from course10_flask.flask_examples.with_templates.forms import BlogPostForm
from course10_flask.flask_examples.with_templates.models import Storage, BlogPostModel


logger = logging.getLogger(__name__)

__author__ = 'sobolevn'

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)


@app.route('/', methods=['GET', 'POST'])
def home():
    storage = Storage()
    all_items = storage.items

    if request.method == 'POST':
        form = BlogPostForm(request.form)
        if form.validate():
            model = BlogPostModel(form.data)
            all_items.append(model)
        else:
            logger.error('Someone have submitted an incorrect form!')
    else:
        form = BlogPostForm()

    return render_template(
        'home.html',
        form=form,
        items=all_items,
    )


if __name__ == '__main__':
    app.run()
