import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sbn

# file handling
from glob import glob

# audio stuff
import librosa
import librosa.display

sbn.set_theme(style="white", palette=None)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
#color_cycle = cycle(plt.rcParams["axes.prop_cycle"].by_key()["color"])

audio_file = glob("./*.wav")
y, sample_rate = librosa.load(audio_file[0], sr=None)

print("sample_rate: {}".format(sample_rate))
print(f'y: {y[10]}')
print(f'shape y: {y.shape}')

pd.Series(y).plot(figsize=(10.5))
