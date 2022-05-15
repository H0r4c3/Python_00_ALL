import os
from pathlib import Path

'''
root_and_name_string = __file__ # string with the path of the .py file + the name of the .py file
root_and_name_list = root_and_name_string.rsplit('\\', 1) # list with 2 strings: path + name
dir_path = root_and_name_list[0] # string with only the path of the folder the .py file is in

path_of_file = Path(__file__).parent.absolute() # the full absolute path to the current file
path_of_folder = Path(__file__) # the path to the folder the file is in

os.path.basename(path) : It is used to return the basename of the file . This function basically return the file name from the path given.
os.path.dirname(path) : It is used to return the directory name from the path given. This function returns the name from the path except the path name. 
'''


class AllFilesFromADirectoryAndSubdirectories():
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
        """ Create a dictionary with key = folder and value = the files in this folder """
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

    object = AllFilesFromADirectoryAndSubdirectories()

    object.create_dict_with_folders_subtitles()

    # create a list of directories and a list of files
    all_dirs, files_with_a_specific_extension = object.unpack_folders_and_files(object.dict_folder_and_files, "sub")

    print("\nAll directories: ", all_dirs)
    print("\nAll files: ", object.all_files)
    print("\nSubtitle files with 'sub' extension: ", files_with_a_specific_extension)

if __name__ == "__main__":
    main()