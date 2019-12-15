from flask import Flask, request, render_template 
from flask_wtf import FlaskForm
from clothapi import Clothapi

app = Flask(__name__,	
			static_url_path='',	
			static_folder='static',
            template_folder='templates')

@app.route('/', methods = ['POST','GET'])
def home():
 return render_template('homepage.html')
 

@app.route('/results', methods = ['GET','POST']) 
def result():
	homepage_city = request.form.get("homepage_city")
	homepage_price = request.form.get("homepage_price")
	print(homepage_city)
	print(homepage_price)
	# Clothapi.get_data(homepage_city)
	return render_template("resultTemp2.html",inputted_city = "Monterey", inputted_temp = "40", inputted_weather = "Sunny")
app.run(debug=True, port=5000) 