from PIL import Image

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

im = Image.open("dog.jpg")

data = im.getdata()
data_list = list(data)
new_pic = []
def colorize(image_data):
	for pixel in image_data:
		red = pixel[0]
		green = pixel[1]
		blue = pixel[2]
		intensity = red + green + blue
		if intensity < 182:
			new_pic.append(darkBlue)
		elif intensity < 364:
			new_pic.append(red)
		elif intensity < 546:
			new_pic.append(lightBlue)
		else:
			new_pic.append(yellow)	

	return new_pic
new_data = colorize(data_list)	
new_image = Image.new(im.mode, im.size)
new_image.putdata(new_data)
new_image.show()
new_image.save("dog.jpg")
