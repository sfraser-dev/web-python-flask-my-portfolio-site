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
            "categories": ["JavaScript", "CSS", "HTML"],
            "slug": "memory-game",
            "production": "https://sfraser-memory-game.onrender.com",
            "sourcecode": "https://github.com/sfraser-dev/web-portfolio-memory-game",
        },
        {
            "name": "Dice Game",
            "thumb": "images/dice-wee.png",
            "hero": "images/dice-hero.png",
            "categories": ["JavaScript", "CSS", "HTML"],
            "slug": "dice-game",
            "production": "https://sfraser-dice-game.onrender.com",
            "sourcecode": "https://github.com/sfraser-dev/web-portfolio-dice-game",
        },
        {
            "name": "Drum Set",
            "thumb": "images/drum-wee.png",
            "hero": "images/drum-hero.png",
            "categories": ["JavaScript", "CSS", "HTML"],
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
    # value. This creates a handy lookup table (index). We can now quickly retrieve
    # the details of a project based on its slug.
    slug_to_project = {project["slug"]: project for project in projects}

    # slug_to_project is a dictionary that maps the slug (key) of a project to the
    # project (value) itself. For example:
    # {
    #   "drum-set": {
    #           "name": "Drum Set",
    #           "thumb": "images/drum-wee.png",
    #           "hero": "images/drum-hero.png",
    #           "categories": ["HTML", "CSS", "JS"],
    #           "slug": "drum-set",
    #           "prod": "https://sfraser-microblog.onrender.com",
    #   },
    #   "dice-game": {
    #           "name": "Dice Game",
    #           "thumb": "images/dice-wee.png",
    #           "hero": "images/dice-hero.png",
    #           "categories": ["HTML", "CSS", "JS"],
    #           "slug": "dice-game",
    #           "prod": "https://sfraser-microblog.onrender.com",
    #   }
    #   # etc...
    # }

    # Note the Flask function "url_for('projects_page')" will return the URL "/projects/" because:
    # - the function is "projects_page()"
    # - route is "/projects/".
    #
    # Projects endpoint creation.
    @app.route("/projects/")  # The route is the URL path.
    def projects_page():      # The function is the name of the endpoint.
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
        return render_template("certificates.html")

    # Project/project-name slug endpoint creations.
    #
    # <string:slug> is a route with a variable for the URL. The variable is "slug" and it is of type "string".
    #
    # For example, if user visits http://127.0.0.1:5500/projects/dice-game, then slug would be "dice-game".
    @app.route("/projects/<string:slug>")
    def project_index(slug):
        # User has input an URL we don't recognise - give 404 error.
        if slug not in slug_to_project:
            abort(404)
        # URL is recognised so render template using the project dictionary.
        # So if the slug is "dice-game", the dictionary for "dice-game" will be passed
        # as an argument to render_template (obtained from the slug_to_project mapping).
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
