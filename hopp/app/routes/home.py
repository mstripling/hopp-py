from flask import Blueprint, render_template

# Create a Blueprint for home routes
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return "hello world" #render_template('home.html')
