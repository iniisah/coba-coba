import random as rd 

angka = rd.randrange(0,100)
jumlah = 0

print("batas tebak emfat kali sjhh\n")
while True:
    masukan = int(input("berapa cuyy : "))
    jumlah +=1
    if jumlah == 4 :
        print("kalah luhk!")
        print(f"yang bener {angka} anjay")
        break
    if masukan > angka :
        print("kegedean")
    elif masukan < angka :
        print("kekecilan dah")
    elif masukan == angka :
        print("bener bejirr!")
        break  
