# =======================================================
# PYTHON DERS 5: TAM SAYILARLA İLERİ İŞLEMLER
# =======================================================

# Önceki derslerde print() fonksiyonunu ayrıntılı öğrendik.
# Bu derste tam sayılarla daha fazla işlem yapmayı öğreneceğiz.

# Öğreneceğiniz konular:
#   - Tam sayı özellikleri
#   - Negatif sayılarla işlemler
#   - Büyük sayılarla çalışma
#   - Pratik uygulama örnekleri
#   - Tip dönüşümlerinde dikkat edilecekler

print("Python Tam Sayılar Dersine Hoş Geldiniz!")


# =======================================================
# 1. TAM SAYI ÖZELLİKLERİ
# =======================================================
print("1. TAM SAYI ÖZELLİKLERİ")
print("------------------------")

# Pozitif, negatif ve sıfır tam sayılar
pozitif = 42
negatif = -15
sifir = 0

print("Pozitif tam sayı:", pozitif)
print("Negatif tam sayı:", negatif)
print("Sıfır:", sifir)

# type() ile hepsinin türünü kontrol edelim
print("pozitif'in türü:", type(pozitif))
print("negatif'in türü:", type(negatif))
print("sifir'ın türü:", type(sifir))

print("Tam sayı özellikleri tamamlandı!")


# =======================================================
# 2. NEGATİF SAYILARLA İŞLEMLER
# =======================================================
print("2. NEGATİF SAYILARLA İŞLEMLER")
print("------------------------------")

a = -10
b = 5
c = -3

# Negatif sayılarla temel işlemler
print("a + b =", a + b)    # -10 + 5 = -5
print("a - b =", a - b)    # -10 - 5 = -15
print("a * b =", a * b)    # -10 * 5 = -50
print("a / b =", a / b)    # -10 / 5 = -2.0

# İki negatif sayının çarpımı
print("a * c =", a * c)    # -10 * -3 = 30

# Negatif sayının üssü
print("a ** 2 =", a ** 2)  # (-10)² = 100
print("a ** 3 =", a ** 3)  # (-10)³ = -1000

print("Negatif sayılarla işlemler tamamlandı!")


# =======================================================
# 3. BÜYÜK SAYILARLA ÇALIŞMA
# =======================================================
print("3. BÜYÜK SAYILARLA ÇALIŞMA")
print("---------------------------")

# Python'da tam sayılar çok büyük olabilir
milyon = 1000000
milyar = 1000000000
trilyon = 1000000000000

print("1 milyon:", milyon)
print("1 milyar:", milyar)
print("1 trilyon:", trilyon)

# Çok büyük bir sayı oluşturalım
buyuk_sayi = 2 ** 100  # 2'nin 100. kuvveti
print("2^100 =", buyuk_sayi)
print("Bu sayının türü:", type(buyuk_sayi))

print("Büyük sayılarla çalışma tamamlandı!")


# =======================================================
# 4. BÖLME İŞLEMLERİNDE DİKKAT EDİLECEKLER
# =======================================================
print("4. BÖLME İŞLEMLERİNDE DİKKAT EDİLECEKLER")
print("----------------------------------------")

# Normal bölme (/) her zaman float sonuç verir
print("10 / 3 =", 10 / 3)      # 3.3333333333333335
print("12 / 4 =", 12 / 4)      # 3.0 (tam bölünse bile float)

# Tam sayı bölmesi (//) sadece tam kısmı verir
print("10 // 3 =", 10 // 3)    # 3
print("12 // 4 =", 12 // 4)    # 3

# Negatif sayılarda tam sayı bölmesi
print("-10 // 3 =", -10 // 3)  # -4 (aşağı yuvarlar)
print("-12 // 4 =", -12 // 4)  # -3

print("Bölme işlemleri tamamlandı!")


# =======================================================
# 5. PRATİK UYGULAMALAR
# =======================================================
print("5. PRATİK UYGULAMALAR")
print("----------------------")

# Uygulama 1: Yaş hesaplama
dogum_yili = 1995
su_anki_yil = 2024
yas = su_anki_yil - dogum_yili
print("Doğum yılı:", dogum_yili)
print("Şu anki yıl:", su_anki_yil)
print("Yaş:", yas)

# Uygulama 2: Sıcaklık dönüşümü (Celsius'tan Fahrenheit'e)
celsius = 25
fahrenheit = celsius * 9 // 5 + 32  # Tam sayı bölmesi kullandık
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

# Uygulama 3: Dakikayı saat ve dakikaya çevirme
toplam_dakika = 150
saat = toplam_dakika // 60  # Tam bölme ile saat sayısı
kalan_dakika = toplam_dakika % 60  # Kalan ile dakika sayısı
print("Toplam dakika:", toplam_dakika)
print("Saat:", saat, "Dakika:", kalan_dakika)

# Uygulama 4: Çift mi tek mi kontrolü
sayi = 17
kalan = sayi % 2
print("Sayı:", sayi)
print("2'ye bölümünden kalan:", kalan)
if kalan == 0:
    print("Bu sayı çifttir")
else:
    print("Bu sayı tektir")

print("Pratik uygulamalar tamamlandı!")


# =======================================================
# DERS ÖZET
# =======================================================
print("DERS ÖZETİ")
print("-----------")
print("Bu derste öğrendiğiniz tam sayı özellikleri:")
print("1. Pozitif, negatif ve sıfır tam sayılar")
print("2. Negatif sayılarla matematiksel işlemler")
print("3. Python'da tam sayılar çok büyük olabilir")
print("4. Normal bölme (/) float, tam bölme (//) int sonuç verir")
print("5. Mod (%) işlemi kalanı verir")
print("6. Pratik uygulamalar: yaş, sıcaklık, zaman dönüşümleri")

print("TAM SAYILAR DERSİ TAMAMLANDI!")
print("Sonraki ders: Ondalıklı sayıları (float) öğreneceğiz.")