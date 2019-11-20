#Placeholder
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('homepage.html')

@app.route('/result', methods = ['POST'])
def results():
	result = request.form['weather']
	# result will equal the string from the user in the homepage.
	print("The search was " + result + ".")
	# This will print the search into the console, 
	# then redirect back to the homepage. This can
	# be replaced with another render_template once we
	# get a results page
	return redirect('/')
