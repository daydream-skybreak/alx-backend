#!/usr/bin/env python3
"""Basic flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """babel configuration class for flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """determines best match from supported languages"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def hello() -> str:
    """renders a html element"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
