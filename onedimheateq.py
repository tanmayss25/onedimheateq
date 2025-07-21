from numpy import ones
import matplotlib.pyplot as plt
import seaborn as sns

x = 0.01
t = 10

dx = 0.01
dt = 0.01

c = 0.0025

k = dt*c**2/dx**2

nx = int(x/dx)
nt = int(t/dt)

t0 = 373.15
tSurr = 273.15

heat_array = tSurr*ones((nx, nt))

heat_array[0] = t0*ones((1, nt))[0]
heat_array[-1] = tSurr*ones((1, nt))[0]

for i in range(nx - 1):
    for j in range(nt - 1):

        heat_array[i][j + 1] = k*heat_array[i - 1][j] + (1 - 2*k)*heat_array[i][j] + k*heat_array[i + 1][j]
    
    heat_array[0] = t0*ones((1, nt))[0]
    heat_array[-1] = tSurr*ones((1, nt))[0]

colors = ["blue", "green", "yellow", "red"]
custom_cmap = plt.cm.colors.LinearSegmentedColormap.from_list("BGYR", colors)

plt.figure(figsize = (6,6))
sns.heatmap(heat_array, cmap = custom_cmap, cbar = True, cbar_kws = {'label':'Temperature (K)'})
plt.title('Temperature Distribution vs Time')
plt.xlabel('Time')
plt.ylabel('x')
plt.show()