# =======================================================
# PYTHON DERS 6: ONDALIKLI SAYILAR (float)
# =======================================================

# Önceki derste tam sayılarla ileri işlemler öğrendik.
# Bu derste ondalıklı sayılarla çalışmayı öğreneceğiz.

# Öğreneceğiniz konular:
#   - Ondalıklı sayı özellikleri
#   - Float sayılarla matematiksel işlemler
#   - Hassasiyet ve yuvarlama
#   - Pratik uygulama örnekleri

print("Python Ondalıklı Sayılar Dersine Hoş Geldiniz!")


# =======================================================
# 1. ONDALIKLI SAYI ÖZELLİKLERİ  
# =======================================================
print("1. ONDALIKLI SAYI ÖZELLİKLERİ")
print("------------------------------")

# Ondalıklı sayılar nokta ile yazılır
pi = 3.14159
yukseklik = 175.5
sicaklik = -5.2
sifir_float = 0.0

print("Pi sayısı:", pi)
print("Yükseklik:", yukseklik)
print("Sıcaklık:", sicaklik)
print("Sıfır (float):", sifir_float)

# type() ile türlerini kontrol edelim
print("pi'nin türü:", type(pi))
print("yukseklik'in türü:", type(yukseklik))
print("sifir_float'ın türü:", type(sifir_float))

print("Ondalıklı sayı özellikleri tamamlandı!")


# =======================================================
# 2. FLOAT SAYILARLA MATEMATİKSEL İŞLEMLER
# =======================================================
print("2. FLOAT SAYILARLA MATEMATİKSEL İŞLEMLER")
print("------------------------------------------")

a = 5.5
b = 2.0

print("İlk sayı:", a)
print("İkinci sayı:", b)
print()

print("Toplama:", a + b)        # 7.5
print("Çıkarma:", a - b)        # 3.5
print("Çarpma:", a * b)         # 11.0
print("Bölme:", a / b)          # 2.75

# Tam sayı bölmesi float sayılarda da çalışır
print("Tam sayı bölmesi:", a // b)  # 2.0 (sonuç float ama tam kısım)

# Mod işlemi float sayılarda da çalışır
print("Kalan:", a % b)          # 1.5

# Üs alma
print("Üs alma:", a ** b)       # 30.25

print("Float sayılarla işlemler tamamlandı!")


# =======================================================
# 3. TAM SAYI VE FLOAT KARIŞIMI
# =======================================================
print("3. TAM SAYI VE FLOAT KARIŞIMI")
print("------------------------------")

tam_sayi = 10
ondalik_sayi = 3.5

print("Tam sayı:", tam_sayi, "- Türü:", type(tam_sayi))
print("Ondalıklı sayı:", ondalik_sayi, "- Türü:", type(ondalik_sayi))
print()

# Tam sayı + Float = Float
sonuc1 = tam_sayi + ondalik_sayi
print("10 + 3.5 =", sonuc1, "- Türü:", type(sonuc1))

# Tam sayı * Float = Float  
sonuc2 = tam_sayi * ondalik_sayi
print("10 * 3.5 =", sonuc2, "- Türü:", type(sonuc2))

# Tam sayı / Tam sayı = Float
sonuc3 = 15 / 3
print("15 / 3 =", sonuc3, "- Türü:", type(sonuc3))

print("Karışık işlemler tamamlandı!")


# =======================================================
# 4. YUVARLAMA İŞLEMLERİ
# =======================================================
print("4. YUVARLAMA İŞLEMLERİ")
print("-----------------------")

uzun_sayi = 3.1415926535

# round() fonksiyonu ile yuvarlama
print("Orijinal sayı:", uzun_sayi)
print("Tam sayıya yuvarlama:", round(uzun_sayi))
print("1 ondalığa yuvarlama:", round(uzun_sayi, 1))
print("2 ondalığa yuvarlama:", round(uzun_sayi, 2))
print("3 ondalığa yuvarlama:", round(uzun_sayi, 3))

# int() fonksiyonu ondalık kısmı atar (yuvarlamaz!)
print("int() ile dönüşüm:", int(uzun_sayi))  # 3

print("Yuvarlama işlemleri tamamlandı!")


# =======================================================
# 5. PRATİK UYGULAMALAR
# =======================================================
print("5. PRATİK UYGULAMALAR")
print("----------------------")

# Uygulama 1: Boy-kilo indeksi (BMI) hesaplama
boy_cm = 175
kilo = 70
boy_m = boy_cm / 100  # cm'yi metreye çevir
bmi = kilo / (boy_m * boy_m)

print("Boy (cm):", boy_cm)
print("Kilo (kg):", kilo)
print("Boy (m):", boy_m)
print("BMI:", round(bmi, 2))

# Uygulama 2: Daire alanı hesaplama
pi = 3.14159
yaricap = 5.0
alan = pi * yaricap * yaricap

print("Yarıçap:", yaricap)
print("Daire alanı:", round(alan, 2))

# Uygulama 3: Sıcaklık dönüşümü (Celsius'tan Fahrenheit'e)
celsius = 23.5
fahrenheit = celsius * 9 / 5 + 32

print("Celsius:", celsius)
print("Fahrenheit:", round(fahrenheit, 1))

# Uygulama 4: Ortalama hesaplama
not1 = 85.5
not2 = 92.0  
not3 = 78.5
ortalama = (not1 + not2 + not3) / 3

print("1. not:", not1)
print("2. not:", not2)
print("3. not:", not3)
print("Ortalama:", round(ortalama, 2))

print("Pratik uygulamalar tamamlandı!")


# =======================================================
# DERS ÖZET
# =======================================================
print("DERS ÖZETİ")
print("-----------")
print("Bu derste öğrendiğiniz ondalıklı sayı özellikleri:")
print("1. Float sayılar nokta (.) ile yazılır")
print("2. Tüm matematiksel işlemler float sayılarda çalışır")
print("3. Tam sayı + Float = Float sonuç verir")
print("4. round() fonksiyonu ile yuvarlama yapılır")
print("5. int() ondalık kısmı atar, yuvarlamaz")
print("6. Pratik uygulamalar: BMI, alan, sıcaklık, ortalama")

print("ONDALIKLI SAYILAR DERSİ TAMAMLANDI!")
print("Sonraki ders: Metin ifadeleri (string) öğreneceğiz.")