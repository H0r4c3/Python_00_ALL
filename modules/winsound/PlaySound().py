'https://docs.python.org/3/library/winsound.html'

'''
winsound.PlaySound(sound, flags)

Call the underlying PlaySound() function from the Platform API. The sound parameter may be a filename, a system sound alias, 
audio data as a bytes-like object, or None. Its interpretation depends on the value of flags, which can be a bitwise ORed combination of 
the constants described below. 
If the sound parameter is None, any currently playing waveform sound is stopped. If the system indicates an error, RuntimeError is raised.
'''

import winsound 

# 1. Example
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)