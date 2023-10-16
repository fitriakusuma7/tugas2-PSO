# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:59:04 2023

@author: Asus
"""

#ID
print("Nama: Fitria Kusumaningrum")
print("NRP: 5009201044")

import numpy as np
import matplotlib.pyplot as plt

# Buat sinyal kotak dengan periode 2A dan amplitudo 1
# Parameter sinyal
A = 1  # Amplitudo
T = 2 * A  # Periode
duration = T  # Durasi sinyal
fs = 1000  # Frekuensi sampel (Hz)

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

# Melakukan FFT
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(3001)
magnitude = np.abs(fft_result)

# Plot sinyal
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Sinyal Asli')

# Plot spektrum frekuensi dari FFT
plt.subplot(2, 1, 2)
plt.plot(frequencies, magnitude)
plt.title('Spektrum Frekuensi (FFT)')
plt.xlabel('Frekuensi')
plt.ylabel('Amplitudo')

plt.tight_layout()
plt.show()
