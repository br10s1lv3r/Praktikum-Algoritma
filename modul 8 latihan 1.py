# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:23:01 2026

@author: Acer
"""
#ARDIE ARYA ADITYA
#065002600013
def input_dan_jumlah(n, i=1, total=0):
    if i > n:
        return total

    angka = int(input(f"Masukkan angka ke-{i}: "))

    return input_dan_jumlah(n, i + 1, total + angka)


def main():
    n = int(input("Masukkan Jumlah: "))
    hasil = input_dan_jumlah(n)
    print(f"Hasil penjumlahan: {hasil}")

main()
