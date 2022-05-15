import os
import sys

sys.path.append(r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL')

from GUI.Selecting_a_Folder.GUI_for_selecting_a_folder import GUIForSelectingAFolder


class AllFilesFromAFolder:
    def __init__(self, path_folder):
        self.path_folder = path_folder
    
    def all_files_and_subfolders_in_a_folder(self):
        # tuple with the folder + the directories in that folder + the files in that folder
        folder_subfolders_files = os.walk(self.path_folder)
        
        return folder_subfolders_files 

    def paths_of_files(self, folder_subfolders_files):
        list_of_paths_of_files = []
        
        for folder, subfolders, files in folder_subfolders_files:
            print('Folder: ', folder)
            print('Subfolders: ', subfolders)
            print('Files: ', files)
            print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
            
            # create a list of paths of all files in folder
            for filename in files:
                list_of_paths_of_files.append(os.path.join(folder, filename))
        
        return list_of_paths_of_files
            
    def paths_of_files_having_specific_extension(self, list_of_paths_of_files, extension):
        list_of_paths_of_files_having_extension = [item for item in list_of_paths_of_files if item.endswith(extension)]
        
        return list_of_paths_of_files_having_extension



# def main():
#     # Create the GUI
#     my_GUI = GUIForSelectingAFolder()
    
#     path_folder = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\All_Files_from_a_Folder'

#     my_object = AllFilesFromAFolder(path_folder)
#     folder_subfolder_files = my_object.all_files_and_subfolders_in_a_folder()
#     list_of_path_of_files = my_object.paths_of_files(folder_subfolder_files)
#     list_of_paths_of_files_having_extension = my_object.paths_of_files_having_specific_extension(list_of_path_of_files, ('.JPG', 'jpg'))

#     for pic in list_of_paths_of_files_having_extension:
#         print(pic)

#     # Start the GUI event loop (performing an infinite loop for the window to display)
#     my_GUI.root.mainloop()


# if __name__ == "__main__":
#     main()