import os
from flask import Flask, render_template, send_from_directory, request, redirect
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
   return render_template('aboutPage.html', title="John Smith", url=os.getenv("URL"))

@app.route('/about')
def about():
    return render_template('aboutPage.html', title="John Smith", url=os.getenv("URL"))

@app.route('/blog')
def blog():
    return render_template('blogPage.html', title="John Smith", url=os.getenv("URL"))

@app.route('/projects')
def projects():
    return render_template('projectsPage.html', title="John Smith", url=os.getenv("URL"))
