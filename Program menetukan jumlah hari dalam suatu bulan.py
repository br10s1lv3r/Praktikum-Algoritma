# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 07:25:47 2026

@author: Acer
"""

# ARDIE ARYA ADITYA
# 065002600013
day = str("")
bulan = int(input("Masukkan bulan (1-12): "))
while bulan < 1 or bulan > 12:
    print("Bulan tidak valid! Masukkan angka 1 sampai 12.")
    bulan = int(input("Masukkan bulan (1-12): "))

tahun = int(input("Masukkan tahun: "))
while tahun < 1:
    print("Tahun tidak valid! Masukkan tahun lebih dari 0.")
    tahun = int(input("Masukkan tahun: "))
if bulan == 1:
    day = "Januari"
elif bulan == 2:
    day = "Februari"
elif bulan == 3:
    day = "Maret"
elif bulan == 4:
    day = "April"
elif bulan == 5:
    day = "Mei"
elif bulan == 6:
    day = "Juni"
elif bulan == 7:
    day = "Juli"
elif bulan == 8:
    day = "Agustus"
elif bulan == 9:
    day = "September"
elif bulan == 10:
    day = "Oktober"
elif bulan == 11:
    day = "November"
elif bulan == 12:
    day = "Desember"    
    
if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
    hari = 31
elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
    hari = 30
else:
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        hari = 29
    else:
        hari = 28

print("Jumlah hari pada bulan", bulan,"(",day,")" "tahun", tahun, "adalah", hari, "hari.")