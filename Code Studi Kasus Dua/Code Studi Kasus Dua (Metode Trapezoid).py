def a(t):
    return (4*t - 2)**2  # Persamaan percepatan a(t)

def trapezoid(f, a, b, n):
    h = (b - a) / n
    sum_val = 0.0

    for i in range(1, n):
        x = a + i * h
        sum_val += f(x)

    integral = (h / 2) * (f(a) + 2 * sum_val + f(b))
    return integral

# Kecepatan awal
v0 = 3  # m/s

# Batas waktu
t0 = 0
t1 = 2  # Misalkan kita ingin mengetahui kecepatan pada t = 2 detik

# Jumlah segmen, dapat disesuaikan sesuai kebutuhan
n = 100  

# Hitung kecepatan menggunakan metode trapesium
kecepatan = v0 + trapezoid(a, t0, t1, n)
print(f"Kecepatan pada t={t1} detik:", kecepatan, "m/s")
