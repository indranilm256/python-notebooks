import mido
from mido import Message, MidiFile, MidiTrack, bpm2tempo

# Set tempo and time signature
bpm = 68
tempo = bpm2tempo(bpm)
ticks_per_beat = 480  # Standard MIDI resolution

# Define chord voicings (right hand) and bass notes (left hand) in MIDI note numbers
# Chords in Db major key: Db, Ab, Bbm, Gb
chords = [
    {"name": "Db",  "right": [65, 68, 73], "left": [49]},  # F Ab Db | Db bass
    {"name": "Ab",  "right": [60, 63, 68], "left": [44]},  # C Eb Ab | Ab bass
    {"name": "Bbm", "right": [61, 65, 70], "left": [46]},  # Db F Bb | Bb bass
    {"name": "Gb",  "right": [58, 61, 66], "left": [42]},  # Bb Db Gb | Gb bass
]

# Duration: each chord holds for 1 bar = 3 quarter notes in 6/8
duration = ticks_per_beat * 3

# Create MIDI file and track
mid = MidiFile(ticks_per_beat=ticks_per_beat)
track = MidiTrack()
mid.tracks.append(track)

# Set tempo
track.append(Message('program_change', program=0, time=0))
track.append(mido.MetaMessage('set_tempo', tempo=tempo))

# Add chords and bass notes
for chord in chords:
    # Note on (right hand)
    for note in chord["right"]:
        track.append(Message('note_on', note=note, velocity=80, time=0))
    # Note on (left hand)
    for note in chord["left"]:
        track.append(Message('note_on', note=note, velocity=90, time=0))
    # Note off (after duration)
    for note in chord["right"] + chord["left"]:
        track.append(Message('note_off', note=note, velocity=64, time=duration))

# Save the MIDI file
output_path = "/Users/packofice/Desktop/ArturiaProjects/sun_is_shining_down_intro_chords.mid"
mid.save(output_path)

output_path