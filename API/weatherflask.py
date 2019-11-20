from flask import Flask, render_template 
from flask_wtf import FlaskForm

app = Flask(__name__)


@app.route('/')
def home():
 return render_template('homepage.html') 
