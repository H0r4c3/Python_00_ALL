'https://stackoverflow.com/questions/36422107/how-to-convert-crlf-to-lf-on-a-windows-machine-in-python'



def convert_line_endings(file_path):

    # replacement strings
    UNIX_LINE_ENDING = b'\n'
    WINDOWS_LINE_ENDING = b'\r\n'
    
    # file path
    #file_path = r"c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Convert_all_line_endings_in_a_file/Subtitle_NOK.srt"
    
    # Open subtitle file and read the content
    with open(file_path, 'rb') as open_file:
        content = open_file.read()
    
    print(content)
    
    content = content.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)
    
    print(content)
    
    with open(file_path, 'wb') as open_file:
       open_file.write(content)
