isim = input("Adınızı Giriniz")
boy = float(input("Boyunuzu giriniz"))
kilo = int(input("kilonuzu giriniz"))
d_tarihi = int(input("Doğum yılınızı Giriniz"))
goz = input("Göz Rengini giriniz")
cocuk = [isim,boy,kilo,d_tarihi,goz]
print(cocuk)

print("Adınız :",cocuk[0],
      "Yaşınız :", 2021 - cocuk[3])
cocuk[3] = int(input("Doğum yılınızı Tekrar Giriniz"))

print(cocuk)

print("Adınız :",cocuk[0],
      "Yaşınız :", 2021 - cocuk[3])