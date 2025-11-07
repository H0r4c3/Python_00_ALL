# --------------------------------------------------------
# Script: orga_pop_em.py
# Generează acompaniament curat de orgă pop în E minor, 125 BPM
# --------------------------------------------------------

from midiutil import MIDIFile

# Setări generale
track = 0
channel = 0
time = 0           # start time
tempo = 125        # BPM
volume = 90

# Creează fișierul MIDI
midi = MIDIFile(1)
midi.addTempo(track, time, tempo)

# Acorduri (note MIDI)
chords = {
    "Em": [52, 55, 59],  # E G B
    "G": [55, 59, 62],   # G B D
    "D": [50, 57, 62],   # D A D
    "C": [48, 55, 60],   # C G C
}

# Structura piesei
progression = (
    ["Em"] * 2 +                # intro
    ["Em", "G", "D", "C"] * 4 + # vers
    ["Em", "C", "G", "D"] * 4 + # refren
    ["Em", "C"] * 2 +           # bridge
    ["Em", "C", "G", "D"] * 2   # final
)

# Fiecare acord durează 1 măsură (4 bătăi)
for chord_name in progression:
    for note in chords[chord_name]:
        midi.addNote(track, channel, note, time, 4, volume)
    time += 4

# Salvează fișierul MIDI
output_file = "Orga_Eminor_Pop_125BPM.mid"
with open(output_file, "wb") as f:
    midi.writeFile(f)

print(f"✅ Fișierul MIDI a fost generat: {output_file}")
