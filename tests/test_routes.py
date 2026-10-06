"""
test_routes.py

A small set of tests covering the most important routes and
behaviour: the homepage loading, the 404 page, and contact form
validation.
"""

import pytest
from app import create_app, db
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False


@pytest.fixture
def client():
    app = create_app(TestConfig)
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_homepage_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Sania Jameel" in response.data


def test_navigation_links_present(client):
    response = client.get("/")
    for anchor in ["#about", "#education", "#skills", "#projects", "#experience", "#contact"]:
        assert anchor.encode() in response.data


def test_404_page(client):
    response = client.get("/this-page-does-not-exist")
    assert response.status_code == 404
    assert b"doesn" in response.data.lower() or b"404" in response.data


def test_contact_form_rejects_empty_submission(client):
    response = client.post("/", data={}, follow_redirects=True)
    assert response.status_code == 200
    assert b"This field is required" in response.data


def test_contact_form_accepts_valid_submission(client):
    response = client.post(
        "/",
        data={
            "name": "Test User",
            "email": "test@example.com",
            "subject": "Hello",
            "message": "This is a valid test message.",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Thanks for reaching out" in response.data
