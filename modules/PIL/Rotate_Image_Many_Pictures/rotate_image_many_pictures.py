import os
from PIL import Image

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\PIL\Rotate_Image_Many_Pictures\Rotated_Images\DSCN1369.JPG'

path_folder_output = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\PIL\Rotate_Image_Many_Pictures\Rotated_Images\DSCN1369.JPG'

path_folder_input = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\PIL\Rotate_Image_Many_Pictures'

path1 = path_folder_input + '\\1.JPG'
path2 = path_folder_input + '\\2.JPG'
path3 = path_folder_input + '\\3.JPG'
path4 = path_folder_input + '\\4.JPG'
path5 = path_folder_input + '\\5.JPG'

list_of_paths_of_files_having_extension = [path1, path2, path3, path4, path5]


class RotateImageManyPictures:
    def __init__(self, list_of_paths_of_files_having_extension):
        self.list_of_paths_of_files_having_extension = list_of_paths_of_files_having_extension
        self.list_with_images_for_rotate = []
        
    
    def create_list_with_images_for_rotate(self):
        for path in self.list_of_paths_of_files_having_extension:
            my_image = Image.open(path)
            if my_image.size[0] > my_image.size[1]:
                self.list_with_images_for_rotate.append(path)
                
            my_image.close()
            
        return self.list_with_images_for_rotate
    

    def rotate_image(self, path):
        my_image = Image.open(path)
        print('START image ', path)
        print('My Image size = ', my_image.size)
        print('My Image dpi = ', my_image.info['dpi'])

        # Rotate my_image with 270 degrees
        rotated_img = my_image.rotate(270, resample=Image.BICUBIC, expand=True)

        print('Rotated Image size = ', rotated_img.size)
        print('Rotated Image dpi = ', rotated_img.info['dpi'])

        #rotate_img.show()

        # Create path for saved file
        path2 = path.replace('.JPG', '_2.JPG').replace('Rotate_Image_Many_Pictures', 'Rotate_Image_Many_Pictures\Rotated_Images')

        # Using a quality factor of 95 should be enough to preserve the image quality
        rotated_img.save(path2, quality=95, dpi=(300.0, 300.0))

        # Open the saved image for printing the properties
        my_new_image = Image.open(path2)

        print('Saved Image size = ', my_new_image.size)
        print('Saved Image dpi = ', my_new_image.info['dpi'])
        print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
        
        my_image.close()
        my_new_image.close()


def main():
    my_object = RotateImageManyPictures(list_of_paths_of_files_having_extension)

    my_object.list_with_images_for_rotate = my_object.create_list_with_images_for_rotate()

    for path in my_object.list_with_images_for_rotate:
        my_object.rotate_image(path)
        
if __name__ == "__main__":
    main()