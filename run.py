from PIL import Image
import json
from os import listdir

image_size = 1024
tile_size = 64


def crop(image_name):
	image_params = params[image_name]
	width  = image_params["w"]
	height = image_params["h"]
	frames = image_params["frames"]

	left  = image_size/2 - tile_size * width
	right = image_size/2 + tile_size * width

	top    = image_size - tile_size * height*2
	bottom = image_size

	for i in range(0, frames):
		image = Image.open(r"./input/" + image_name + "/output/" + image_name + str(i) + ".png") 

		cropped_image = image.crop((left, top, right, bottom)) 
		cropped_image.save("./output/" + image_name + "/" + image_name + str(i) + ".png")

with open('images.json') as json_file:
	params = json.load(json_file)

for image_name in params:
	crop(image_name)

