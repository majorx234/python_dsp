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

def create_magnitude_from_filter_coeffs(filter_coeffs,s):
    (num_coeffs, den_coeffs) = filter_coeffs
    num_coeffs_len = num_coeffs.size
    den_coeffs_len = den_coeffs.size

    num = 0;
    for i in range(0, num_coeffs_len):
        num += num_coeffs[i]* np.power(s, num_coeffs_len - i)

    den = 0;
    for i in range(0, den_coeffs_len):
        den += den_coeffs[i]* np.power(s, den_coeffs_len - i)

    return num/den


def main():
    magnitude_samples = np.ones(64)
    (impulse_response, magnitude_response, phase_response) = create_fir_from_magnitude(magnitude_samples)
    print(impulse_response)

if __name__ == "__main__":
    main()
