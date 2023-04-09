import matplotlib.pyplot as plt
import numpy as np

# Define the function for the photoelectric equation
def photoelectric_eq(freq, work_func):
    h = 6.626e-34  # Planck's constant in J s
    return h*freq - work_func

# Define the frequency range and work function for the material
freq_range = np.linspace(0, 1e15, 1000)  # frequency range in Hz
work_func = 4.5  # work function in eV

# Calculate the kinetic energy for each frequency in the range
kinetic_energy = photoelectric_eq(freq_range, work_func*1.602e-19)/1.602e-19  # convert J to eV

# Plot the relationship between frequency and kinetic energy
plt.plot(freq_range, kinetic_energy)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Kinetic Energy (eV)')
plt.title('Photoelectric Equation')
plt.grid(True)
plt.show()
