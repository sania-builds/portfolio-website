"""
routes.py

All page routes for the portfolio. There is one main page (the
single page portfolio itself) plus the contact form submission
endpoint and the error handlers.
"""

from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from app import db
from app.forms import ContactForm
from app.models import ContactMessage
from app.data import PROFILE, ABOUT, EDUCATION, SKILLS, PROJECTS, EXPERIENCE

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    form = ContactForm()

    if form.validate_on_submit():
        message = ContactMessage(
            name=form.name.data.strip(),
            email=form.email.data.strip(),
            subject=form.subject.data.strip(),
            message=form.message.data.strip(),
        )
        db.session.add(message)
        db.session.commit()
        flash("Thanks for reaching out. I will get back to you soon.", "success")
        return redirect(url_for("main.index") + "#contact")

    return render_template(
        "index.html",
        profile=PROFILE,
        about=ABOUT,
        education=EDUCATION,
        skills=SKILLS,
        projects=PROJECTS,
        experience=EXPERIENCE,
        form=form,
    )


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return render_template("404.html", profile=PROFILE), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template("500.html", profile=PROFILE), 500
