# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:10:56 2026

@author: Acer
"""
#ARDIE ARYA ADITYA
#065002600013
def ordinal(n):
    """Mengubah angka menjadi ordinal berdasarkan digit terakhir."""
    n = int(n)
    digit = n % 10
    if digit == 1:
        suffix = "st"
    elif digit == 2:
        suffix = "nd"
    elif digit == 3:
        suffix = "rd"
    else:
        suffix = "th"
    return f"{n}{suffix}"


while True:
    try:
        user_input = input(">>")
        print(f">>{ordinal(user_input)}")
    except ValueError:
        print("Input tidak valid, masukkan angka.")
    except (EOFError, KeyboardInterrupt):
        print("\nProgram selesai.")
        break