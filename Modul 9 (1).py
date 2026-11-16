# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:04:46 2026

@author: Acer
"""
#065002600013
#Ardie Arya Aditya
print("Masukan Data Kamu Dibawah")
file = open("Test.txt", "w")
nama = input("Masukan Nama : ")
file.write(f"Nama :  {nama}\n")
umur = input("Masukan Umur : ")
file.write(f"Umur :  {umur}\n")
alamat = input("Masukan Alamat : ")
file.write(f"Alamat :  {alamat}\n")
email = input("Masukan E-mail : ")
file.write(f"E-mail :  {email}\n")
dosen = input("Masukan Dosen Wali : ")
file.write(f"Dosen Wali :  {dosen}\n")
file.close()

print("Ini Data Kamu")
file = open("Test.txt", "r")
text = file.read()
print(text)
file.close()