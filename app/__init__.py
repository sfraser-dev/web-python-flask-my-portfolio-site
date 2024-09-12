from flask import Flask, render_template, abort
from dotenv import load_dotenv


# Flask app factory.
def create_app():

    # The flask app.
    app = Flask(__name__)

    # Load environment variables.
    load_dotenv()

    # The projects to be shown in the projects-page grid via a for loop
    # stored as a list of dictionaries.
    projects = [
        {
            "name": "Microblog",
            "thumb": "images/microblog-wee.png",
            "hero": "images/microblog-hero.png",
            "categories": ["Python", "Flask", "MongoDB"],
            "slug": "microblog",
            "production": "https://sfraser-microblog-u1r8.onrender.com",
        },
        {
            "name": "Memory Game",
            "thumb": "images/memory-wee.png",
            "hero": "images/memory-hero.png",
            "categories": ["JavaScript", "CSS", "HTML"],
            "slug": "memory-game",
            "production": "https://sfraser-memory-game.onrender.com",
        },
        {
            "name": "Dice Game",
            "thumb": "images/dice-wee.png",
            "hero": "images/dice-hero.png",
            "categories": ["JavaScript", "CSS", "HTML"],
            "slug": "dice-game",
            "production": "https://sfraser-dice-game.onrender.com",
        },
        {
            "name": "Drum Set",
            "thumb": "images/drum-wee.png",
            "hero": "images/drum-hero.png",
            "categories": ["JavaScript", "CSS", "HTML"],
            "slug": "drum-set",
            "production": "https://sfraser-drum-set.onrender.com",
        },
        {
            "name": "Film Database",
            "thumb": "images/film-wee.png",
            "hero": "images/film-hero.png",
            "categories": ["Python", "Pandas", "SQL"],
            "slug": "film-database",
            "production": "https://replit.com/@koalaTreeBear/filmdatabase",
            # "production": "https://sfraser-film-database.onrender.com",
        },
    ]

    # A dictionary comprehension that loads the project's website slug and
    # maps it to the project itself.
    slug_to_project = {project["slug"]: project for project in projects}

    # Gives a mapping of slugs to projects as a single dictionary. This is a
    # common way of "making an index" to make it easy to search for a single
    # property we're interested in. For example:
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
    # }

    # Projects endpoint creation.
    # Note url_for('projects_page') returns URL "/projects/" as def is projects_page())
    @app.route("/projects/")
    def projects_page():
        return render_template("projects.html", projects=projects)

    # Home endpoint creation.
    @app.route("/")
    def home():
        return render_template("home.html")

    # Contact endpoint creation.
    @app.route("/contact/")
    def contact():
        return render_template("contact.html")

    # Certificates endpoint creation.
    @app.route("/certificates/")
    def certificates():
        return render_template("certificates.html")

    # Project/project-name slug endpoint creations.
    # <string:slug> is a route with a variable for the URL (variable slug as a string).
    # For example: 127.0.0.1:550/projects/dice-game
    @app.route("/projects/<string:slug>")
    def project(slug):
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


# 400 errors if handling form data
