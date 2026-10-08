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
from app.mailer import send_contact_email
from app.data import PROFILE, ABOUT, EDUCATION, SKILLS, PROJECTS, EXPERIENCE

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    form = ContactForm()

    if form.validate_on_submit():
        name = form.name.data.strip()
        email = form.email.data.strip()
        subject = form.subject.data.strip()
        body = form.message.data.strip()

        # Email is the reliable way to receive messages on a hosted site.
        email_sent = send_contact_email(name, email, subject, body)

        # Also keep a copy in the database (best effort).
        saved = False
        try:
            db.session.add(
                ContactMessage(name=name, email=email, subject=subject, message=body)
            )
            db.session.commit()
            saved = True
        except Exception:
            db.session.rollback()

        email_configured = bool(current_app.config.get("MAIL_USERNAME"))
        delivered = email_sent if email_configured else saved

        if delivered:
            flash("Thanks for reaching out. I will get back to you soon.", "success")
        else:
            flash("Sorry, your message could not be sent. Please email me directly.", "error")
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
