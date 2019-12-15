#Placeholder
from flask import Flask, render_template, request, redirect
from weather import Weatherapi

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('homepage.html')

@app.route('/result', methods = ['POST'])
def results():
	result = request.form['weather']
	api = Weatherapi()
	result = result.replace(' ', "%20")
	print(api.get_data(result))
	arr = api.get_data(result)
	# result will equal the string from the user in the homepage.
	print("The search was " + result + ".")
	# This will print the search into the console, 
	# then redirect back to the homepage. This can
	# be replaced with another render_template once we
	# get a results page
	return render_template('ResultTemplate.html', result_arr = arr)
