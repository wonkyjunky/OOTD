from weather import Weatherapi
from PIL import Image

im1 = Image.open("weatherImage/cloud.png")

#call the funtion from weather.py
weather = Weatherapi()

#user input city where they live
city = input()
# if there's space between words, it replace it with "%20"
city = city.replace(" ", "%20")


for x in weather.get_data(city)[2].split():
	if x == "clouds":
		im1.show()
		
#working on the images if condition has cloud, it prints cloud image.
