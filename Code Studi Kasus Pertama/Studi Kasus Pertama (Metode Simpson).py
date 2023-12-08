from simpson import *
def v(t):
    return 3*t**2 + 4*t - 5

a = 0
b = 3
n = 100  

posisi = simpson(v, a, b, n)
print("Posisi mobil setelah t=3 detik:", posisi)
