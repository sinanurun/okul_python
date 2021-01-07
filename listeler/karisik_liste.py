import random

ogrenciler = ["Eren","Muhammed","Mert","Efe","Mert","Aytuğ"]
print(ogrenciler)

uzunluk = len(ogrenciler)

rastgele = random.randint(0,uzunluk-1)
print(rastgele)
print(ogrenciler[rastgele])