import clothes
from weather import Weatherapi
import random
import request

hatdata = clothes.hat_info
outerdata = clothes.outer_info
topdata = clothes.top_info
pantsdata = clothes.pants_info
shoedata = clothes.shoe_info
accdata = clothes.acc_info

api = Weatherapi()
arr = api.get_data(request.form.get("weather"))


hatnames = []
for x in hatdata:
	if (x["price"] > 0 and x["price"] < 50):
		for a in x["tags"]:
			if a == arr[2]:
				if x["temperature"][0] <= arr[1] and x["temperature"][1] >= arr[1]:
					hatnames.append(x["image"])


print(random.choice(hatnames))