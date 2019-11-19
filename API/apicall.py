from weather import Weatherapi



weather = Weatherapi()

city = input()
city = city.replace(" ", "%20")

for x in weather.get_data(city)[2].split():
	if x == "clouds":
		print("happy")
