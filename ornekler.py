"""
adet = 0
for i in range(1000):
    if i % 2 == 0 and i % 3 == 0:
        adet += 1
print(adet)
"""

"""
x = int(input("Birinci saıyı giriniz"))
y = int(input("ikinci saıyı giriniz"))
sonuc = 1
for a in range(y):
    sonuc *= x
print(sonuc)
"""
"""
tek_toplam = 0
cift_toplam = 0

for i in range(1,5000):
    if i % 2 == 0:
        cift_toplam += i
    else:
        tek_toplam += i
print("Tek sayılar toplamı",tek_toplam)
print("Çift sayılar toplamı", cift_toplam)
"""

"""
x = int(input("Birinci sayıyı giriniz"))
y = int(input("ikinci sayıyı giriniz"))
sonuc = 0
for a in range(y):
    sonuc += x
print(sonuc)
"""
"""
for a in range(1,11):
    for b in range(1,11):
        print(b,"*",a,"=",a*b,sep="", end=" ")
    print()
"""