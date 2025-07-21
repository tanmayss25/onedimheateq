from numpy import ones

x = 1
t = 10

dx = 0.01
dt = 0.01

c = 1.9e-5

k = dt*c**2/dx**2

nx = int(x/dx)
nt = int(t/dt)

heat_array = 273.15*ones((nx, nt))

heat_array[0] = 373.15*ones((1, nt))[0]
heat_array[-1] = 373.15*ones((1, nt))[0]

for i in range(nx - 1):
    for j in range(nt - 1):

        heat_array[i][j + 1] = k*heat_array[i - 1][j] + (1 - 2*k)*heat_array[i][j] + k*heat_array[i + 1][j]
    
    heat_array[0] = 373.15*ones((1, nt))[0]
    heat_array[-1] = 373.15*ones((1, nt))[0]

    