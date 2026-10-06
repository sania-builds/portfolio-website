"""
run.py

Entry point for running the app locally during development.
In production, a WSGI server such as gunicorn imports create_app
directly and does not use this file.
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
