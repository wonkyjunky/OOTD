import clothes
from weather import Weatherapi
import random
import request

class Clothapi():
	@staticmethod
	def get_data(self, city, price):

		hatdata = clothes.hat_info
		outerdata = clothes.outer_info
		topdata = clothes.top_info
		pantsdata = clothes.pants_info
		shoedata = clothes.shoe_info
		accdata = clothes.acc_info

		api = Weatherapi()
		arr = api.get_data(city)


		hatnames = []
		outernames = []
		topnames = []
		pantsnames = []
		shoenames = []
		accnames = []
		finalnames = []

		for x in hatdata:
			if (x["price"] > 0 and x["price"] < 1000):
				for a in x["tags"]:
					if a == arr[2]:
						if x["temperature"][0] <= arr[1] and x["temperature"][1] >= arr[1]:
							hatnames.append(x["image"])

		if (len(hatnames) > 0):
			a = random.choice(hatnames)

		finalnames.append(a)

		for x in outerdata:
			if (x["price"] > 0 and x["price"] < 1000):
				for a in x["tags"]:
					if a == arr[2]:
						if x["temperature"][0] <= arr[1] and x["temperature"][1] >= arr[1]:
							outernames.append(x["image"])


		b = random.choice(outernames)
		finalnames.append(b)

		for x in topdata:
			if (x["price"] > 0 and x["price"] < 1000):
				for a in x["tags"]:
					if a == arr[2]:
						if x["temperature"][0] <= arr[1] and x["temperature"][1] >= arr[1]:
							topnames.append(x["image"])


		c = random.choice(topnames)
		finalnames.append(c)


		for x in pantsdata:
			if (x["price"] > 0 and x["price"] < 1000):
				for a in x["tags"]:
					if a == arr[2]:
						if x["temperature"][0] <= arr[1] and x["temperature"][1] >= arr[1]:
							pantsnames.append(x["image"])


		d = random.choice(pantsnames)
		finalnames.append(d)

		for x in shoedata:
			if (x["price"] > 0 and x["price"] < 1000):
				for a in x["tags"]:
					if a == arr[2]:
						if x["temperature"][0] <= arr[1] and x["temperature"][1] >= arr[1]:
							shoenames.append(x["image"])

		e = random.choice(shoenames)
		finalnames.append(e)

		for x in accdata:
			if (x["price"] > 0 and x["price"] < 1000):
				for a in x["tags"]:
					if a == arr[2]:
						if x["temperature"][0] <= arr[1] and x["temperature"][1] >= arr[1]:
							accnames.append(x["image"])


		f = random.choice(accnames)
		finalnames.append(f)

		return finalnames
