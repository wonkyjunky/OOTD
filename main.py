from flask import Flask, request, render_template, url_for
from flask import redirect

from clothapi import Clothapi
from weather import Weatherapi
import clothes
import ast 
#from hw4

def find_dict_from_url(arr, url):
	for item in arr:
		if url == item["image"]:
			return item
	return {}

app = Flask(__name__,	
			static_url_path='',	
			static_folder='static',
            template_folder='templates')


@app.route('/test')
def article_of_clothing():
	article_data = request.args.get('output', default = '*', type = str)
	article_data = ast.literal_eval(article_data)
	return render_template("article_of_clothing.html",clothing_data = article_data)

@app.route('/', methods = ['POST','GET'])
def home():
 return render_template('homepage.html')
 

@app.route('/results', methods = ['POST', 'GET']) 
def result():
	homepage_city = request.form.get("homepage_city")
	homepage_price = request.form.get("homepage_price")
	print(homepage_city)
	print(homepage_price)

	homepage_city = homepage_city.replace(" ", "%20")
	clothes_api_result = Clothapi().get_data(homepage_city, homepage_price)
	weather_api_result = Weatherapi().get_data(homepage_city)
	print(weather_api_result)
	
	homepage_city = homepage_city.replace("%20", " ")
	hat_dict =  find_dict_from_url(clothes.hat_info, clothes_api_result[0])
	outerwear_dict = find_dict_from_url(clothes.outer_info, clothes_api_result[1]) 
	top_dict = find_dict_from_url(clothes.top_info, clothes_api_result[2])
	pants_dict = find_dict_from_url(clothes.pants_info, clothes_api_result[3]) 
	shoes_dict = find_dict_from_url(clothes.shoe_info, clothes_api_result[4])
	accessories_dict = find_dict_from_url(clothes.acc_info, clothes_api_result[5])
	
	outfit_data_arr = [hat_dict,outerwear_dict,top_dict,pants_dict,shoes_dict,accessories_dict]

	for i in range(len(outfit_data_arr)):
		outfit_data_arr[i] = str(outfit_data_arr[i])

	return render_template("resultTemp2.html",inputted_city = homepage_city, inputted_temp = weather_api_result[1], inputted_weather = weather_api_result[2], output_hat = clothes_api_result[0], output_outerwear = clothes_api_result[1], output_top = clothes_api_result[2], output_pants = clothes_api_result[3], output_shoes = clothes_api_result[4], output_accessories= clothes_api_result[5], outfit_data_arr = outfit_data_arr)



app.run(debug=True, port=5000) 