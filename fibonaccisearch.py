# NAMA: MUTHMAINNAH AISYAH
# NIM: 2209116001
# KELAS: A -2022

# FIBONACCI SEARCH

import os
os.system("cls")

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

def fibonaccisearch(data, x): # mendefinisikan fungsi
    n = len(data) # panjang data
    # inisialisasi nomor fibonacci
    f2 = 0 
    f1 = 1 
    f = f2 + f1
    # mencari nilai f yang akan menyimpan nomor fibonacci yang terkecil yang lebih besar atau sama dengan n
    while (f < n): # ketika f lebih kecil dari n
        f2 = f1
        f1 = f
        f = f2 + f1
    # index awal untuk pencarian
    offset = -1
    # mencari nilai fibonacci
    while (f > n): # ketika f lebih besar dari n
        i = min(offset+f2, n-1)
        # jika x lebih dari nilai elemen pada index i, pencarian dilakukan pada subarray kanan
        if (data[i] < x):
            f = f1
            f1 = f2
            f2 = f - f1
            offset = i
        # jika x kurang dari nilai elemen pada index i, pencarian dilakukan pada subarray kiri
        elif (data[i] > x):
            f = f2
            f1 = f1 - f2
            f2 = f - f1
        # jika elemen ditemukan, return index
        else:
            return i
    # membandingkan elemen terakhir dengan x
    if (f1 and data[offset+1] == x):
        return offset+1
    # jika elemen tidak ditemukan, return -1
    return -1

def search():
    while True:
        print(var)
        print(47*"=")
        cari = str(input("Masukkan Nama Yang Ingin Dicari: ")) # inputan mencari nama
        for i in range(len(var)): # perulangan for dari panjang data list
            search = fibonaccisearch(var[i], cari) 
            if type(var[i]) == list: # jika tipe data var adalah list
                print(47*"=")
                print("Hasil Pencarian: \n")
                print(cari, "berada di array index ke -", i, "kolom", search)
                print(47*"=")
                return
            else:
                if var[i] == cari: # jika cari terdapat dalam var
                    print(47*"=")
                    print("Hasil Pencarian: \n")
                    print(cari, "berada di array index ke -", i)
                    print(47*"=")
                    return

def lanjut():
    while True:
        tanya = input("Apakah Anda Ingin Lanjut mencari (y/n)? ")
        if tanya == "y": # jika y, maka akan kembali ke fungsi search
            os.system("cls")
            search()
        elif tanya == "n": # jika n, maka program akan berhenti
            os.system("cls")
            exit()
        else:
            print("Masukkan dengan benar!")

# pemanggilan fungsi
search()
lanjut()
