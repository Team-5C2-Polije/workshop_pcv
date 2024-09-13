from PIL import Image

image_path = 'your_image_path_here.jpg'
image = Image.open(image_path)

left = 50
top = 50
right = 350
bottom = 250

cropped_image = image.crop((left, top, right, bottom))

cropped_image.save('cropped_image.jpg')

cropped_image.show()