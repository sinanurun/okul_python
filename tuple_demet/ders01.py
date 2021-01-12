ogrenci = (95,"Efe","Sesliçan","9/A")
print(ogrenci)
print(type(ogrenci))
print(ogrenci[0])

print(ogrenci[:2])
print(ogrenci[::-1])

yeni_liste = list(ogrenci)
print(yeni_liste)

yeni_liste.append("Bilişim Bölümü")

ogrenci = tuple(yeni_liste)
print(ogrenci)