# =======================================================
# PYTHON DERS 8: MANTIKSAL DEĞERLER (bool)
# =======================================================

# Önceki derste metin ifadelerini öğrendik.
# Bu derste mantıksal değerleri (True/False) öğreneceğiz.

# Öğreneceğiniz konular:
#   - True ve False değerleri
#   - Karşılaştırma operatörleri
#   - Mantıksal operatörler (and, or, not)
#   - Boolean dönüşümleri
#   - Pratik uygulama örnekleri

print("Python Mantıksal Değerler Dersine Hoş Geldiniz!")


# =======================================================
# 1. TRUE VE FALSE DEĞERLERİ
# =======================================================
print("1. TRUE VE FALSE DEĞERLERİ")
print("----------------------------")

# Bool türünde sadece iki değer vardır: True ve False
# DİKKAT: İlk harfleri büyük yazılır!
dogru = True
yanlis = False

print("Doğru değer:", dogru)
print("Yanlış değer:", yanlis)

# type() ile türlerini kontrol edelim
print("dogru'nun türü:", type(dogru))
print("yanlis'ın türü:", type(yanlis))

#######################
# Karşılaştırma Operatörleri (True/False döner)
#######################

a = 10
b = 20

print(f"{a} == {b}  :", a == b)   # Eşit mi? False
print(f"{a} != {b}  :", a != b)   # Eşit değil mi? True
print(f"{a} > {b}   :", a > b)    # Büyük mü? False
print(f"{a} < {b}   :", a < b)    # Küçük mü? True
print(f"{a} >= {b}  :", a >= b)   # Büyük veya eşit mi? False
print(f"{a} <= {b}  :", a <= b)   # Küçük veya eşit mi? True

#######################
# Mantıksal Operatörler
#######################

x = True
y = False

# Doğru ve Yanlış : False
print(f"x and y   : {x and y}")   # False

# Doğru ya da Yanlış : True
print(f"x or y    : {x or y}")    # True

# not x: # x'in tersini alır | False
print(f"not x     : {not x}")     # False

# not y: # y'nin tersini alır | True
print(f"not y     : {not y}")     # True

#######################
# Koşullarda Boolean Kullanımı
#######################

sayi = 7

if sayi % 2 == 0:
    print(f"{sayi} çifttir. (bool: {sayi % 2 == 0})")
else:
    print(f"{sayi} tektir. (bool: {sayi % 2 == 0})")

sayi = 42 
if sayi > 0:
    if sayi % 2 == 0:
        print(f"{sayi} pozitif ve çifttir. (bool: {sayi > 0 and sayi % 2 == 0})")
    else:
        print(f"{sayi} pozitif ve tektir. (bool: {sayi > 0 and sayi % 2 == 0})")
else: 
    print(f"{sayi} negatif veya sıfırdır. (bool: {sayi > 0})")

#######################
# Boolean Fonksiyonları ve Dönüşümleri
#######################

print("bool(0)        :", bool(0))          # False
print("bool(1)        :", bool(1))          # True
print("bool('')       :", bool(''))         # False
print("bool('veri')   :", bool('veri'))     # True
print("bool([])       :", bool([]))         # False
print("bool([1, 2])   :", bool([1, 2]))     # True
print("bool(None)     :", bool(None))       # False