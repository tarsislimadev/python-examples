# pip install PyGuitarPro --break-system-packages

import guitarpro

# Get file in https://www.cifraclub.com.br/harpa-crista/porque-ele-vive/guitarpro/
song = guitarpro.parse('./guitarpro-porque-ele-vive.gp5')

for track in song.tracks:
    for measure in track.measures:
        for voice in measure.voices:
            for beat in voice.beats:
                for note in beat.notes:
                    print()
                    print(track)
                    print(measure)
                    print(voice)
                    print(beat)
                    print(note)
                    print()
