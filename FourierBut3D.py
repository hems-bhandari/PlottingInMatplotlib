import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a meshgrid of x and y values
N = 101
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)

# Evaluate the 2D Gaussian function
sigma = 1
Z = np.exp(-0.5*(X**2 + Y**2) / sigma**2)

# Compute the 3D Fourier transform
Z_fft = np.fft.fftn(Z)
Z_fft_shift = np.fft.fftshift(Z_fft)
Z_fft_shift_norm = np.abs(Z_fft_shift)**2 / (N**2)

# Create a 3D plot of the Fourier transform
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 0.2])
ax.set_xlabel('u')
ax.set_ylabel('v')
ax.set_zlabel('|F(u,v)|^2')
ax.set_title('3D Fourier Transform of a 2D Gaussian Function')

# Create a meshgrid of u and v values
u = np.linspace(-1, 1, N)
v = np.linspace(-1, 1, N)
U, V = np.meshgrid(u, v)

# Plot the Fourier transform
ax.plot_surface(U, V, Z_fft_shift_norm, cmap='jet')

# Show the plot
plt.show()
