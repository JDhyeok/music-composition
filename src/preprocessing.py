import glob
import numpy as np
import pandas as pd
import pickle
from music21 import converter, instrument, note, chord

def get_notes():
    notes = []

    for file in glob.glob("../midi/*.mid"):
        midi = converter.parse(file)

        notes_to_parse = None
        
        try:
            s2 = instrument.partitionByInstrument(midi)
            notes_to_parse = s2.parts[0].recurse()
        except:
            note_to_parse = midi.flat.notes
            
        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))
        
        #with open('./', 'wb') as filepath:
        #    pickle.dump(notes, filepath)
            
        return notes