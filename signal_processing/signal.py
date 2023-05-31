import numpy as np
from dataclasses import dataclass
import matplotlib.pyplot as plt

@dataclass
class signal:
    frequency: int
    num_samples: int
    sampling_rate: int
    amplitude: float

    def create_sine(self) -> np.array:
        sine_wave = np.zeros((num_samples,), dtype=float)
        for x in range(num_samples):
            sine_wave[x] = np.sin(2 * np.pi * self.frequency * x/self.sampling_rate)
        return sine_wave
