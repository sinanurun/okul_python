ogrenciler = ["Eren","Muhammed","Mert","Efe","Mert","Aytuğ"]
print(ogrenciler)

ogrenciler.append("Sinan")
print(ogrenciler)

yeni_ogrenciler = ["Ali","Veli"]
ogrenciler.extend(yeni_ogrenciler)
print(ogrenciler)
ogrenciler.insert(3,"Can")
print(ogrenciler)

ogrenciler.remove("Sinan")
print(ogrenciler)

ogrenciler.pop()
print(ogrenciler)

ogrenciler.pop(3)
print(ogrenciler)

print(ogrenciler.index('Mert'))

print(ogrenciler.count("Mert"))

ogrenciler.reverse()
print(ogrenciler)

ogrenciler.sort()
print(ogrenciler)

ogrenciler2 =  ogrenciler.copy()

print(ogrenciler2)
ogrenciler.append("Kamil")
print(ogrenciler2)
print(ogrenciler)
ogrenciler2.clear()
print(ogrenciler2)
del(ogrenciler2)
#print(ogrenciler2)
del(ogrenciler[2])
print(ogrenciler)
