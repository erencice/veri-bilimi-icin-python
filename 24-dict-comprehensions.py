###############################################
# 24. DERS: DICTIONARY COMPREHENSIONS (SÖZLÜK KAVRAMA)
###############################################

# Bu derste öğreneceğimiz konular:
# - Dictionary comprehension temel kullanımı
# - Koşullu dictionary comprehension
# - Zip fonksiyonu ile dictionary oluşturma
# - Performans avantajları ve pratik uygulamalar

print("=== DICTIONARY COMPREHENSIONS (SÖZLÜK KAVRAMA) ===")

# Dictionary comprehension: Sözlükleri tek satırda oluşturmanın pratik yolu
# List comprehension'ın sözlük versiyonu: {key: value for item in iterable}

#######################
# 1. TEMEL DICTIONARY COMPREHENSION
#######################

print("\n=== Temel Dictionary Comprehension ===")

# Basit bir sözlüklə başlayalım
sayilar = [1, 2, 3, 4, 5]

# Normal yöntem: For döngüsü ile kareler sözlüğü
kareler_normal = {}
for sayi in sayilar:
    kareler_normal[sayi] = sayi ** 2
print("Normal for döngüsü ile kareler:", kareler_normal)

# Dictionary comprehension ile kareler (tek satır!)
kareler_dict = {sayi: sayi ** 2 for sayi in sayilar}
print("Dict comprehension ile kareler:", kareler_dict)

# String listesinden uzunluk sözlüğü
isimler = ["ali", "mehmet", "ayşe", "fatma"]
isim_uzunlukları = {isim: len(isim) for isim in isimler}
print("İsim uzunlukları:", isim_uzunlukları)

#######################
# 2. MEVCUT SÖZLÜK ÜZERİNDE İŞLEMLER
#######################

print("\n=== Mevcut Sözlük Üzerinde İşlemler ===")

# Mevcut bir sözlük
notlar = {"Ali": 85, "Veli": 92, "Ayşe": 78, "Mehmet": 95, "Fatma": 67}

# Tüm notları 10 puan artır
artirilmis_notlar = {isim: notu + 10 for isim, notu in notlar.items()}
print("10 puan artırılmış notlar:", artirilmis_notlar)

# İsimleri büyük harfe çevir
buyuk_isimler = {isim.upper(): notu for isim, notu in notlar.items()}
print("Büyük harfli isimler:", buyuk_isimler)

# Hem isim hem not değiştir
donusturulmus = {isim.upper(): notu * 1.1 for isim, notu in notlar.items()}
print("Dönüştürülmüş sözlük:", donusturulmus)

#######################
# 3. KOŞULLU DICTIONARY COMPREHENSION
#######################

print("\n=== Koşullu Dictionary Comprehension ===")

# Sadece geçen öğrencileri al (70+ not)
gecen_ogrenciler = {isim: notu for isim, notu in notlar.items() if notu >= 70}
print("Geçen öğrenciler:", gecen_ogrenciler)

# Çift sayıların karelerini al
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift_kareler = {sayi: sayi ** 2 for sayi in sayilar if sayi % 2 == 0}
print("Çift sayıların kareleri:", cift_kareler)

# Uzun isimleri al (5+ harf)
uzun_isimler = {isim: len(isim) for isim in isimler if len(isim) >= 5}
print("Uzun isimler:", uzun_isimler)

#######################
# 4. IF-ELSE KOMBINASYONU
#######################

print("\n=== If-Else Kombinasyonu ===")

# 80+ not alanlar "Başarılı", diğerleri "Gelişmeli"
basari_durumu = {isim: "Başarılı" if notu >= 80 else "Gelişmeli" for isim, notu in notlar.items()}
print("Başarı durumu:", basari_durumu)

# Çift sayıları 2 ile çarp, tekları 3 ile çarp
cift_tek_dict = {sayi: sayi * 2 if sayi % 2 == 0 else sayi * 3 for sayi in sayilar}
print("Çift/tek işlem:", cift_tek_dict)

#######################
# 5. ZIP İLE DICTIONARY OLUŞTURMA
#######################

print("\n=== Zip ile Dictionary Oluşturma ===")

# İki ayrı listeden sözlük oluşturma
sehirler = ["İstanbul", "Ankara", "İzmir", "Antalya"]
nufuslar = [15000000, 5500000, 4300000, 2500000]

# Normal yöntem
sehir_nufus_normal = {}
for sehir, nufus in zip(sehirler, nufuslar):
    sehir_nufus_normal[sehir] = nufus
print("Normal yöntem:", sehir_nufus_normal)

# Dictionary comprehension ile
sehir_nufus = {sehir: nufus for sehir, nufus in zip(sehirler, nufuslar)}
print("Dict comprehension:", sehir_nufus)

# Nüfusları milyonlara çevir
sehir_milyon = {sehir: nufus / 1000000 for sehir, nufus in zip(sehirler, nufuslar)}
print("Milyon cinsinden:", sehir_milyon)

#######################
# 6. RANGE İLE DICTIONARY OLUŞTURMA
#######################

print("\n=== Range ile Dictionary Oluşturma ===")

# 1'den 5'e kadar sayıların kareleri
kare_dict = {sayi: sayi ** 2 for sayi in range(1, 6)}
print("Kare sözlüğü:", kare_dict)

# Çift sayılar için faktöriyel benzeri
faktoriyel_dict = {sayi: sayi * (sayi - 1) for sayi in range(2, 6)}
print("Faktöriyel benzeri:", faktoriyel_dict)

#######################
# 7. STRING İŞLEMLERİ
#######################

print("\n=== String İşlemleri ===")

# Cümledeki kelimelerin uzunlukları
cumle = "Python öğrenmek çok eğlenceli ve faydalı"
kelime_uzunlukları = {kelime: len(kelime) for kelime in cumle.split()}
print("Kelime uzunlukları:", kelime_uzunlukları)

# Kelimelerin ilk harfleri
ilk_harfler = {kelime: kelime[0].upper() for kelime in cumle.split()}
print("İlk harfler:", ilk_harfler)

#######################
# 8. PRATİK ÖRNEKLER
#######################

print("\n=== Pratik Örnekler ===")

# Örnek 1: Karakter sayacı
metin = "python programlama"
karakter_sayaci = {harf: metin.count(harf) for harf in set(metin) if harf != ' '}
print("Karakter sayacı:", karakter_sayaci)

# Örnek 2: Sıcaklık dönüştürme
celsius_listesi = [0, 10, 20, 30, 40, 100]
celsius_fahrenheit = {c: c * 9/5 + 32 for c in celsius_listesi}
print("Celsius -> Fahrenheit:", celsius_fahrenheit)

# Örnek 3: Ürün fiyat güncellemesi
urunler = {"Laptop": 5000, "Telefon": 3000, "Tablet": 2000, "Kulaklık": 500}
indirimli_fiyatlar = {urun: fiyat * 0.8 for urun, fiyat in urunler.items()}
print("İndirimli fiyatlar (%20 indirim):", indirimli_fiyatlar)

# Örnek 4: Öğrenci bilgi sistemi
ogrenci_listesi = ["Ali", "Veli", "Ayşe", "Mehmet"]
ogrenci_no = {ogrenci: f"2024{i+1:03d}" for i, ogrenci in enumerate(ogrenci_listesi)}
print("Öğrenci numaraları:", ogrenci_no)

#######################
# 9. EN İYİ PRATİKLER
#######################

print("\n=== En İyi Pratikler ===")

print("✓ Basit dönüşümler için dictionary comprehension kullanın")
print("✓ Karmaşık mantık için normal for döngüsü tercih edin")
print("✓ Okunabilirliği her zaman önceleyın")
print("✓ Çok uzun comprehension'ları parçalayın")
print("✓ Key'lerin benzersiz olduğundan emin olun")

# Format özetleri
print("\nDictionary Comprehension formatları:")
print("Temel: {key: value for item in iterable}")
print("Koşullu: {key: value for item in iterable if condition}")
print("If-else: {key: true_value if condition else false_value for item in iterable}")

print("\n=== Bu Derste Öğrendiklerimiz ===")
print("✓ Dictionary comprehension temel kullanımı")
print("✓ Mevcut sözlük üzerinde işlemler")
print("✓ Koşullu filtreleme (if)")
print("✓ If-else kombinasyonları")
print("✓ Zip ile sözlük oluşturma")
print("✓ Range ile sözlük oluşturma")
print("✓ String işlemleri")
print("✓ Performans avantajları")
print("✓ En iyi pratikler")

print("\nSıradaki ders: Uygulamalar ve Örnekler")

