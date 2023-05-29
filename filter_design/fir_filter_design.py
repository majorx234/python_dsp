import numpy as np


def create_fir_from_magnitude(magnitude_samples):
    nsamples = magnitude_samples.size
    response = np.zeros((nsamples,), dtype=complex)
    for idx in range(0,int(np.floor((nsamples-1)/2))):
        response[idx] = magnitude_samples[idx] * np.exp(-1j*2*np.pi/nsamples*idx*(nsamples-1)/2 )
        response[nsamples-idx-1] = np.conjugate(response[idx])

    if nsamples % 2 == 0:
        response[int(nsamples/2+1)] = magnitude_samples[int(nsamples/2+1)]

    magnitude_response = np.absolute(response)
    phase_response = np.angle(response)
    impulse_response = np.fft.ifft(response)
    return (impulse_response, magnitude_response, phase_response)


def main():
    magnitude_samples = np.ones(64)
    (impulse_response, magnitude_response, phase_response) = create_fir_from_magnitude(magnitude_samples)
    print(impulse_response)

if __name__ == "__main__":
    main()
