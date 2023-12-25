def toplama(a,b):
    return a+b
def cikarma(c,d):
    return c-d
def carpma(e,f):
    return e*f

a = int(input("Toplamak istediğiniz ilk sayıyı girin: "))
b = int(input("Toplamak istediğiniz ikinci sayıyı girin: "))
sonuc_toplama=toplama(a,b)
print(f"{a} + {b} = {sonuc_toplama}")


c = int(input("Çıkarmak istediğiniz ilk sayıyı girin: "))
d = int(input("Çıkarmal istediğiniz ikinci sayıyı girin: "))
sonuc_cikarma=cikarma(c,d)
print(f"{c} - {d} = {sonuc_cikarma}")

e = int(input("Çarpmak istediğiniz ilk sayıyı girin: "))
f = int(input("Çarpmak istediğiniz ikinci sayıyı girin: "))
sonuc_carpma=carpma(e,f)
print(f"{e} * {f} = {sonuc_carpma}")

list=[sonuc_toplama,sonuc_cikarma,sonuc_carpma]
print(f"sonuclar = {list}")

sirali_list=sorted(list)
print(f"sıralı sonuclar = {sirali_list}")

