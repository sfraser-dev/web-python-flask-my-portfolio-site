from flask import Flask, render_template
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()

projects = [
    {
        "name": "Drums",
        "thumb": "images/drum-wee.png",
        "hero": "images/drum-hero.png",
        "categories": ["HTML", "CSS", "JS"],
        "slug": "drums",
        "production": "https://www.bbc.co.uk",
    },
    {
        "name": "Dice",
        "thumb": "images/dice-wee.png",
        "hero": "images/dice-hero.png",
        "categories": ["HTML", "CSS", "JS"],
        "slug": "dice",
        "production": "https://www.bbc.co.uk",
    },
    {
        "name": "Memory",
        "thumb": "images/memory-wee.png",
        "hero": "images/memory-hero.png",
        "categories": ["HTML", "CSS", "JS"],
        "slug": "dice",
        "production": "https://www.bbc.co.uk",

    },
]


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")
