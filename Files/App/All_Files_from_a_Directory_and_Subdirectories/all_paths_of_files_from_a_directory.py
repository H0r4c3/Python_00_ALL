import os

'''
dirpath is a string, the path to the directory. 
dirnames is a list of the names of the subdirectories in dirpath (excluding '.' and '..'). 
filenames is a list of the names of the non-directory files in dirpath
To get a full path (which begins with top) to a file or directory in dirpath, do os.path.join(dirpath, name).

os.path.basename(path) : It is used to return the basename of the file . This function basically return the file name from the path given.
os.path.dirname(path) : It is used to return the directory name from the path given. This function returns the name from the path except the path name. 
'''


path = 'C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/0_ALL/Files/All_Files_from_a_Directory_and_Subdirectories/'



class AllPathsOfFilesFromADirectory:
    '''This Class is searching for files with extension "extension" in a folder with the path "path" and returns a list with the paths of these files'''
    
    def __init__(self):
        self.file_paths = []
        self.list_of_selected_files = []
        #self.extension = extension
    
    def paths_for_all_files(self, path):
        '''This method gets the full path of every file in a folder and subfolders and make a list named "file_paths" with all the paths'''

        # transform the path string into a raw string
        raw_path = (r'%s' %path)

        for dirpath, dirnames, filenames in os.walk(raw_path):
            #print("dirpath:", dirpath)
            #print("dirnames: ", dirnames)
            #print("filenames: ", filenames)

            # get the full path of every file
            for item in filenames:
                full_path = os.path.join(dirpath, item)
                raw_full_path = r'%s' %full_path
                self.file_paths.append(raw_full_path)
                #print("full_path:", raw_full_path)
                #print(self.file_paths)
        return self.file_paths


    def filter_files_in_list(self, list_of_files, extension):
        '''This method filters the files with extension "extension" from the list with the paths for all files'''

        for item in list_of_files:
            if item[-3:] == extension:
                self.list_of_selected_files.append(item)
        return self.list_of_selected_files


my_object = AllPathsOfFilesFromADirectory()

my_object.file_paths = my_object.paths_for_all_files(path)
my_object.filter_files_in_list(my_object.file_paths, 'srt')
for item in my_object.list_of_selected_files:
    print(item)
