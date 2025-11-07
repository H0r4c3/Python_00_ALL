
from GUI_for_selecting_a_folder import GUIForSelectingAFolder
from files_renamer import AllFilesFromAFolder

def main():
    # Create the GUI
    my_GUI = GUIForSelectingAFolder()
    
    path_folder = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\App\Rename_Randomly_All_Files_in_a_Folder\Folder_with_Files'
    
    #path_folder = r'b:\MP3\Spotify_MP3\LIKED_SONGS\Horace_Liked_Songs_ALL_Random'
    
    #path_folder = my_GUI.browse_for_folder
    print(path_folder)

    my_object = AllFilesFromAFolder(path_folder)
    folder_subfolder_files = my_object.all_files_and_subfolders_in_a_folder()
    list_of_path_of_files = my_object.paths_of_files(folder_subfolder_files)
    list_of_paths_of_files_having_extension = my_object.paths_of_files_having_specific_extension(list_of_path_of_files, ('.mp3'))
    list_of_unique_random_numbers = AllFilesFromAFolder.unique_random_numbers(1, len(list_of_path_of_files), len(list_of_path_of_files))
    print(list_of_unique_random_numbers)
    print(len(list_of_path_of_files))
    print(len(list_of_unique_random_numbers))
    
    my_object.rename_files(path_folder)

    for file in list_of_paths_of_files_having_extension:
        print(file)

    # Start the GUI event loop (performing an infinite loop for the window to display)
    my_GUI.root.mainloop()


if __name__ == "__main__":
    main()