'https://www.geeksforgeeks.org/python-winsound-module/'
'https://blog.finxter.com/how-to-make-a-beep-sound-in-python-linux-macos-win/?tl_inbound=1&tl_target_all=1&tl_form_type=1&tl_period_type=3&utm_source=newsletter&utm_medium=email&utm_campaign=finxter_weekly_how_to_make_beeep_in_python_and_more&utm_term=2022-01-27'

'''
winsound.Beep( )
The functionality devoted to this method is to generate a ‘Beep’ sound. However, the user is required to input 
the frequency value and the duration of the sound (these are parameters that shall be passed while calling the function).

Note: The frequency must be in the range 37 through 32,767 hertz.
'''

# 1. Example
import winsound 
  
# frequency is set to 500Hz
freq = 500 
  
# duration is set to 100 milliseconds             
dur = 100
               
winsound.Beep(freq, dur)


# 2. Example: “Alle Meine Entchen”
# from winsound import Beep
# notes = {'C': 1635,
#          'D': 1835,
#          'E': 2060,
#          'S': 1945,
#          'F': 2183,
#          'G': 2450,
#          'A': 2750,
#          'B': 3087,
#          ' ': 37}
# melodie = 'CDEFG G AAAAG AAAAG FFFFE E DDDDC'
# for note in melodie:
#     Beep(notes[note], 500)


# 3. Example
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)