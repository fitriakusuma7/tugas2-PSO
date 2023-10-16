# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:42:31 2023

@author: Asus
"""

#ID
print("Nama: Fitria Kusumaningrum")
print("NRP: 5009201044")

import math
import matplotlib.pyplot as plt

# Fungsi untuk menghitung FFT manual
def manual_fft(signal):
    N = len(signal)
    fft_result = [0j] * N  # Inisialisasi array kompleks untuk menyimpan hasil FFT

    for k in range(N):
        sum_real = 0
        sum_imag = 0
        for n in range(N):
            angle = 2 * math.pi * k * n / N
            sum_real += signal[n] * math.cos(angle)
            sum_imag += -signal[n] * math.sin(angle)
        fft_result[k] = complex(sum_real, sum_imag)

    return fft_result

# Buat sinyal kotak dengan periode 2A dan amplitudo 1
# Parameter sinyal
A = 1  # Amplitudo
T = A  # Periode
duration = T  # Durasi sinyal
fs = 500  # Frekuensi sampel (Hz)

# Inisialisasi list untuk menyimpan sinyal
t = []
signal = []

# Waktu
t_step = 1 / fs
t_current = -1

# Membuat sinyal kotak
while t_current < duration:
    t.append(t_current)
    if 0 <= t_current % T < T / 2:
        signal.append(1)
    else:
        signal.append(0)
    t_current += t_step

# Plot sinyal kotak
plt.figure(figsize=(10, 4))
plt.plot(t, signal, lw=2)
plt.title('Sinyal Kotak Periode 2A dan Amplitudo 1')
plt.xlabel('Waktu')
plt.ylabel('Amplitudo')
plt.grid(True)
plt.ylim(-0.2, 1.2)
plt.show()

# Hitung FFT manual
fft_result = manual_fft(signal)

# Plot sinyal asli
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Sinyal Kotak')

# Plot spektrum frekuensi dari FFT
plt.subplot(2, 1, 2)
frequency = [k / T for k in range(2000)]
magnitude = [abs(x) for x in fft_result]
plt.plot(frequency, magnitude)
plt.title('Spektrum Frekuensi (FFT)')
plt.xlabel('Frekuensi')
plt.ylabel('Amplitudo')

plt.tight_layout()
plt.show()
