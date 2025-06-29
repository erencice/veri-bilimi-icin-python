# =======================================================
# PYTHON DERS 2: TEMEL VERİ TÜRLERİ
# =======================================================

# Bir önceki derste matematiksel işlemleri öğrendik.
# Bu derste Python'da hangi türde veriler saklayabileceğimizi öğreneceğiz.

# Öğreneceğiniz veri türleri:
#   1. int (Tam sayılar)
#   2. float (Ondalıklı sayılar) 
#   3. str (Metinler)
#   4. bool (Mantıksal değerler)

# type() fonksiyonu bir verinin hangi türde olduğunu gösterir.

print("Python Veri Türleri Dersine Hoş Geldiniz!")


# =======================================================
# 1. TAM SAYILAR (int)
# =======================================================
print("1. TAM SAYILAR (int)")
print("---------------------")

# Tam sayılar pozitif, negatif veya sıfır olabilir
sayi1 = 42        # Pozitif tam sayı
sayi2 = -15       # Negatif tam sayı  
sayi3 = 0         # Sıfır

print("Pozitif tam sayı:", sayi1)
print("Negatif tam sayı:", sayi2)
print("Sıfır:", sayi3)

# type() fonksiyonu ile veri türünü kontrol edebiliriz
print("sayi1'in türü:", type(sayi1))
print("sayi2'in türü:", type(sayi2))

print("Tam sayılar konusu tamamlandı!")


# =======================================================
# 2. ONDALIKLI SAYILAR (float)
# =======================================================
print("2. ONDALIKLI SAYILAR (float)")
print("------------------------------")

# Ondalıklı sayılar nokta ile yazılır
pi = 3.14159      # Pi sayısı
sicaklik = -5.2   # Negatif ondalıklı sayı
yukseklik = 175.5 # Pozitif ondalıklı sayı

print("Pi sayısı:", pi)
print("Sıcaklık:", sicaklik)
print("Yükseklik:", yukseklik)

# type() ile kontrol edelim
print("pi'nin türü:", type(pi))
print("sicaklik'in türü:", type(sicaklik))

print("Ondalıklı sayılar konusu tamamlandı!")


# =======================================================
# 3. METİNLER (str)
# =======================================================
print("3. METİNLER (str)")
print("-----------------")

# Metinler tek veya çift tırnak içinde yazılır
isim = "Ahmet"           # Çift tırnak
soyisim = 'Yılmaz'       # Tek tırnak
mesaj = "Merhaba Dünya!" # Uzun metin
bos_metin = ""           # Boş metin

print("İsim:", isim)
print("Soyisim:", soyisim)
print("Mesaj:", mesaj)
print("Boş metin:", bos_metin)

# type() ile kontrol edelim
print("isim'in türü:", type(isim))
print("mesaj'ın türü:", type(mesaj))

print("Metinler konusu tamamlandı!")


# =======================================================
# 4. MANTIKSAL DEĞERLER (bool)
# =======================================================
print("4. MANTIKSAL DEĞERLER (bool)")
print("------------------------------")

# Mantıksal değerler sadece True (Doğru) veya False (Yanlış) olabilir
# DİKKAT: True ve False büyük harfle yazılır!
dogru = True      # Doğru değer
yanlis = False    # Yanlış değer

print("Doğru değer:", dogru)
print("Yanlış değer:", yanlis)

# type() ile kontrol edelim
print("dogru'nun türü:", type(dogru))
print("yanlis'ın türü:", type(yanlis))

# Mantıksal değerler genellikle karşılaştırmalarda kullanılır
# Örnek: Bir sayının büyük olup olmadığını kontrol etmek
sayi = 15
buyuk_mu = sayi > 10  # 15 > 10 True'dur
print("15 sayısı 10'dan büyük mü?", buyuk_mu)
print("Sonucun türü:", type(buyuk_mu))

print("Mantıksal değerler konusu tamamlandı!")


# =======================================================
# 5. VERİ TÜRLERİNİ KARŞILAŞTIRMA
# =======================================================
print("5. VERİ TÜRLERİNİ KARŞILAŞTIRMA")
print("--------------------------------")

# Aynı değerde farklı türlerde veriler oluşturalım
tam_sayi = 5        # int türünde 5
ondalik_sayi = 5.0  # float türünde 5.0
sayi_metni = "5"    # str türünde "5"

print("Tam sayı:", tam_sayi, "- Türü:", type(tam_sayi))
print("Ondalıklı sayı:", ondalik_sayi, "- Türü:", type(ondalik_sayi))
print("Sayı metni:", sayi_metni, "- Türü:", type(sayi_metni))

# Bu değerler farklı türlerde olsa da bazıları birbirine eşit olabilir
print("5 == 5.0 mi?", tam_sayi == ondalik_sayi)     # True
print("5 == '5' mi?", tam_sayi == sayi_metni)       # False

print("Veri türlerini karşılaştırma tamamlandı!")


# =======================================================
# DERS ÖZET
# =======================================================
print("DERS ÖZETİ")
print("-----------")
print("Bu derste öğrendiğiniz veri türleri:")
print("1. int (Tam sayılar): 42, -15, 0")
print("2. float (Ondalıklı sayılar): 3.14, -5.2, 175.5")
print("3. str (Metinler): 'Merhaba', \"Python\"")
print("4. bool (Mantıksal değerler): True, False")
print("5. type() fonksiyonu: Veri türünü kontrol eder")

print("VERİ TÜRLERİ DERSİ TAMAMLANDI!")
print("Sonraki ders: Tip dönüşümlerini öğreneceğiz.")