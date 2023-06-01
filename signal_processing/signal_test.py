import numpy as np
import matplotlib.pyplot as plt
from wave import Wave

def main():
    sine_wave = Wave(440,1024,48000,1.0)
    my_values = sine_wave.create_sine()
    xpoints = np.array(range(0, 1024))
    plt.plot(xpoints, my_values )
    plt.xlabel("bla")
    plt.ylabel('sine signal')
    plt.show()

if __name__ == "__main__":
    main()
