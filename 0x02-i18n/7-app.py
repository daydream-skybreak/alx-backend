#!/usr/bin/env python3
"""Login in Mock"""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict
from pytz import all_timezones


class Config:
    """babel configuration class for flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """returns a user dictionary
    or None if user dictionary doesn't exist or login_as is not passed"""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """executes before everything to set flask.g.user using get_user"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """determines best match from supported languages"""
    locale = request.args.get('locale', '')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    h_locale = request.headers.get('locale')
    if h_locale in app.config['LANGUAGES']:
        return h_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone() -> str:
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        return g.user.get('timezone', '')
    try:
        pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def hello() -> str:
    """renders a html element"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
