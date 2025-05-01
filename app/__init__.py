from flask import Flask, render_template, abort
from dotenv import load_dotenv


# Flask app factory.
def create_app():

    # The flask app.
    app = Flask(__name__)

    # Load environment variables.
    load_dotenv()

    # The projects to be shown in the projects-page grid via a for loop
    # stored as a list of dictionaries. The slug is a unique identifier
    # for the project.
    projects = [
        {
            "name": "Microblog",
            "thumb": "images/microblog-wee.png",
            "hero": "images/microblog-hero.png",
            "categories": ["Python", "Flask", "MongoDB"],
            "slug": "microblog",
            "production": "https://sfraser-microblog-u1r8.onrender.com",
            "sourcecode": "https://github.com/sfraser-dev/python-flask-microblog",
        },
        {
            "name": "Memory Game",
            "thumb": "images/memory-wee.png",
            "hero": "images/memory-hero.png",
            "categories": ["JavaScript", "HTML", "CSS"],
            "slug": "memory-game",
            "production": "https://sfraser-memory-game.onrender.com",
            "sourcecode": "https://github.com/sfraser-dev/web-portfolio-memory-game",
        },
        {
            "name": "Dice Game",
            "thumb": "images/dice-wee.png",
            "hero": "images/dice-hero.png",
            "categories": ["JavaScript", "HTML", "CSS"],
            "slug": "dice-game",
            "production": "https://sfraser-dice-game.onrender.com",
            "sourcecode": "https://github.com/sfraser-dev/web-portfolio-dice-game",
        },
        {
            "name": "Notes Application",
            "thumb": "images/notes-wee.png",
            "hero": "images/notes-hero.png",
            "categories": ["JavaScript", "HTML", "CSS"],
            "slug": "notes-app",
            "production": "https://sfraser-notes-app.onrender.com",
            "sourcecode": "https://github.com/sfraser-dev/web-portfolio-notes-app",
        },
        {
            "name": "Drum Set",
            "thumb": "images/drum-wee.png",
            "hero": "images/drum-hero.png",
            "categories": ["JavaScript", "HTML", "CSS"],
            "slug": "drum-set",
            "production": "https://sfraser-drum-set.onrender.com",
            "sourcecode": "https://github.com/sfraser-dev/web-portfolio-drum-set",
        },
        {
            "name": "Film Database",
            "thumb": "images/film-wee.png",
            "hero": "images/film-hero.png",
            "categories": ["Python", "Pandas", "SQL"],
            "slug": "film-database",
            "production": "https://replit.com/@sfraser-dev/filmdatabase",
            "sourcecode": "https://github.com/sfraser-dev/python-jit-sqlite-pandas-film-db",
        },
    ]

    # A dictionary comprehension that iterates through the projects list, taking
    # the slug of each project as the key and the entire project dictionary as the
    # value. This creates a handy lookup table (index).
    slug_to_project = {project["slug"]: project for project in projects}

    certificates = [
        {
            "title": "Python: Online Data Analysis Course (October 2024)",
            "slug": "python-data-analysis",
            "desc": "Performing data analysis using Python.",
            "pdf": "docs/cert-fcc-python-data-analysis-sf.pdf",
            "img": "docs/cert-fcc-python-data-analysis-sf.png",
            "alt": "Data Analysis FCC certificate",
            "link": "https://www.freecodecamp.org/certification/fcc011121fa-fa04-41d9-8189-0d017cab7a94/data-analysis-with-python-v7",
            "label": "View Data Analysis certificate on freeCodeCamp",
        },
        {
            "title": "JavaScript: Online DSA Course (March 2024)",
            "slug": "javascript-dsa",
            "desc": "Implementing algorithms and data structures using JavaScript.",
            "pdf": "docs/cert-fcc-javascript-dsa-sf.pdf",
            "img": "docs/cert-fcc-javascript-dsa-sf.png",
            "alt": "JavaScript FCC certificate",
            "link": "https://www.freecodecamp.org/certification/fcc011121fa-fa04-41d9-8189-0d017cab7a94/javascript-algorithms-and-data-structures",
            "label": "View JavaScript DSA certificate on freeCodeCamp",
        },
        {
            "title": "C#: Online Microsoft Course (February 2024)",
            "slug": "csharp-microsoft",
            "desc": "Comprehensive introduction to the C# programming language with Microsoft.",
            "pdf": "docs/cert-fcc-ms-csharp-sf.pdf",
            "img": "docs/cert-fcc-ms-csharp-sf.png",
            "alt": "C# Microsoft and FCC certificate",
            "link": "https://freecodecamp.org/certification/fcc011121fa-fa04-41d9-8189-0d017cab7a94/foundational-c-sharp-with-microsoft",
            "label": "View C# certificate and exam results on freeCodeCamp",
        },
        {
            "title": "Go (Golang): Online Course (January 2024)",
            "slug": "golang-udemy",
            "desc": "Mastering the Go programming language.",
            "pdf": "docs/cert-go-grider.pdf",
            "img": "docs/cert-go-grider.png",
            "alt": "Go Udemy certificate",
            "link": "https://ude.my/UC-39842b87-9f21-4303-ad79-44a69760dd18",
            "label": "View Go certificate on Udemy",
        },
        {
            "title": "JavaScript: Online Backend Development and APIs Course (November 2023)",
            "slug": "javascript-backend-apis",
            "desc": "Creating microservices using JavaScript, Node, Express and MongoDB.",
            "pdf": "docs/cert-fcc-backend-api-sf.pdf",
            "img": "docs/cert-fcc-backend-api-sf.png",
            "alt": "API FCC certificate",
            "link": "https://freecodecamp.org/certification/fcc011121fa-fa04-41d9-8189-0d017cab7a94/back-end-development-and-apis",
            "label": "View JavaScript Backend Development and APIs certificate on freeCodeCamp",
        },
        {
            # No online version of this certificate
            "title": "Just IT Software Development Bootcamp (June 2023)",
            "slug": "justit-bootcamp",
            "desc": "In-person three-month intensive bootcamp focusing on Python, JavaScript, SQL, CSS and HTML.",
            "pdf": "docs/cert-JustIT-completion-certificate.pdf",
            "img": "docs/cert-JustIT-completion-certificate.png",
            "alt": "JustIT certificate",
            "link": "",
            "label": "",
        },
        {
            "title": "SQL: Online Course (May 2023)",
            "slug": "sql-udemy",
            "desc": "Become an expert at SQL using PostgreSQL and PgAdmin.",
            "pdf": "docs/cert-sql-portilla.pdf",
            "img": "docs/cert-sql-portilla.png",
            "alt": "SQL Udemy Certificate",
            "link": "https://ude.my/UC-ec6421c1-4784-4ba5-902d-229c7d08c2b4",
            "label": "View SQL certificate on Udemy",
        },
        {
            "title": "Python: Online Course (March 2023)",
            "slug": "python-udemy",
            "desc": "Begin with the basics of Python and progress to creating your own applications and games.",
            "pdf": "docs/cert-python-portilla.pdf",
            "img": "docs/cert-python-portilla.png",
            "alt": "Python Udemy Certificate",
            "link": "https://ude.my/UC-ac1d437e-d4f3-43ec-8b1f-27386db098b9",
            "label": "View Python certificate on Udemy",
        },
    ]

    # Projects endpoint creation.
    @app.route("/projects/")  # The route is the URL path.
    def projects_page():  # The function is the name of the endpoint.
        return render_template("projects.html", projects=projects)

    # Home endpoint creation.
    @app.route("/")
    def home_page():
        return render_template("home.html")

    # Contact endpoint creation.
    @app.route("/contact/")
    def contact_page():
        return render_template("contact.html")

    # Certificates endpoint creation.
    @app.route("/certificates/")
    def certificates_page():
        return render_template("certificates.html", certificates=certificates)

    # Project/project-name slug endpoint creations.
    # Example: <string:slug>, the variable is "slug" and it is of type "string".
    # Example, if user visits http://127.0.0.1:5500/projects/dice-game, then slug is "dice-game".
    @app.route("/projects/<string:slug>")
    def project_index(slug):
        # User has input an URL we don't recognise - give 404 error.
        if slug not in slug_to_project:
            abort(404)
        # URL is recognised so render template using the project dictionary.
        return render_template(f"project-{slug}.html", project=slug_to_project[slug])

    # Errorhandler endpoint creation. Run this when flask aborts with a 404 response.
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    # Other 400 errors if handling form data

    # Errorhandler endpoint creation. Run this when flask aborts with a 500 response.
    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("500.html"), 500

    # # A 500 endpoint to test 500 error handling (via typing of 127.0.0.1:5500/500).
    # @app.route("/500")
    # def error500():
    #     abort(500)

    # Flask app factory.
    return app
