'Replace the diacritics in a srt file (subtile file)'

'''
letters = [(u'\u0219',u'\u015f'),(u'\u021b',u'\u0163'),(u'\0218',u'\u015e'),
            (u'\u021a',u'\u0162')] #(new diacritic, old diacritic)
'''

from GUI_for_selecting_a_file import CreateMenusFieldsButtons

# path1 = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\Replace_Diacritics\Subtitle_File.srt'
# path2 = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\Replace_Diacritics\Subtitle_File_NEW.srt'


class ReplaceDiacriticsInSrtFile():
    def __init__(self):
        pass
           
    def read_content_from_file(self, path1):
        with open(path1, 'r') as open_file:
            content = open_file.read() #returns a string with all the lines in the file
        return content

    def replace_chars(self, content):
        content_without_diacritics = content.replace('þ', 't').replace('º', 's').replace('ã', 'a').replace('â', 'a').replace('ª', 'S').replace('Þ', 'T').replace('Ã', 'A')
        print('Diacritics replaced!')
        return content_without_diacritics

    def write_content_to_file(self, path2, content_without_diacritics):
        with open(path2, 'w') as open_file:
            open_file.write(content_without_diacritics)
        print('Done! New file saved!')



# def main():
#     my_GUI = CreateMenusFieldsButtons()
    
#     # Start the GUI event loop (performing an infinite loop for the window to display)
#     my_GUI.root.mainloop()
    
    
# if __name__ == "__main__":
#     main()
