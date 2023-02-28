#!/usr/bin/env python3
"""Basic flask app"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """babel configuration class for flask app"""
    LANGUAGES = []
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def hello() -> str:
    """renders html page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
