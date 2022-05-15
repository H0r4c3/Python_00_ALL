import os
from pathlib import Path

# dir_path = "c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/All_Files_from_a_Directory_and_Subdirectories"
'''
root_and_name_string = __file__ # string with the path of the .py file + the name of the .py file
root_and_name_list = root_and_name_string.rsplit('\\', 1) # list with 2 strings: path + name
dir_path = root_and_name_list[0] # string with only the path of the folder the .py file is in

path_of_file = Path(__file__).parent.absolute() # the full absolute path to the current file
path_of_folder = Path(__file__) # the path to the folder the file is in
'''

all_dirs = []
all_subtitle_files = []
dict_folder_and_files = {}

def extract_folder_name_from_dirpath(dirpath):
    path_and_folder_name = dirpath.rsplit('\\', 1)
    #print("path_and_folder_name: ", path_and_folder_name)
    folder_name = path_and_folder_name[1]
    #print("folder_name:", folder_name)

    return folder_name


# Get the list of all files in directory tree at given path
def get_all_files(dir_path, extension):
    for dirpath, dirs, files in os.walk(dir_path):
        print("dirpath: ", dirpath)
        print("dirs: ", dirs)
        print("files", files)
        for file in files:
            if file.endswith(extension):
                all_subtitle_files.append(file)
                [all_dirs.append(dir) for dir in dirs if dir not in all_dirs]
    return all_dirs, all_subtitle_files
#srt_dirs, srt_subtitle_files = get_all_files(dir_path, '.srt')
#sub_dirs, sub_subtitle_files = get_all_files(dir_path, '.sub')


def create_dict_with_folders_subtitles():
    """ Create a dictionary with key = folder and value = the files in this folder """
    for dirpath, dirs, files in os.walk(dir_path):
        #print("dirpath: ", dirpath)
        folder_name = extract_folder_name_from_dirpath(dirpath)
        #print("foldername: ", folder_name)
        #print("files: ", files)
        dict_folder_and_files[folder_name] = files

    return dict_folder_and_files

def unpack_folders_and_files(dict_folder_and_files):
    all_dirs = list(dict_folder_and_files.keys())
    all_subtitle_files_listoflist = dict_folder_and_files.values()

    for item in all_subtitle_files_listoflist:
        all_subtitle_files.extend(item)

    return all_dirs, all_subtitle_files


create_dict_with_folders_subtitles()

# create a list of directories and a list of files
all_dirs, all_subtitle_files = unpack_folders_and_files(dict_folder_and_files)

# filter after extension
files_with_a_specific_extension = [file for file in all_subtitle_files if file.endswith("sub")]


print("All directories: ", all_dirs)
print("All subtitle files: ", all_subtitle_files)
print("Subtitle files with 'sub' extension: ", files_with_a_specific_extension)


