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


def mix_signals(signals: [np.array]) -> np.array:
    num_signals = len(signals)
    num_samples = signals[0].size
    mixed_signal = np.zeros((num_samples,), dtype=float)

    for sample_idx in range(0,num_samples):
        sum_sample: float = 0.0
        mul_sample: float = 1.0
        for sign_idx in range(0,num_signals):
            sum_sample += signals[sign_idx][sample_idx]
            mul_sample *= signals[sign_idx][sample_idx]
        mixed_signal[sample_idx] = sum_sample - mul_sample * num_signals
    return mixed_signal
