###############################################
# 16. DERS: KOŞULLAR VE KARAR YAPILARI
###############################################

# Bu derste öğreneceğimiz konular:
# - True ve False kavramı
# - if koşul yapısı
# - if-else yapısı
# - if-elif-else çoklu koşullar
# - Mantıksal operatörler (and, or, not)
# - Pratik örnekler

print("=== KOŞULLAR VE KARAR YAPILARI ===")

#######################
# 1. TRUE VE FALSE KAVRAMI
#######################

print("\n=== True ve False Kavramı ===")

# Karşılaştırma işlemleri True veya False sonucu verir
print("5 > 3 sonucu:", 5 > 3)        # True
print("5 < 3 sonucu:", 5 < 3)        # False
print("5 == 5 sonucu:", 5 == 5)      # True
print("5 != 5 sonucu:", 5 != 5)      # False

# Karşılaştırma operatörleri:
print("\nKarşılaştırma Operatörleri:")
print("== : Eşit mi?")
print("!= : Eşit değil mi?")
print(">  : Büyük mü?")
print("<  : Küçük mü?")
print(">= : Büyük veya eşit mi?")
print("<= : Küçük veya eşit mi?")

#######################
# 2. BASİT if YAPISI
#######################

print("\n=== Basit if Yapısı ===")

# if koşul doğruysa kod bloğu çalışır
yas = 18

if yas >= 18:
    print("Reşitsiniz!")

print("Bu satır her zaman çalışır")

# Başka bir örnek
sayi = 10

if sayi > 5:
    print("Sayı 5'ten büyük")
    print("Bu satır da if bloğunun içinde")

print("Bu satır if bloğunun dışında")

#######################
# 3. if-else YAPISI
#######################

print("\n=== if-else Yapısı ===")

# Koşul doğru değilse else bloğu çalışır
yas = 15

if yas >= 18:
    print("Reşitsiniz!")
else:
    print("Henüz reşit değilsiniz")

# Fonksiyon ile örnek
def yas_kontrol(yas):
    if yas >= 18:
        return "Reşit"
    else:
        return "Reşit değil"

print("20 yaşında:", yas_kontrol(20))
print("16 yaşında:", yas_kontrol(16))

#######################
# 4. if-elif-else YAPISI
#######################

print("\n=== if-elif-else Yapısı ===")

# Birden fazla koşul kontrolü için elif kullanılır

def not_degerlendirme(puan):
    if puan >= 85:
        return "Pekiyi"
    elif puan >= 70:
        return "İyi"
    elif puan >= 55:
        return "Orta"
    elif puan >= 40:
        return "Geçer"
    else:
        return "Kaldı"

# Farklı puanları test edelim
print("90 puan:", not_degerlendirme(90))
print("75 puan:", not_degerlendirme(75))
print("60 puan:", not_degerlendirme(60))
print("45 puan:", not_degerlendirme(45))
print("30 puan:", not_degerlendirme(30))

#######################
# 5. MANTIKSAL OPERATÖRLER
#######################

print("\n=== Mantıksal Operatörler ===")

# and: Her iki koşul da doğru olmalı
# or: En az bir koşul doğru olmalı
# not: Koşulun tersini alır

yas = 25
maas = 8000

print("Yaş:", yas, "Maaş:", maas)

# and operatörü
if yas >= 18 and maas >= 5000:
    print("Kredi için uygun")
else:
    print("Kredi için uygun değil")

# or operatörü
if yas >= 65 or maas <= 3000:
    print("İndirim hakkı var")
else:
    print("İndirim hakkı yok")

# not operatörü
if not yas < 18:
    print("Reşit")
else:
    print("Reşit değil")

#######################
# 6. İÇ İÇE KOŞULLAR
#######################

print("\n=== İç İçe Koşullar ===")

def detayli_kontrol(yas, gelir):
    if yas >= 18:
        print("Reşitsiniz")
        if gelir >= 5000:
            print("Yüksek gelir grubunda")
            if gelir >= 15000:
                print("Çok yüksek gelir")
        else:
            print("Düşük gelir grubunda")
    else:
        print("Henüz reşit değilsiniz")

detayli_kontrol(25, 8000)
detayli_kontrol(16, 3000)
detayli_kontrol(30, 20000)

#######################
# 7. PRATİK UYGULAMA ÖRNEKLERİ
#######################

print("\n=== Pratik Uygulama Örnekleri ===")

# Örnek 1: BKİ değerlendirmesi
def bki_degerlendirme(kilo, boy):
    bki = kilo / (boy * boy)
    
    if bki < 18.5:
        kategori = "Zayıf"
    elif bki < 25:
        kategori = "Normal"
    elif bki < 30:
        kategori = "Fazla kilolu"
    else:
        kategori = "Obez"
    
    return bki, kategori

bki, kategori = bki_degerlendirme(70, 1.75)
print("BKİ:", bki, "Kategori:", kategori)

# Örnek 2: Hava durumu tavsiyeleri
def hava_tavsiyesi(sicaklik):
    if sicaklik >= 30:
        return "Çok sıcak! Bol su için, gölgede durun"
    elif sicaklik >= 20:
        return "Güzel hava! Dışarı çıkabilirsiniz"
    elif sicaklik >= 10:
        return "Serin, mont almayı unutmayın"
    elif sicaklik >= 0:
        return "Soğuk! Kalın giysiler giyin"
    else:
        return "Dondurucu soğuk! Dışarı çıkmayın"

print("25°C:", hava_tavsiyesi(25))
print("5°C:", hava_tavsiyesi(5))
print("-5°C:", hava_tavsiyesi(-5))

# Örnek 3: Basit hesap makinesi
def hesap_makinesi(sayi1, sayi2, islem):
    if islem == "+":
        return sayi1 + sayi2
    elif islem == "-":
        return sayi1 - sayi2
    elif islem == "*":
        return sayi1 * sayi2
    elif islem == "/":
        if sayi2 != 0:
            return sayi1 / sayi2
        else:
            return "Sıfıra bölünemez!"
    else:
        return "Geçersiz işlem"

print("10 + 5 =", hesap_makinesi(10, 5, "+"))
print("10 / 0 =", hesap_makinesi(10, 0, "/"))
print("10 x 5 =", hesap_makinesi(10, 5, "x"))

#######################
# 8. STRING'LERDEKİ KOŞULLAR
#######################

print("\n=== String'lerdeki Koşullar ===")

def dil_kontrolu(metin):
    # String'lerde de koşullar kullanabiliriz
    if metin == "merhaba":
        return "Türkçe selamlama"
    elif metin == "hello":
        return "İngilizce selamlama"
    elif metin == "hola":
        return "İspanyolca selamlama"
    else:
        return "Bilinmeyen dil"

print("merhaba:", dil_kontrolu("merhaba"))
print("hello:", dil_kontrolu("hello"))
print("bonjour:", dil_kontrolu("bonjour"))

# String metodları ile koşullar
def metin_analizi(metin):
    if len(metin) > 10:
        print("Uzun metin")
    else:
        print("Kısa metin")
    
    if metin.isupper():
        print("Tüm harfler büyük")
    elif metin.islower():
        print("Tüm harfler küçük")
    else:
        print("Karışık harf durumu")

metin_analizi("PYTHON")
metin_analizi("python")
metin_analizi("Bu uzun bir metin örneğidir")

#######################
# 9. ÖNEMLİ İPUÇLARI VE HATALAR
#######################

print("\n=== Önemli İpuçları ===")

# Doğru kullanım
sayi = 10
if sayi == 10:  # Eşitlik kontrolü için == kullanın
    print("Sayı 10")

# Yaygın hatalar:
# if sayi = 10:  # YANLIŞ! = atama operatörü
# if sayi == 10  # YANLIŞ! : eksik

# Boolean değerlerle direkt kullanım
dogru_mu = True
if dogru_mu:  # if dogru_mu == True: yazmaya gerek yok
    print("Doğru")

# Not operatörü kullanımı
if not dogru_mu:
    print("Yanlış")

print("\n=== Bu Derste Öğrendiklerimiz ===")
print("✓ True/False kavramı ve karşılaştırma operatörleri")
print("✓ if koşul yapısı")
print("✓ if-else yapısı")
print("✓ if-elif-else çoklu koşullar")
print("✓ Mantıksal operatörler (and, or, not)")
print("✓ İç içe koşullar")
print("✓ Pratik uygulama örnekleri")

print("\nSıradaki ders: Döngüler - Tekrar yapıları")
