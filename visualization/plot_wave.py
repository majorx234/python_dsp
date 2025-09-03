import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

# file handling
from glob import glob

# audio stuff
import librosa
import librosa.display

sbn.set_theme(style="white", palette=None)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
# color_cycle = cycle(plt.rcParams["axes.prop_cycle"].by_key()["color"])

audio_file = glob("./*.wav")
y, sample_rate = librosa.load(audio_file[0], sr=None)

print("sample_rate: {}".format(sample_rate))
print(f'y: {y[10]}')
print(f'shape y: {y.shape}')


plt.figure(1)
plt.subplot(4, 1, 1)
wave_plot = pd.Series(y).plot(figsize=(10, 5),
                              ax=plt.gca(),
                              lw=1,
                              title='Audio',
                              color=color_pal[0],
                              subplots=True)


y_trimmed, _ = librosa.effects.trim(y, top_db=17)
plt.subplot(4, 1, 2)
wave_trimmed_plot = pd.Series(y_trimmed).plot(figsize=(10, 5),
                                              ax=plt.gca(),
                                              lw=1,
                                              title='Audio trimmed',
                                              color=color_pal[0],
                                              subplots=True)

plt.subplot(4, 1, 3)
wave_zoomed_plot = pd.Series(y[0:1000]).plot(figsize=(10, 5),
                                             lw=1,
                                             title='Audio zoomed',
                                             ax=plt.gca(),
                                             color=color_pal[0],
                                             subplots=True)
plt.subplot(4, 1, 4)
wave_trimmed_zoomed_plot = pd.Series(y_trimmed[0:1000]).plot(figsize=(10, 5),
                                                             lw=1,
                                                             title='Audio trimmed zoomed',
                                                             ax=plt.gca(),
                                                             color=color_pal[0],
                                                             subplots=True)
plt.show()
