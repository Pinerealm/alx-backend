#!/usr/bin/env python3
"""Use user locale"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configures Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as: int) -> Union[dict, None]:
    """Get user from mock db"""
    if login_as in users:
        return users[login_as]
    return None


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Get locale from request or header"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    elif g.user:
        if g.user['locale'] in app.config['LANGUAGES']:
            return g.user['locale']
    elif request.headers.get('locale'):
        return request.headers.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request() -> None:
    """Find user and set as global on flask.g.user"""
    user_id = request.args.get('login_as')
    if user_id:
        user = get_user(int(user_id))
        g.user = user if user else None
    else:
        g.user = None


@app.route('/', strict_slashes=False)
def index() -> str:
    """Render the index page"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
