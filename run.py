from PIL import Image
import json
import os


image_size = 512
half_tile_size = 32
icon_size = 64

main_path = "../godot_farm/assets/textures/entities/"
icon_path = "../godot_farm/assets/textures/icons/"


def crop(image_name):
	image_params = params[image_name]
	width  = image_params["w"]
	height = image_params["h"]
	frames = image_params["frames"]
	output_path = image_params["outputPath"]
	
	save_icon = "iconFrame" in image_params
	if(save_icon):
		icon_frame = image_params["iconFrame"]

	left  = image_size/2 - half_tile_size * width
	right = image_size/2 + half_tile_size * width

	top    = image_size - half_tile_size * height*2
	bottom = image_size

	image_width = half_tile_size * width
	image_height = half_tile_size * height

	image_out = Image.new('RGBA', (image_width * 2, image_height * 2 * frames))
	image_out_normal = Image.new('RGBA', (image_width * 2, image_height * 2 * frames))
	image_icon = Image.new('RGBA', (icon_size, icon_size))

	for i in range(0, frames):
		image = Image.open(r"./input/" + image_name + "/output/" + image_name + str(i) + ".png") 

		cropped_image = image.crop((left, top, right, bottom)) 
		image_out.paste(cropped_image, (0, image_height * 2 * i))

		image_normal = Image.open(r"./input/" + image_name + "/output/normals/" + image_name + str(i) + ".png")
		cropped_image_normal = image_normal.crop((left, top, right, bottom))
		image_out_normal.paste(cropped_image_normal, (0, image_height * 2 * i))

		if(save_icon and i == icon_frame):
			if(width > height):
				ratio = width
			else:
				ratio = height
			icon_sized_image = cropped_image.resize(((int)(64*(ratio/width)), (int)(64*(ratio/height))))
			image_icon.paste(icon_sized_image)
			saveImage("./output/" + image_name + "/icons/", image_name, image_icon)
			saveImage(icon_path + output_path, image_name, image_icon)

	saveImage('./output/' + image_name + "/", image_name, image_out)
	saveImage('./output/' + image_name + "/normals/", image_name, image_out_normal)

	saveImage(main_path + output_path, image_name, image_out)
	saveImage(main_path + output_path + "normals/", image_name, image_out_normal)



def saveImage(path, fileName, image):
	if not os.path.exists(path):
		os.makedirs(path)
	image.save(path + image_name + ".png")

with open('images.json') as json_file:
	params = json.load(json_file)


for image_name in params:
	crop(image_name)

