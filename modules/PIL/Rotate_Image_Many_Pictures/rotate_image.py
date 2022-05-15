'https://www.askpython.com/python/examples/rotate-an-image-by-an-angle-in-python'

from PIL import Image

path = r"C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\PIL\DSCN1369.JPG"
my_image = Image.open(path)
print('My Image size = ', my_image.size)
print('My Image dpi = ', my_image.info['dpi'])

# Rotate my_image with 270 degrees
rotated_img = my_image.rotate(270, resample=Image.BICUBIC, expand=True)

print('Rotated Image size = ', rotated_img.size)
print('Rotated Image dpi = ', rotated_img.info['dpi'])

#rotate_img.show()

path2 = path.replace('.JPG', '_2.JPG')

# Using a quality factor of 95 should be enough to preserve the image quality
rotated_img.save(path2, quality=95, dpi=(300.0, 300.0))


#path2 = r"C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\PIL\DSCN1369_2.JPG"
path2 = path.replace('.JPG', '_2.JPG')
my_new_image = Image.open(path2)

print('Saved Image size = ', my_new_image.size)
print('Saved Image dpi = ', my_new_image.info['dpi'])
