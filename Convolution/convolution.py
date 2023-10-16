# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:52:35 2023

@author: Asus
"""

#ID
print("Nama: Fitria Kusumaningrum")
print("NRP: 5009201044")

def konvolusi(sig1, sig2):
    # First signal
    signal1 = len(sig1)
    # Second signal 
    signal2 = len(sig2)

    result = [0] * (signal1 + signal2 + 2)
    # Konvolusi
    for a in range(signal1):
        for b in range(signal2):
            result[a + b] += sig1[a]*sig2[b]
    
    return result
        

sinyal1 = [1,2,3]
sinyal2 = [4,5,6]

hasil = konvolusi(sinyal1, sinyal2)
print(hasil)




