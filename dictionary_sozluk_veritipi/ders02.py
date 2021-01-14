# ogrenciler = {2249:["Muhammed","KAPLAN","Bilişim","Erkek"],
#               2389:["Eren","DAĞLI","Elektronik","Erkek"]
#               }
#
# print(ogrenciler)
# print(ogrenciler[2249])
# print(ogrenciler[2389])
# print(ogrenciler[2249][0])
# print(ogrenciler[2389][0])

ogrenciler = {2249:{"isim":"Muhammed","soyisim":"KAPLAN","bolum":"Bilişim"},
              2389:{"isim":"Eren","soyisim":"DAĞLI"}}

print(ogrenciler[2249]["isim"])
print(ogrenciler[2389]["soyisim"])
print(len(ogrenciler))
print(len(ogrenciler[2249]))