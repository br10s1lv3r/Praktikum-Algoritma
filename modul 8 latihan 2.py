# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:57:01 2026

@author: Acer
"""
#ARDIE ARYA ADITYA
#065002600013
def pangkat(base, power):
    if power == 0:
        return 1
    elif power < 0:
        return 1 / pangkat(base, -power)
    else:
        return base * pangkat(base, power - 1)

base  = float(input("Masukkan angka : "))
power = int(input("Masukkan pangkat: "))

hasil = pangkat(base, power)
print(f"Hasil {base} pangkat {power} = {hasil}")
