import numpy as np
import matplotlib.pyplot as plt

# Generate a signal with 1000 data points
t = np.linspace(-1, 1, 1000)
signal = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 10 * t)

# Compute the Fourier transform
frequencies = np.fft.fftfreq(signal.size, t[1] - t[0])
fourier = np.fft.fft(signal)

# Plot the signal in the time domain
plt.subplot(211)
plt.plot(t, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Signal in the Time Domain')

# Plot the Fourier transform in the frequency domain
plt.subplot(212)
plt.plot(frequencies, np.abs(fourier))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Fourier Transform of the Signal')

# Show the plot
plt.tight_layout()
plt.show()
