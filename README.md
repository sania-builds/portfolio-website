# Sania Jameel — Portfolio Website

A personal portfolio website built with Flask, presenting education,
skills, projects, and contact information for a Computer Science
graduate.

Live site: https://sania-jameel-portfolio.vercel.apps

## Features

- Single page layout with Home, About, Education, Skills, Projects,
  Experience, and Contact sections.
- Responsive design that works on desktop, tablet, and mobile, with a
  mobile hamburger menu and active-section highlighting in the nav.
- Contact form with server side validation and CSRF protection,
  storing messages in a SQLite database.
- Custom 404 and 500 error pages.
- A small pytest test suite covering the main routes and the contact
  form.

## Technologies used

- **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-WTF
- **Frontend:** HTML5, CSS3 (no framework), vanilla JavaScript
- **Database:** SQLite (for contact form messages)
- **Testing:** pytest

## Project structure

```
portfolio/
├── app/
│   ├── __init__.py       # application factory
│   ├── routes.py         # page routes and error handlers
│   ├── models.py         # ContactMessage database model
│   ├── forms.py          # contact form definition
│   ├── data.py           # static portfolio content (edit this to update the site)
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── 404.html
│   │   └── 500.html
│   └── static/
│       ├── css/style.css
│       ├── js/script.js
│       ├── images/       # add your real photos here
│       └── files/        # your downloadable CV lives here
├── tests/
│   └── test_routes.py
├── config.py
├── run.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

1. Clone the repository and move into the project folder.
2. Create and activate a virtual environment.

   ```
   python -m venv venv
   ```

   Linux / macOS:
   ```
   source venv/bin/activate
   ```

   Windows:
   ```
   venv\Scripts\activate
   ```

3. Install the dependencies.

   ```
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and set your own `SECRET_KEY`. Any
   random string works for local development.

   ```

   cp .env.example .env
   ```

5. Run the application.

   ```
   flask --app run run
   ```

   or simply:

   ```
   python run.py
   ```

   The site will be available at `http://127.0.0.1:5000`.

## Environment variables

| Variable       | Purpose                                    |
|----------------|---------------------------------------------|
| `SECRET_KEY`   | Used by Flask and Flask-WTF for sessions and CSRF protection. |
| `DATABASE_URL` | SQLAlchemy database connection string. Defaults to a local SQLite file. |
| `FLASK_DEBUG`  | Set to `True` for local development, `False` in production. |

## Running tests

```
pytest
```

## Updating the content

All portfolio content (name, bio, education, skills, projects,
experience) lives in `app/data.py`. Edit the values there to update
the site without touching the templates. Add your real profile photo
and project screenshots to `app/static/images/`.

## Deployment

The app must run behind a production WSGI server, not Flask's
built-in development server. `gunicorn` is already included in
`requirements.txt`.

Example production start command:

```
gunicorn "app:create_app()"
```

Steps for a typical deployment (for example on Render, Railway, or
PythonAnywhere):

1. Push the repository to GitHub.
2. Create a new web service on your hosting platform and connect it
   to the repository.
3. Set the build command to `pip install -r requirements.txt`.
4. Set the start command to `gunicorn "app:create_app()"`.
5. Add the environment variables from the table above in the
   platform's dashboard. Never commit a real `.env` file to GitHub.
6. Deploy, then confirm the live URL loads correctly and `FLASK_DEBUG`
   is set to `False`.

## What could be improved in a future version

- Add an admin dashboard to manage project entries without editing
  code directly.
- Add dark and light mode.
- Add automated deployment with GitHub Actions.
- Expand the test suite to cover edge cases in form validation.
