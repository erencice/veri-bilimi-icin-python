# =======================================================
# PYTHON DERS 1: TEMEL MATEMATİKSEL OPERATÖRLER
# =======================================================

# Merhaba! Python öğrenmeye başlıyorsunuz.
# Bu dosyada matematikte kullandığınız temel işlemleri 
# Python'da nasıl yapacağınızı öğreneceksiniz.

# Öğreneceğiniz konular:
#   - Toplama işlemi (+)
#   - Çıkarma işlemi (-)
#   - Çarpma işlemi (*)
#   - Bölme işlemi (/)
#   - Tam sayı bölmesi (//)
#   - Kalan bulma (%)
#   - Üs alma (**)
#   - İşaret değiştirme (-)
#   - İşlem önceliği

# print() fonksiyonu ekrana sonuç yazdırmaya yarar.
# Python'da değişken isimleri Türkçe karakter içeremez.

print("Python Matematik Dersine Hoş Geldiniz!")


# =======================================================
# 1. TOPLAMA İŞLEMİ (+)
# =======================================================
print("1. TOPLAMA İŞLEMİ")
print("------------------")
# Tam sayılarla toplama
a = 14 
b = 15 
print(a + b)

# Ondalıklı sayılarla toplama
i = 3.1
j = 4.8 
print(i + j)

# Doğrudan sayılarla toplama
print(3.1 + 4.8)

print("Toplama işlemi tamamlandı!")


# =======================================================
# 2. ÇIKARMA İŞLEMİ (-)
# =======================================================
print("2. ÇIKARMA İŞLEMİ")
print("------------------")

# Çoklu çıkarma
a = 28 
b = 35
c = 40
print(a - b - c)

# Negatif sayılarla çıkarma
t = -1
y = 5 
print(t - y)

# Ondalıklı sayılarla çıkarma
k = 3.1
l = 5.8
print(k - l)

print("Çıkarma işlemi tamamlandı!")


# =======================================================
# 3. ÇARPMA İŞLEMİ (*)
# =======================================================
print("3. ÇARPMA İŞLEMİ")
print("------------------")

# Tam sayılarla çarpma
a = 4
b = 5
print(a * b)

# Ondalıklı sayılarla çarpma
i = 3.14
j = 4.5
print(i * j)

# Üç sayının çarpımı
a = 3
b = 4
c = 5
print(a * b * c)

# Farklı türde sayılarla çarpma
a = 3 
b = 3.14
print(a * b)

print("Çarpma işlemi tamamlandı!")


# =======================================================
# 4. BÖLME İŞLEMİ (/)
# =======================================================
print("4. BÖLME İŞLEMİ")
print("----------------")

print(4 / 2)
print(10 / 3)
print(22 / 7)

# ÖNEMLİ NOT: 
# Python 3'te bölme işlemi (/) her zaman ondalıklı sonuç verir.
# Örneğin 4/2 = 2.0 olur (2 değil!)
# Bu daha kesin sonuçlar elde etmemizi sağlar.

print("Bölme işlemi tamamlandı!")


# =======================================================
# 5. TAM SAYI BÖLMESİ (//)
# =======================================================
print("5. TAM SAYI BÖLMESİ")
print("--------------------")

print(4 // 2)     # 2
print(13 // 4)    # 3 (13÷4=3.25, tam kısmı 3)
print(22 // 7)    # 3 (22÷7=3.14, tam kısmı 3)
print(40 // 7)    # 5 (40÷7=5.71, tam kısmı 5)

print("Tam sayı bölmesi tamamlandı!")


# =======================================================
# 6. KALAN BULMA - MOD (%)
# =======================================================
print("6. KALAN BULMA")
print("---------------")

print(13 % 4)     # 1 (13÷4=3 kalan 1)
print(14 % 2)     # 0 (14÷2=7 kalan 0)
print(330 % 111)  # 108

print("Kalan bulma işlemi tamamlandı!")


# =======================================================
# 7. ÜS ALMA (**)
# =======================================================
print("7. ÜS ALMA")
print("-----------")

# Üs alma işlemi
print(4 ** 3)     # 4³ = 64
print(2 ** 4)     # 2⁴ = 16
print(3.14 ** 3)  # π³

# Karekök nasıl bulunur?
# Matematikten bildiğimiz gibi karekök = sayının 0.5 kuvveti
print(64 ** 0.5)  # 64'ün karekökü = 8
print(25 ** 0.5)  # 25'in karekökü = 5

print("Üs alma işlemi tamamlandı!")


# =======================================================
# 8. İŞARET DEĞİŞTİRME (-)
# =======================================================
print("8. İŞARET DEĞİŞTİRME")
print("---------------------")

a = 4
print(-a)    # -4

b = -13
print(-b)    # 13

print("İşaret değiştirme tamamlandı!")


# =======================================================
# 9. İŞLEM ÖNCELİĞİ ve PARANTEZ
# =======================================================
print("9. İŞLEM ÖNCELİĞİ")
print("------------------")

# İşlem öncelik kuralları:
# 1. Parantez içi önce yapılır
# 2. Üs alma (**)
# 3. Çarpma (*) ve Bölme (/, //, %)
# 4. Toplama (+) ve Çıkarma (-)
# 5. Aynı öncelikli işlemler soldan sağa yapılır

print(8 + 4 * 3 / 2 - 18)
print(8 + ((4 * 3) / 2) - 18)

# Parantez kullanımı
print((8 + 4) * 3 / (2 - 18))

print("İşlem önceliği konusu tamamlandı!")

print("TÜM MATEMATIK İŞLEMLERİ TAMAMLANDI!")
print("Sonraki ders: Veri türlerini öğreneceğiz.")