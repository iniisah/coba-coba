import random as rd 

angka = rd.randrange(0,100)
jumlah = 0

print("***batas menebak 4 kali***\n")
while True:
    masukan = int(input("masukkan angka: "))
    jumlah +=1
    if jumlah == 4 :
        print("game over!")
        print(f"angkanya adalah {angka}")
        break
    if masukan > angka :
        print("terlalu besar")
    elif masukan < angka :
        print("terlalu kecil")
    elif masukan == angka :
        print("selamat tebakanmu benar!")
        break  
