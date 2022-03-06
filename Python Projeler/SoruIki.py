### Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

def DiziyiTersDöndürenFonksiyon(num):
    print(f" Lütfen {num} adet sayı giriniz ")
    arr= list()
    for i in range(0,num):
        item = input(f"{i+1}. sayıyı giriniz: \n ")
        arr.append(item)
    print(f"Yazı Sırasına Göre Dizi: {arr} ")
    r = list(reversed(arr))
    print(f"Dizinin Ters Hali: {r} ")

print(DiziyiTersDöndürenFonksiyon(3))
    








