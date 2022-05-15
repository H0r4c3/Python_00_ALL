# open the Subtitle.srt file for reading
subtitle_reader = open(r"C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\Subtitle.srt")

# open the "RO.srt" file for writing
ro_writer = open(r"C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Files\RO.srt", 'w')

# read the content of the Subtitle.srt file
r = subtitle_reader.readlines()

# write the content of "Subtitle.srt" file to "ro.srt" file
ro_writer.writelines(r)

subtitle_reader.close()
ro_writer.close()


#Method2:
#path1 = 'file1.txt'
#path2 = 'file2.txt'
#with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
#    dog_breeds = reader.readlines()
#    writer.writelines(reversed(dog_breeds))




