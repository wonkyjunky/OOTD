import json
import urllib.request



class Weatherapi:
	@staticmethod
	def get_data(city):

		loca=""
		url='http://api.openweathermap.org/data/2.5/weather?q='+city+',us&appid=c9ed41a4f7c70f576c1527b42d197266'

		with urllib.request.urlopen(url) as url:
		    s = url.read()

		j = json.loads(s)
		main = j["main"]
		temp = main["temp"]
		tmp1 = int(round(temp - 273.15) * 9/5 + 32)

		main = j["main"]
		temp = main["temp"]

		weather = j["weather"]
		temp1 = weather[0]
		main = temp1["main"]
		condition = temp1["description"]
		if ("cloud" in condition or "fog" in condition):
			condition = "cloudy"
		if ("sun" in condition or "clear" in condition):
			condition = "sunny"
		if ("rain" in condition):
			condition = "rainy"

		sys = j['sys']
		country= sys['country']

		name = j['name']

		a = (f"{name}, {country}.\n{tmp1}ºF. Condition: {condition}.")

		b = [name, tmp1, condition]

		return b
