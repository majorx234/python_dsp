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

    def create_fm_sine(self, freq_fm) -> np.array:
        fm_sine = np.zeros((self.num_samples,), dtype=float)

def limit_signal(signal: np.array, max: float = 1.0, min: float = -1.0) -> np.array:
    limit_signal = np.zeros((signal.size,), dtype=float)
    for idx in range(0,signal.size):
        sample = signal[idx]
        if sample > max:
            sample = max
        if sample < min:
            sample = min
        limit_signal[idx] = sample
    return limit_signal

def generate_white_noise(nsamples: int) -> np.array:
    mean = 0.0
    scale = 1.0
    noise_signal = np.zeros((nsamples,), dtype=float)
    for idx in range(0,nsamples):
        noise_signal[idx] = np.random.normal(mean,scale)
    return noise_signal
