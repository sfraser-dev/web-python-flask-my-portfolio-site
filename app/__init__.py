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
            "name": "Drum Set",
            "thumb": "images/drum-wee.png",
            "hero": "images/drum-hero.png",
            "categories": ["HTML", "CSS", "JS"],
            "slug": "drum-set",
            "prod": "https://sfraser-microblog.onrender.com",
        },
        {
            "name": "Dice Game",
            "thumb": "images/dice-wee.png",
            "hero": "images/dice-hero.png",
            "categories": ["HTML", "CSS", "JS"],
            "slug": "dice-game",
            "prod": "https://sfraser-microblog.onrender.com",
        },
        {
            "name": "Memory Game",
            "thumb": "images/memory-wee.png",
            "hero": "images/memory-hero.png",
            "categories": ["HTML", "CSS", "JS"],
            "slug": "memory-game",
            "prod": "https://sfraser-microblog.onrender.com",
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

    # Home endpoint. Note url_for('home') returns the route URL "/" because def is home)
    @app.route("/")
    def home():
        return render_template("home.html", projects=projects)

    # About endpoint.
    @app.route("/about/")
    def about():
        return render_template("about.html")

    # Contact endpoint.
    @app.route("/contact/")
    def contact():
        return render_template("contact.html")

    # Project/project-name slug endpoints.
    # <string:slug> is a route with a variable for the URL (variable slug as a string).
    @app.route("/project/<string:slug>")
    def project(slug):
        # User has input an URL we don't recognise - give 404 error.
        if slug not in slug_to_project:
            abort(404)
        # URL is recognised so render template using the project dictionary
        return render_template(f"project-{slug}.html", project=slug_to_project[slug])

    # Errorhandler endpoint decorator. Run this when flask aborts with a 404 response.
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    # Errorhandler endpoint decorator. Run this when flask aborts with a 500 response.
    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("500.html"), 500

    # Flask app factory.
    return app      

# handle 500 error?
# 400 errors if handling form data