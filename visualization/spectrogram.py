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
plt.subplot(2, 1, 1)
wave_plot = pd.Series(y).plot(figsize=(10, 5),
                              ax=plt.gca(),
                              lw=1,
                              title='Audio',
                              color=color_pal[0],
                              subplots=True)

spectrogram = librosa.stft(y)
spectrogram_db = librosa.amplitude_to_db(np.abs(spectrogram), ref=np.max)
spec_shape = spectrogram_db.shape

plt.subplot(2, 1, 2)
img = librosa.display.specshow(spectrogram_db)
plt.show()
