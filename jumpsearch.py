# NAMA: MUTHMAINNAH AISYAH
# NIM: 2209116001
# KELAS: A -2022

# JUMP SEARCH

import os
os.system("cls")

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

def jumpsearch(data, x): #mendefinisikan fungsi
    a = len(data) # panjang data
    step = int(a**0.5) # jarak lompatan/langkah
    # melakukan pencarian blok tempat elemen berada
    prev = 0 
    while data[min(step, a) - 1] < x:
        prev = step
        step += int(a**0.5) # jarak lompatan diperkecil
        # jika prev lebih besar sama dengan panjang data
        if prev >= a:
            return -1
    # melakukan pencarian linear untuk mencari x
    # blok dimulai dengan prev
    while data[prev] < x:
        prev += 1
        # jika mencapai blok selanjutnya atau akhir blok dari array, elemen tidak ada
        if prev == min(step,a):
            return -1
    # jika elemen telah ditemukan
    if data[prev] == x:
        return prev
    # jika elemen tidak ditemukan, return -1
    return -1

def search():
    while True:
        print(var)
        print(47*"=")
        cari = str(input("Masukkan Nama Yang Ingin Dicari: ")) # inputan mencari nama
        for i in range(len(var)): # perulangan for dari panjang data list
            search = jumpsearch(var[i], cari) 
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
