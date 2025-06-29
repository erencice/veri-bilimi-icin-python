###############################################
# 15. DERS: FONKSİYONLAR - KENDİ KOMUTLARIMIZI YAZMA
###############################################

# Bu derste öğreneceğimiz konular:
# - Fonksiyon nedir ve neden kullanılır?
# - Basit fonksiyon tanımlama
# - Parametreli fonksiyonlar
# - Return ile değer döndürme
# - Pratik fonksiyon örnekleri

print("=== FONKSİYONLAR - KENDİ KOMUTLARIMIZI YAZMA ===")

#######################
# 1. FONKSİON NEDİR?
#######################

# Fonksiyon, belirli bir işi yapan kod bloğudur
# print(), input(), int(), str() gibi hazır fonksiyonları kullandık
# Şimdi kendi fonksiyonlarımızı yazacağız

print("\n=== Fonksiyonların Faydaları ===")
print("✓ Kodu tekrar kullanabilmek")
print("✓ Kodu düzenli tutmak")
print("✓ Karmaşık işlemleri basitleştirmek")
print("✓ Hataları kolayca düzeltebilmek")

#######################
# 2. BASİT FONKSİYON TANIPLAMA
#######################

print("\n=== Basit Fonksiyon Tanımlama ===")

# def anahtar kelimesi ile fonksiyon tanımlanır
# Fonksiyon ismi sonra iki nokta üst üste
# İçerideki kodlar girintili yazılır

def selamla():
    print("Merhaba!")
    print("Python fonksiyonlarına hoş geldiniz!")

# Fonksiyonu çağırmak için ismini yazıp parantez açıp kapatırız
print("Fonksiyonu çağırıyoruz:")
selamla()

print("\nFonksiyonu tekrar çağırabiliriz:")
selamla()

#######################
# 3. PARAMETRELİ FONKSİYONLAR
#######################

print("\n=== Parametreli Fonksiyonlar ===")

# Fonksiyona veri gönderebiliriz (parametre)
def kisisel_selamla(isim):
    print("Merhaba " + isim + "!")
    print("Nasılsın?")

# Fonksiyonu farklı isimlerle çağıralım
kisisel_selamla("Ahmet")
kisisel_selamla("Ayşe")
kisisel_selamla("Mehmet")

#######################
# 4. BİRDEN FAZLA PARAMETRE
#######################

print("\n=== Birden Fazla Parametre ===")

def tam_selamla(isim, soyisim):
    print("Merhaba " + isim + " " + soyisim + "!")
    print("Tanıştığımıza memnun oldum!")

tam_selamla("Ahmet", "Yılmaz")
tam_selamla("Ayşe", "Kaya")

# Matematiksel işlem fonksiyonu
def topla(sayi1, sayi2):
    sonuc = sayi1 + sayi2
    print(sayi1, "+", sayi2, "=", sonuc)

topla(5, 3)
topla(10, 20)
topla(7, 13)

#######################
# 5. RETURN İLE DEĞER DÖNDÜRME
#######################

print("\n=== Return ile Değer Döndürme ===")

# print() sadece ekrana yazıyor
# return fonksiyondan bir değer geri döndürüyor

def hesapla_toplam(a, b):
    sonuc = a + b
    return sonuc  # Sonucu geri döndür

# Return'ü kullanarak sonucu değişkene atayabiliriz
toplam = hesapla_toplam(15, 25)
print("Hesaplanan toplam:", toplam)

# Sonucu başka işlemlerde kullanabiliriz
cift_toplam = toplam * 2
print("Toplamın iki katı:", cift_toplam)

#######################
# 6. MATEMATİKSEL FONKSİYONLAR
#######################

print("\n=== Matematiksel Fonksiyonlar ===")

def kare_al(sayi):
    return sayi * sayi

def kup_al(sayi):
    return sayi * sayi * sayi

def alan_hesapla(en, boy):
    return en * boy

# Bu fonksiyonları kullanalım
sayi = 5
print(sayi, "sayısının karesi:", kare_al(sayi))
print(sayi, "sayısının küpü:", kup_al(sayi))

en = 8
boy = 12
alan = alan_hesapla(en, boy)
print("Dikdörtgen alanı:", alan, "birim kare")

#######################
# 7. VARSAYILAN DEĞERLER
#######################

print("\n=== Varsayılan Değerler ===")

# Parametre için varsayılan değer verebiliriz
def selamla_dil(isim, dil="Türkçe"):
    if dil == "Türkçe":
        print("Merhaba " + isim + "!")
    elif dil == "İngilizce":
        print("Hello " + isim + "!")
    else:
        print("Merhaba " + isim + "!")

# Dil belirtmezsek Türkçe olur
selamla_dil("Ahmet")

# Dil belirtirsek o dili kullanır
selamla_dil("John", "İngilizce")

#######################
# 8. PRATİK UYGULAMA ÖRNEKLERİ
#######################

print("\n=== Pratik Uygulama Örnekleri ===")

# BKİ hesaplama fonksiyonu
def bki_hesapla(kilo, boy):
    bki = kilo / (boy * boy)
    return bki

# Kullanıcı bilgileri
kilo = 70
boy = 1.75
bki = bki_hesapla(kilo, boy)
print("Kilo:", kilo, "kg, Boy:", boy, "m")
print("BKİ:", bki)

# Daire alan hesaplama
def daire_alan(yaricap):
    pi = 3.14159
    alan = pi * yaricap * yaricap
    return alan

yaricap = 5
alan = daire_alan(yaricap)
print("Yarıçapı", yaricap, "olan dairenin alanı:", alan)

# Basit hesap makinesi
def hesap_makinesi(sayi1, sayi2, islem):
    if islem == "toplama":
        return sayi1 + sayi2
    elif islem == "çıkarma":
        return sayi1 - sayi2
    elif islem == "çarpma":
        return sayi1 * sayi2
    elif islem == "bölme":
        return sayi1 / sayi2
    else:
        return "Geçersiz işlem"

# Hesap makinesi kullanımı
sonuc1 = hesap_makinesi(10, 5, "toplama")
sonuc2 = hesap_makinesi(10, 5, "çarpma")
print("10 + 5 =", sonuc1)
print("10 × 5 =", sonuc2)

#######################
# 9. FONKSİYON İÇİNDE FONKSİYON KULLANMA
#######################

print("\n=== Fonksiyon İçinde Fonksiyon Kullanma ===")

# Bir fonksiyon başka fonksiyonları çağırabilir

def faktöriyel_hesapla(n):
    # Faktöriyel = 1 × 2 × 3 × ... × n
    sonuc = 1
    sayac = 1
    while sayac <= n:
        sonuc = sonuc * sayac
        sayac = sayac + 1
    return sonuc

def permutasyon_hesapla(n, r):
    # P(n,r) = n! / (n-r)!
    n_faktöriyel = faktöriyel_hesapla(n)
    nr_faktöriyel = faktöriyel_hesapla(n - r)
    return n_faktöriyel / nr_faktöriyel

# Örnek hesaplama
n = 5
r = 3
sonuc = permutasyon_hesapla(n, r)
print("P(5,3) =", sonuc)

#######################
# 10. ÖNEMLİ NOKTALAR VE İPUÇLARI
#######################

print("\n=== Önemli Noktalar ve İpuçları ===")

# 1. Fonksiyon isimleri açık ve anlamlı olmalı
def iyi_ornek():
    pass

def kotu_ornek():  # Ne yaptığı belli değil
    pass

# 2. Fonksiyonlar tek bir iş yapmalı
def sadece_toplama(a, b):
    return a + b  # Sadece toplama yapar, iyi

# 3. Return kullanımı print'ten daha iyidir
def dogru_kullanim(a, b):
    return a * b  # Sonucu döndürür

def yanlis_kullanim(a, b):
    print(a * b)  # Sadece yazdırır, sonucu alamayız

# 4. Parametreler anlamlı isimlere sahip olmalı
def alan_hesapla_iyi(en, boy):
    return en * boy

def alan_hesapla_kotu(x, y):  # x ve y ne anlama geliyor?
    return x * y

print("\n=== Bu Derste Öğrendiklerimiz ===")
print("✓ def ile fonksiyon tanımlama")
print("✓ Parametreli fonksiyonlar")
print("✓ return ile değer döndürme")
print("✓ Varsayılan parametre değerleri")
print("✓ Fonksiyon içinde fonksiyon kullanma")
print("✓ Pratik matematik fonksiyonları")

print("\nSıradaki ders: Koşullar ve karar yapıları")
