###############################################
# 20. DERS: ENUMERATE - İNDEKS VE DEĞER İKİLİSİ
###############################################

# Bu derste öğreneceğimiz konular:
# - enumerate() fonksiyonu nedir?
# - İndeks ve değere aynı anda erişim
# - enumerate ile pratik uygulamalar
# - Alternatif yöntemlerle karşılaştırma

print("=== ENUMERATE - İNDEKS VE DEĞER İKİLİSİ ===")

#######################
# 1. ENUMERATE NEDİR?
#######################

print("\n=== enumerate Fonksiyonu Nedir? ===")

# enumerate() bir liste veya string üzerinde dönerken
# hem indeks (sıra numarası) hem de değeri verir

ogrenciler = ["Ahmet", "Ayşe", "Mehmet", "Fatma"]

print("Normal for döngüsü (sadece değer):")
for ogrenci in ogrenciler:
    print(ogrenci)

print("\nenumerate ile (indeks + değer):")
for indeks, ogrenci in enumerate(ogrenciler):
    print("İndeks:", indeks, "- Öğrenci:", ogrenci)

print("\nDaha güzel format:")
for i, ogrenci in enumerate(ogrenciler):
    print(f"{i+1}. öğrenci: {ogrenci}")

#######################
# 2. ENUMERATE'İN TEMEL KULLANIMI
#######################

print("\n=== enumerate'in Temel Kullanımı ===")

# String karakterleri üzerinde
metin = "python"
print("String karakterlerinde enumerate:")
for i, karakter in enumerate(metin):
    print(f"Pozisyon {i}: '{karakter}'")

print()

# Liste elemanları üzerinde
renkler = ["kırmızı", "mavi", "yeşil", "sarı"]
print("Renk listesinde enumerate:")
for sira, renk in enumerate(renkler):
    print(f"{sira} numaralı renk: {renk}")

print()

# Sayılar listesi
sayilar = [10, 20, 30, 40, 50]
print("Sayılar listesinde enumerate:")
for konum, deger in enumerate(sayilar):
    print(f"Liste[{konum}] = {deger}")

#######################
# 3. ENUMERATE İLE BAŞLANGIÇ DEĞERİ
#######################

print("\n=== enumerate ile Başlangıç Değeri ===")

# enumerate(liste, start=n) ile başlangıç değeri belirleyebiliriz
dersler = ["Matematik", "Fizik", "Kimya", "Biyoloji"]

print("0'dan başlayarak (varsayılan):")
for i, ders in enumerate(dersler):
    print(f"{i}: {ders}")

print("\n1'den başlayarak:")
for i, ders in enumerate(dersler, start=1):
    print(f"{i}. ders: {ders}")

print("\n10'dan başlayarak:")
for i, ders in enumerate(dersler, start=10):
    print(f"Ders kodu {i}: {ders}")

#######################
# 4. ALTERNATİF YÖNTEMLERLE KARŞILAŞTIRMA
#######################

print("\n=== Alternatif Yöntemlerle Karşılaştırma ===")

liste = ["a", "b", "c", "d"]

# Yöntem 1: range(len()) kullanarak (karmaşık)
print("range(len()) ile (eski yöntem):")
for i in range(len(liste)):
    print(f"{i}: {liste[i]}")

print("\nenumerate ile (modern yöntem):")
for i, eleman in enumerate(liste):
    print(f"{i}: {eleman}")

print("\nHangisi daha okunabilir? enumerate! ✓")

#######################
# 5. PRATİK UYGULAMA ÖRNEKLERİ
#######################

print("\n=== Pratik Uygulama Örnekleri ===")

# Örnek 1: Çift indeksli elemanları bulma
print("Çift indeksli elemanlar:")
meyveler = ["elma", "armut", "muz", "çilek", "kiraz", "üzüm"]

cift_indeksli = []
tek_indeksli = []

for i, meyve in enumerate(meyveler):
    if i % 2 == 0:
        cift_indeksli.append(meyve)
        print(f"Çift indeks {i}: {meyve}")
    else:
        tek_indeksli.append(meyve)

print("Çift indeksliler:", cift_indeksli)
print("Tek indeksliler:", tek_indeksli)

print()

# Örnek 2: En büyük elemanın pozisyonunu bulma
notlar = [85, 92, 78, 96, 89, 73]
print("Notlar:", notlar)

en_yuksek_not = 0
en_yuksek_pozisyon = 0

for i, not_degeri in enumerate(notlar):
    print(f"İndeks {i}: Not {not_degeri}")
    if not_degeri > en_yuksek_not:
        en_yuksek_not = not_degeri
        en_yuksek_pozisyon = i

print(f"En yüksek not: {en_yuksek_not}")
print(f"Pozisyonu: {en_yuksek_pozisyon}")

#######################
# 6. STRING İŞLEME UYGULAMALARI
#######################

print("\n=== String İşleme Uygulamaları ===")

# Uygulama 1: Alternating harf büyütme (18. dersten hatırlayın)
def alternating_with_enumerate(metin):
    """
    Çift indeksleri büyük, tek indeksleri küçük harf yapar
    """
    yeni_metin = ""
    
    for i, karakter in enumerate(metin):
        if i % 2 == 0:
            yeni_metin += karakter.upper()
        else:
            yeni_metin += karakter.lower()
    
    return yeni_metin

test_metni = "python programlama dili"
print("Orijinal:", test_metni)
print("Dönüştürülmüş:", alternating_with_enumerate(test_metni))

print()

# Uygulama 2: Belirli pozisyonlardaki karakterleri değiştirme
def pozisyon_degistir(metin, pozisyonlar, yeni_karakter="*"):
    """
    Belirtilen pozisyonlardaki karakterleri değiştirir
    """
    karakter_listesi = list(metin)
    
    for i, karakter in enumerate(karakter_listesi):
        if i in pozisyonlar:
            karakter_listesi[i] = yeni_karakter
    
    return "".join(karakter_listesi)

orjinal = "merhaba dünya"
degisecek_pozisyonlar = [0, 3, 7, 10]
print("Orijinal:", orjinal)
print("Pozisyonlar:", degisecek_pozisyonlar)
print("Değiştirilmiş:", pozisyon_degistir(orjinal, degisecek_pozisyonlar))

#######################
# 7. LİSTE İŞLEMLERİNDE ENUMERATE
#######################

print("\n=== Liste İşlemlerinde enumerate ===")

# Belirli koşullardaki elemanların pozisyonlarını bulma
sayilar = [12, 7, 23, 9, 17, 31, 4, 19]
print("Sayılar:", sayilar)

# 15'ten büyük sayıların pozisyonları
buyuk_sayilar = []
for i, sayi in enumerate(sayilar):
    if sayi > 15:
        buyuk_sayilar.append((i, sayi))
        print(f"Pozisyon {i}: {sayi} (15'ten büyük)")

print("15'ten büyük sayılar ve pozisyonları:", buyuk_sayilar)

print()

# Liste elemanlarını değiştirme
print("Liste elemanlarını 2 ile çarpma:")
for i, sayi in enumerate(sayilar):
    yeni_deger = sayi * 2
    print(f"sayilar[{i}]: {sayi} → {yeni_deger}")
    sayilar[i] = yeni_deger

print("Yeni liste:", sayilar)

#######################
# 8. FONKSİYONLARLA ENUMERATE
#######################

print("\n=== Fonksiyonlarla enumerate ===")

def liste_analiz(liste):
    """
    Liste hakkında detaylı analiz yapar
    """
    print("Liste analizi:")
    print("-" * 30)
    
    toplam = 0
    en_buyuk = liste[0] if liste else 0
    en_kucuk = liste[0] if liste else 0
    en_buyuk_pozisyon = 0
    en_kucuk_pozisyon = 0
    
    for i, deger in enumerate(liste):
        print(f"İndeks {i:2d}: {deger:3d}")
        
        toplam += deger
        
        if deger > en_buyuk:
            en_buyuk = deger
            en_buyuk_pozisyon = i
        
        if deger < en_kucuk:
            en_kucuk = deger
            en_kucuk_pozisyon = i
    
    print(f"\nToplam: {toplam}")
    print(f"Ortalama: {toplam/len(liste):.2f}")
    print(f"En büyük: {en_buyuk} (pozisyon {en_buyuk_pozisyon})")
    print(f"En küçük: {en_kucuk} (pozisyon {en_kucuk_pozisyon})")

# Test edelim
test_sayilari = [45, 23, 78, 12, 89, 34, 56]
liste_analiz(test_sayilari)

#######################
# 9. ENUMERATE İLE VERİ İŞLEME
#######################

print("\n=== enumerate ile Veri İşleme ===")

# Öğrenci notları ve sıralama
ogrenci_notlari = [
    ("Ahmet", 85),
    ("Ayşe", 92),
    ("Mehmet", 78),
    ("Fatma", 96),
    ("Can", 89)
]

print("Öğrenci sıralama listesi:")
for sira, (isim, not_degeri) in enumerate(ogrenci_notlari, start=1):
    durum = "Geçti" if not_degeri >= 80 else "Şartlı"
    print(f"{sira:2d}. {isim:8s} - Not: {not_degeri:3d} - {durum}")

print()

# En yüksek not alan öğrenci
en_yuksek_not = 0
en_basarili = ""
en_basarili_sira = 0

for i, (isim, not_degeri) in enumerate(ogrenci_notlari):
    if not_degeri > en_yuksek_not:
        en_yuksek_not = not_degeri
        en_basarili = isim
        en_basarili_sira = i + 1

print(f"En başarılı öğrenci: {en_basarili}")
print(f"Notu: {en_yuksek_not}")
print(f"Sıra: {en_basarili_sira}")

#######################
# 10. ENUMERATE vs DİĞER YÖNTEMLER
#######################

print("\n=== enumerate vs Diğer Yöntemler ===")

veri = ["python", "java", "javascript", "go", "rust"]

print("Farklı yöntemlerle aynı işi yapma:")

# Yöntem 1: Manuel sayaç (önerilmez)
print("\n1. Manuel sayaç:")
sayac = 0
for dil in veri:
    print(f"{sayac}: {dil}")
    sayac += 1

# Yöntem 2: range(len()) (karmaşık)
print("\n2. range(len()) kullanımı:")
for i in range(len(veri)):
    print(f"{i}: {veri[i]}")

# Yöntem 3: enumerate (önerilen)
print("\n3. enumerate kullanımı:")
for i, dil in enumerate(veri):
    print(f"{i}: {dil}")

print("\nHangisi en okunabilir ve Pythonic? enumerate! ✓")

#######################
# 11. EN İYİ PRATİKLER VE İPUÇLARI
#######################

print("\n=== En İyi Praktikler ve İpuçları ===")

print("enumerate kullanırken:")
print("✓ Değişken isimleri açık olsun: i, eleman")
print("✓ start parametresini uygun kullanın")
print("✓ tuple unpacking'i doğru yapın")
print("✓ Manuel sayaç yerine enumerate tercih edin")

print("\nNe zaman enumerate kullanmalı:")
print("• Hem indeks hem değere ihtiyaç duyduğunuzda")
print("• Çift/tek pozisyon kontrolü yapacağınızda") 
print("• Elemanları konumlarıyla birlikte işleyeceğinizde")
print("• Liste indekslerini güvenli şekilde kullanacağınızda")

print("\nNe zaman enumerate kullanmamali:")
print("• Sadece değerlere ihtiyaç varsa (normal for döngüsü)")
print("• Sadece indekslere ihtiyaç varsa (range kullanın)")

#######################
# 12. ÖZET VE ÖĞRENME ÇIKTILARI
#######################

print("\n=== Bu Derste Öğrendiklerimiz ===")
print("✓ enumerate() fonksiyonunun kullanımı")
print("✓ İndeks ve değere aynı anda erişim")
print("✓ start parametresi ile başlangıç değeri")
print("✓ Alternatif yöntemlerle karşılaştırma")
print("✓ String işlemede enumerate uygulamaları")
print("✓ Liste analizi ve veri işlemede kullanım")
print("✓ En iyi pratikler ve kullanım alanları")

print("\n=== Kullanılan Kavramlar ===")
print("• enumerate() fonksiyonu")
print("• Tuple unpacking (i, eleman)")
print("• For döngüleri")
print("• İndeksleme ve pozisyon kontrolü")
print("• Liste ve string işlemleri")
print("• Koşullu yapılar")

print("\nSıradaki ders: Zip fonksiyonu - Listeleri birleştirme")
