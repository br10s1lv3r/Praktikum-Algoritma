# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:30:15 2026

@author: Acer
"""
#ARDIE ARYA ADITYA
#065002600013
def angka_prima(angka):
    if angka <= 1 :
        return False
    for i in range(2, angka):
        if angka % i == 0:
            return False
        return True
    
def tampil_prima(angka):
    if angka_prima(angka):
        print(f"{angka} adalah bilangan Prima")
    else:
        print(f"{angka} adalah bukan bilangan Prima")
        
input_angka = int(input("Masukan angka : "))
tampil_prima(input_angka)
