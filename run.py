from PIL import Image
import json
from os import listdir

image_size = 1024
tile_size = 64


def crop(image_name):
	image = Image.open(r"./input/" + image_name + ".png") 
	image_params = params[image_name]
	width  = image_params["w"]
	height = image_params["h"]

	left  = image_size/2 - tile_size * width/2
	right = image_size/2 + tile_size * width/2

	top    = image_size - tile_size * height
	bottom = image_size


	cropped_image = image.crop((left, top, right, bottom)) 
	cropped_image.save("./output/" + image_name + ".png")

with open('images.json') as json_file:
	params = json.load(json_file)

for image_name in listdir("./input"):
	crop(image_name.split(".")[0])

