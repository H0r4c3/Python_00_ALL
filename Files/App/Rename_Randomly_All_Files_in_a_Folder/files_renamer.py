import os
import sys
import random

sys.path.append(r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\App\Rename_Randomly_All_Files_in_a_Folder')
#sys.path.append(r'b:\MP3\Spotify_MP3\LIKED_SONGS\Horace_Liked_Songs_ALL')


class AllFilesFromAFolder:
    def __init__(self, path_folder):
        self.path_folder = path_folder
    
    def all_files_and_subfolders_in_a_folder(self):
        # tuple with the folder + the directories in that folder + the files in that folder
        folder_subfolders_files = os.walk(self.path_folder)
        
        return folder_subfolders_files 

    def paths_of_files(self, folder_subfolders_files):
        list_of_paths_of_files = list()
        
        for folder, subfolders, files in folder_subfolders_files:
            print('Folder: ', folder)
            print('Subfolders: ', subfolders)
            print('Files: ', files)
            
            # create a list of paths of all files in folder
            for filename in files:
                list_of_paths_of_files.append(os.path.join(folder, filename))
        
        return list_of_paths_of_files
            
    def paths_of_files_having_specific_extension(self, list_of_paths_of_files, extension):
        list_of_paths_of_files_having_extension = [item for item in list_of_paths_of_files if item.endswith(extension)]
        
        return list_of_paths_of_files_having_extension
    
    def unique_random_numbers(start, end, count):
        '''Generate a list of unique random numbers within the specified range'''
        if count > (end - start + 1):
            raise ValueError("Count should not exceed the range!")
        list_of_unique_random_numbers = random.sample(range(start, end + 1), count)
        return list_of_unique_random_numbers
    
    
    def rename_files(self, path_folder):
        '''Rename files in the given folder'''
        files = os.listdir(path_folder)
        list_of_unique_random_numbers = AllFilesFromAFolder.unique_random_numbers(1, len(files), len(files))
        i = 0
        for file_name in files:
            # Add a random number in front of the name of mp3
            #new_name = str(list_of_unique_random_numbers[i]) + '-' + os.path.splitext(file_name)[1]
            number = list_of_unique_random_numbers[i]
            if len(str(number)) == 1:
                new_name = '00' + str(list_of_unique_random_numbers[i]) + '-' + file_name
            elif len(str(number)) == 2:
                new_name = '0' + str(list_of_unique_random_numbers[i]) + '-' + file_name
            else:
                new_name = str(list_of_unique_random_numbers[i]) + '-' + file_name
                
                
            i += 1
            # Construct the new path
            new_path = os.path.join(path_folder, new_name)
            # Rename the file
            os.rename(os.path.join(path_folder, file_name), new_path)



# def main():
#     # Create the GUI
#     my_GUI = GUIForSelectingAFolder()
    
#     path_folder = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\App\Rename_Randomly_All_Files_in_a_Folder\Folder_with_Files'
#     #path_folder = my_GUI.browse_for_folder

#     my_object = AllFilesFromAFolder(path_folder)
#     folder_subfolder_files = my_object.all_files_and_subfolders_in_a_folder()
#     list_of_path_of_files = my_object.paths_of_files(folder_subfolder_files)
#     list_of_paths_of_files_having_extension = my_object.paths_of_files_having_specific_extension(list_of_path_of_files, ('.mp3'))
#     list_of_unique_random_numbers = AllFilesFromAFolder.unique_random_numbers(1, len(list_of_path_of_files), len(list_of_path_of_files))
#     print(list_of_unique_random_numbers)
#     print(len(list_of_path_of_files))
#     print(len(list_of_unique_random_numbers))
    
#     my_object.rename_files(path_folder)

#     for file in list_of_paths_of_files_having_extension:
#         print(file)

#     # Start the GUI event loop (performing an infinite loop for the window to display)
#     my_GUI.root.mainloop()


def main():
    pass


if __name__ == "__main__":
    main()