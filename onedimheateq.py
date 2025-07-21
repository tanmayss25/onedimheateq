from pandas import DataFrame
from numpy import array, ones

x = 1
t = 10

dx = 0.01
dt = 0.01

c = 1.9e-5

k = dt*c**2/dx**2

df = DataFrame()

t0 = 373.15
tSurr = 273.15

df['u0'] = tSurr*ones((1, int(x/dx)))[0]
df['u0'][0] = t0

for i in range(1, int(t/dt)):

    reqd_arr = df[f'u{i - 1}']

    current_arr = []
    current_arr.append(t0)
    
    for j in range(1, int(x/dx) - 1):

        cur_val = k*reqd_arr[j - 1] + (1 - 2*k)*reqd_arr[j] + k*reqd_arr[j + 1]
        current_arr.append(cur_val)

    current_arr.append(t0)

    df[f'u{i}'] = current_arr

df.to_csv('onedimheateqdata.csv')