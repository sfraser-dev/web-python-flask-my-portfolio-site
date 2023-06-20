from flask import Flask, render_template, abort
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    load_dotenv()

    projects = [
        {
            "name": "Drum Set",
            "thumb": "images/drum-wee.png",
            "hero": "images/drum-hero.png",
            "categories": ["HTML", "CSS", "JS"],
            "slug": "drum-set",
            "prod": "https://microblog-flask-w3css.onrender.com",
        },
        {
            "name": "Dice Game",
            "thumb": "images/dice-wee.png",
            "hero": "images/dice-hero.png",
            "categories": ["HTML", "CSS", "JS"],
            "slug": "dice-game",
            "prod": "https://microblog-flask-w3css.onrender.com",
        },
        {
            "name": "Memory Game",
            "thumb": "images/memory-wee.png",
            "hero": "images/memory-hero.png",
            "categories": ["HTML", "CSS", "JS"],
            "slug": "memory-game",
            "prod": "https://microblog-flask-w3css.onrender.com",
        },
    ]

    # dictionary comprehension
    # eg: drum-set: { drum dict syntax here }
    # eg: dice-game: { dice dict syntax here }
    # eg: memory-game: { dice dict syntax here }
    slug_to_project = {project["slug"]: project for project in projects}

    @app.route("/")
    def home():
        return render_template("home.html", projects=projects)


    @app.route("/about/")
    def about():
        return render_template("about.html")


    @app.route("/contact/")
    def contact():
        return render_template("contact.html")

    @app.route("/project/<string:slug>")
    def project(slug):
        if slug not in slug_to_project:
            abort(404)
        return render_template(f"project-{slug}.html", project=slug_to_project[slug])

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    return app      # flask app factory

# handle 500 error?
# 400 error if handling form data