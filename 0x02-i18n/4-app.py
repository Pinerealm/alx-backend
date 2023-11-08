#!/usr/bin/env python3
"""Force locale with URL parameter"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Get locale from request or header"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """Render the index page"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
