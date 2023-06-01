import numpy as np
from dataclasses import dataclass


@dataclass
class Wave:
    frequency: int
    num_samples: int
    sampling_rate: int
    amplitude: float

    def create_sine(self) -> np.array:
        sine_wave = np.zeros((self.num_samples,), dtype=float)
        for x in range(self.num_samples):
            sine_wave[x] = np.sin(2 * np.pi * self.frequency * x/self.sampling_rate)
        return sine_wave
