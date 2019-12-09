from flask import Flask, request, render_template 
from flask_wtf import FlaskForm

app = Flask(__name__,	
			static_url_path='',	
			static_folder='static',
            template_folder='templates')

@app.route('/', methods = ['POST','GET'])
def home():
 return render_template('homepage.html')
 

@app.route('/results', methods = ['GET','POST']) 
def result():
	if request.method == 'POST':
		print("form recieved")
		print("The user inputted: " + request.form.get("weather"))
	
	return render_template("result_super_temporary.html",output = "Hello, World!")
app.run(debug=True, port=5000) 