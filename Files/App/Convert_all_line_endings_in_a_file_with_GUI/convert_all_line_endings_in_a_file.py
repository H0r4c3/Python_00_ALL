'https://stackoverflow.com/questions/36422107/how-to-convert-crlf-to-lf-on-a-windows-machine-in-python'



def convert_line_endings(file_path):

    # replacement strings
    UNIX_LINE_ENDING = b'\n'
    WINDOWS_LINE_ENDING = b'\r\n'
    
    
    # Open subtitle file and read the content
    with open(file_path, 'rb') as open_file:
        content = open_file.read()
    
    print(f'\n Before replacing: \n{content}')
    
    content = content.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)
    
    print(f'\n After replacing: \n {content}')
    
    with open(file_path.replace('.srt', '_2.srt' ), 'wb') as open_file:
       open_file.write(content)
       
    print('\n Replacing finished!')


#file_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\Convert_all_line_endings_in_a_file\Squid.Game.S01E04.KOREAN.WEBRip.x264-ION10[eztv.re].srt'

#convert_line_endings(file_path)
