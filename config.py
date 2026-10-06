"""
config.py

Application configuration loaded from environment variables.
Keeping this separate from app code means secrets never live in source
control and the same code can run in development or production.
"""

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-change-me")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(basedir, "portfolio.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = True

    DEBUG = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
