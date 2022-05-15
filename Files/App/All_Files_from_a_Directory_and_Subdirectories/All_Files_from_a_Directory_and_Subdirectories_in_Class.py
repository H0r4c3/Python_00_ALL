import os
from pathlib import Path


class All_Files_from_a_Directory_and_Subdirectories():
    """ 
    Creates a list with all the folders from a given path and a list with all the files in folders
    """
    def __init__(self):

        self.dir_path = "c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/All_Files_from_a_Directory_and_Subdirectories"

        self.all_dirs = []
        self.all_files = []
        self.dict_folder_and_files = {}
        self.folder_name = ''

    def extract_folder_name_from_dirpath(self, dirpath):
        path_plus_folder_name = dirpath.rsplit('/', 1)
        self.folder_name = path_plus_folder_name[1]

        return self.folder_name


    def create_dict_with_folders_subtitles(self):
        """ Create a dictionary with key = folder and value = list of files in this folder """
        for self.dirpath, self.dirs, self.files in os.walk(self.dir_path):
            self.folder_name = self.extract_folder_name_from_dirpath(self.dirpath)
            self.dict_folder_and_files[self.folder_name] = self.files

        return self.dict_folder_and_files

    def unpack_folders_and_files(self, dict_folder_and_files, extension):
        all_dirs = list(dict_folder_and_files.keys())
        all_files_listoflist = dict_folder_and_files.values()

        for item in all_files_listoflist:
            self.all_files.extend(item)

        # filter after extension
        files_with_a_specific_extension = [file for file in self.all_files if file.endswith(extension)]

        return all_dirs, files_with_a_specific_extension


def main():

    my_object = All_Files_from_a_Directory_and_Subdirectories()

    my_object.create_dict_with_folders_subtitles()

    # create a list of directories and a list of files
    all_dirs, files_with_a_specific_extension = my_object.unpack_folders_and_files(my_object.dict_folder_and_files, "sub")

    print("Dict_Folder_ListOfFiles: ", my_object.create_dict_with_folders_subtitles())
    print("\nAll directories: ", all_dirs)
    print("\nAll files: ", my_object.all_files)
    print("Subtitle files with 'sub' extension: ", files_with_a_specific_extension)

if __name__ == "__main__":
    main()