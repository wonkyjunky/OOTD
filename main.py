from flask import Flask, request, render_template 
from flask_wtf import FlaskForm
from clothapi import Clothapi
from weather import Weatherapi

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
	
	clothes_api_result = Clothapi().get_data(homepage_city, homepage_price)
	weather_api_result = Weatherapi().get_data(homepage_city)
	print(weather_api_result)


	return render_template("resultTemp2.html",inputted_city = homepage_city, inputted_temp = weather_api_result[1], inputted_weather = weather_api_result[2], output_hat = clothes_api_result[0], output_outerwear = clothes_api_result[1], output_top = clothes_api_result[2], output_pants = clothes_api_result[3], output_shoes = clothes_api_result[4], output_accessories= clothes_api_result[5])


app.run(debug=True, port=5000) 