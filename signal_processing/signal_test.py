import numpy as np
import matplotlib.pyplot as plt
from wave import Wave

def main():
    sine_wave = Wave(440,1024,48000,1.0)
    fm_sine_wave = Wave(440,1024,48000,1.0)
    sine_values = sine_wave.create_sine()
    fm_sine_values = fm_sine_wave.create_fm_sine(10)
    xpoints = np.array(range(0, 1024))
    plt.plot(xpoints, sine_values, fm_sine_values )
    plt.xlabel("bla")
    plt.ylabel('sine and fm sine')
    plt.show()

if __name__ == "__main__":
    main()
