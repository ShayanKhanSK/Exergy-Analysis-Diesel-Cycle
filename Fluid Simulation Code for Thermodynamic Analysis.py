import numpy as np
import matplotlib.pyplot as plt

nx = 50  # Number of grid points in the x-direction
ny = 50  # Number of grid points in the y-direction
nt = 100  # Number of time steps
nu = 0.1  # Viscosity
dt = 0.01  # Time step
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)

# Initialize velocity field
u = np.zeros((nx, ny))
v = np.zeros((nx, ny))

# Main simulation loop
for n in range(nt):
    un = u.copy()
    vn = v.copy()

    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            u[i, j] = (un[i, j] - 
                       un[i, j] * dt / dx * (un[i, j] - un[i-1, j]) - 
                       vn[i, j] * dt / dy * (un[i, j] - un[i, j-1]) + 
                       nu * (dt / dx**2 * (un[i+1, j] - 2*un[i, j] + un[i-1, j]) + 
                             dt / dy**2 * (un[i, j+1] - 2*un[i, j] + un[i, j-1])))

            v[i, j] = (vn[i, j] - 
                       un[i, j] * dt / dx * (vn[i, j] - vn[i-1, j]) - 
                       vn[i, j] * dt / dy * (vn[i, j] - vn[i, j-1]) + 
                       nu * (dt / dx**2 * (vn[i+1, j] - 2*vn[i, j] + vn[i-1, j]) + 
                             dt / dy**2 * (vn[i, j+1] - 2*vn[i, j] + vn[i, j-1])))
            kinetic_energy = 0.5 * (u**2 + v**2)

v = np.linspace(0, 2, nx)
u = np.linspace(0, 2, ny)
u, v = np.meshgrid(u, v)

# Plot the velocity field
plt.figure(figsize=(8, 6))
plt.quiver(u, v, u, v, scale=20, color='blue')
plt.title('2D Fluid Flow Simulation')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

plt.contourf(u, cmap='viridis')
plt.colorbar()
plt.title('Velocity Field (U)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)
X, Y = np.meshgrid(x, y)

plt.streamplot(x, y, u, v)
plt.title('Streamlines')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
