# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:00:58 2026

@author: Acer
"""
#065002600013
#Ardie Arya Aditya
while True:
    print("Program File Handling\n 1. Mmebuat dan Menulis File\n 2. Membaca File\n 3. Menulis File\n 4. Keluar dari Program")
    choice = int(input("Masukan angka (1/2/3/4) : "))
    if choice == 1 :
        name = input("Masukan Nama File : ")
        file = open(f"{name}.txt", "w")
        nama = input("Masukan Nama : ")
        file.write(f"Nama :  {nama}\n")
        nim = input("Masukan NIM : ")
        file.write(f"Umur :  {nim}\n")
        tahun = input("Masukan Tahun Angkatan : ")
        file.write(f"Angkatan Tahun :  {tahun}\n")
        file.close()
        print("File Berhasil dibuat")
    
    elif choice == 2 :
        name = input("Masukan Nama File : ")
        file = open(f"{name}.txt", "r")
        text = file.read()
        print(text)
        file.close()
        
    elif choice == 3 :
        name = input("Masukan Nama File : ")
        file = open(f"{name}.txt", "a")
        vehicle = input("Masukan Kendaraan : ")
        file.write(f"Kendaraan : {vehicle}\n")
        maybe = input("Masukan Tipe Kendaraan (Mobil/Motor/Umum): ")
        file.write(f"Tipe Kendaraan : {maybe}\n")
        file.close()
        
    elif choice == 4 :
        print("Terimakasih Telah Menggunakan Program Ini")
        break
    else:
        print("masukan angka yang benar")
        break