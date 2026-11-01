# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 23:17:33 2026

@author: Acer
"""
#ARDIE ARYA ADITYA
#065002600013
def harga_tiket(age):
    if age <= 2:
        return 0.0
    elif age <= 12:
        return 14.0
    elif age <= 64:
        return 23.0
    elif age >= 65:
        return 18.0

def beli_tiket():
    total = 0.0
    while True:
        umur = input("Masukan umur (langsung enter untuk selesai): ")
        if umur == "":
           break
        try:
            age = int(umur)
        except ValueError:
            print("harus berupa angka")
            continue

        harga = harga_tiket(age)
        total += harga
        
        if harga == 0.0:
            print("Gratis")
        else:
            print(f"Harga Tiket : {harga}")
            print(f"Total Harga : {total}")
   
    print(f"Total Harga : {total}")
    bayar = float(input("Masukan jumlah pembayaran : "))
    kembalian = bayar - total
    print(f"Jumlah kembalian : {kembalian}")
beli_tiket()