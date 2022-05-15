
import pygame

PATH1 = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Sounds\English_to_Morse_Code_Audio_Converter\morse_code_audio\S_morse_code.ogg'
PATH2 = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Sounds\English_to_Morse_Code_Audio_Converter\morse_code_audio\O_morse_code.ogg'
PATH3 = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Sounds\English_to_Morse_Code_Audio_Converter\morse_code_audio\S_morse_code.ogg'

TIME_BETWEEN = 0.5

pygame.init()

pygame.mixer.music.load(PATH1)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()
time.sleep(3 * TIME_BETWEEN)
pygame.mixer.music.load(PATH2)
time.sleep(3 * TIME_BETWEEN)
pygame.mixer.music.load(PATH3)