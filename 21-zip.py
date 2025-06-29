###############################################
# 21. DERS: ZIP FONKSİYONU - LİSTELERİ BİRLEŞTİRME
###############################################

# Bu derste öğreneceğimiz konular:
# - zip() fonksiyonu nedir?
# - Birden fazla listeyi birlikte işleme
# - Sözlük oluşturma uygulamaları
# - Unzip işlemi (tersine çevirme)
# - Pratik kullanım örnekleri

print("=== ZIP FONKSİYONU - LİSTELERİ BİRLEŞTİRME ===")

#######################
# 1. ZIP FONKSİYONU NEDİR?
#######################

print("\n=== zip Fonksiyonu Nedir? ===")

# zip() fonksiyonu birden fazla listeyi paralel olarak birleştirir
# Aynı indeksteki elemanları tuple halinde gruplar

print("Örnek: Üç ayrı liste")
isimler = ["Ahmet", "Ayşe", "Mehmet"]
yaslar = [25, 23, 28]
sehirler = ["İstanbul", "Ankara", "İzmir"]

print("İsimler:", isimler)
print("Yaşlar:", yaslar)
print("Şehirler:", sehirler)

print("\nzip ile birleştirme:")
birlesik = list(zip(isimler, yaslar, sehirler))
print("Birleşik hali:", birlesik)

print("\nAnlamlı format:")
for isim, yas, sehir in zip(isimler, yaslar, sehirler):
    print(f"{isim}, {yas} yaşında, {sehir}'da yaşıyor")

#######################
# 2. ZIP İLE TEMEL KULLANIM
#######################

print("\n=== zip ile Temel Kullanım ===")

# İki liste birleştirme
sayilar = [1, 2, 3, 4, 5]
harfler = ['a', 'b', 'c', 'd', 'e']

print("Sayılar:", sayilar)
print("Harfler:", harfler)

print("\nzip ile eşleştirme:")
for sayi, harf in zip(sayilar, harfler):
    print(f"Sayı: {sayi} - Harf: {harf}")

print("\nListe haline getirme:")
eslestirilmis = list(zip(sayilar, harfler))
print("Eşleştirilmiş:", eslestirilmis)

#######################
# 3. FARKLI UZUNLUKTAKI LİSTELER
#######################

print("\n=== Farklı Uzunluktaki Listeler ===")

kisa_liste = [1, 2, 3]
uzun_liste = ['a', 'b', 'c', 'd', 'e', 'f']

print("Kısa liste:", kisa_liste)
print("Uzun liste:", uzun_liste)

print("\nzip sonucu (kısa liste kadar eşleşir):")
sonuc = list(zip(kisa_liste, uzun_liste))
print("Sonuç:", sonuc)
print("Not: 'd', 'e', 'f' elemanları atlandı")

print("\nPraktik örnek:")
for sayi, harf in zip(kisa_liste, uzun_liste):
    print(f"{sayi} → {harf}")

#######################
# 4. SÖZLÜK OLUŞTURMA
#######################

print("\n=== Sözlük Oluşturma ===")

# İki listeyi key-value olarak sözlük yapma
anahtarlar = ["ad", "soyad", "yas", "meslek"]
degerler = ["Ahmet", "Yılmaz", 30, "Mühendis"]

print("Anahtarlar:", anahtarlar)
print("Değerler:", degerler)

# zip ile sözlük oluşturma
sozluk = dict(zip(anahtarlar, degerler))
print("\nOluşan sözlük:", sozluk)

# Sözlüğü kullanma
print(f"\nKişi bilgileri:")
print(f"Ad: {sozluk['ad']}")
print(f"Soyad: {sozluk['soyad']}")
print(f"Yaş: {sozluk['yas']}")
print(f"Meslek: {sozluk['meslek']}")

#######################
# 5. ÇOK LİSTELİ UYGULAMA
#######################

print("\n=== Çok Listeli Uygulama ===")

# Öğrenci bilgi sistemi
ogrenci_adlari = ["Zeynep", "Can", "Defne", "Berk"]
matematik_notlari = [85, 78, 92, 67]
fizik_notlari = [90, 82, 88, 74]
kimya_notlari = [87, 85, 94, 71]

print("Öğrenci Not Raporu:")
print("-" * 50)

for ad, mat, fiz, kim in zip(ogrenci_adlari, matematik_notlari, fizik_notlari, kimya_notlari):
    ortalama = (mat + fiz + kim) / 3
    print(f"{ad:8s} | Mat: {mat:2d} | Fiz: {fiz:2d} | Kim: {kim:2d} | Ort: {ortalama:.1f}")

#######################
# 6. UNZIP İŞLEMİ (TERSİNE ÇEVİRME)
#######################

print("\n=== Unzip İşlemi (Tersine Çevirme) ===")

# Birleştirilmiş veriyi tekrar ayırma
birlesik_veri = [("Ahmet", 25), ("Ayşe", 23), ("Mehmet", 28)]
print("Birleşik veri:", birlesik_veri)

# * operatörü ile unzip
isimler_yeni, yaslar_yeni = zip(*birlesik_veri)
print("Ayrılan isimler:", isimler_yeni)
print("Ayrılan yaşlar:", yaslar_yeni)

# Başka bir örnek
koordinatlar = [(1, 2), (3, 4), (5, 6), (7, 8)]
print("\nKoordinat noktaları:", koordinatlar)

x_koordinatlari, y_koordinatlari = zip(*koordinatlar)
print("X koordinatları:", x_koordinatlari)
print("Y koordinatları:", y_koordinatlari)

#######################
# 7. PRATİK UYGULAMA ÖRNEKLERİ
#######################

print("\n=== Pratik Uygulama Örnekleri ===")

# Örnek 1: Alışveriş sepeti
urunler = ["Ekmek", "Süt", "Peynir", "Domates"]
fiyatlar = [2.5, 4.0, 15.0, 8.0]
adetler = [2, 1, 1, 3]

print("Alışveriş sepeti:")
toplam_tutar = 0

for urun, fiyat, adet in zip(urunler, fiyatlar, adetler):
    tutar = fiyat * adet
    toplam_tutar += tutar
    print(f"{urun:10s} | {fiyat:5.1f} TL x {adet} adet = {tutar:6.1f} TL")

print(f"{'Toplam':>35s} = {toplam_tutar:6.1f} TL")

print()

# Örnek 2: Sıcaklık dönüşümü
gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]
celsius_sicaklik = [22, 25, 19, 27, 24]

print("Haftalık hava durumu:")
for gun, celsius in zip(gunler, celsius_sicaklik):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{gun:10s}: {celsius:2d}°C = {fahrenheit:4.1f}°F")

#######################
# 8. ENUMERATE VE ZIP BİRLİKTE
#######################

print("\n=== enumerate ve zip Birlikte ===")

takimlar = ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor"]
puanlar = [65, 72, 58, 49]

print("Lige tablosu:")
for sira, (takim, puan) in enumerate(zip(takimlar, puanlar), start=1):
    print(f"{sira}. {takim:12s} - {puan} puan")

print()

# Başka bir birleştirme örneği
sehir_isimleri = ["İstanbul", "Ankara", "İzmir", "Antalya"]
nufuslar = [15500000, 5500000, 4400000, 2500000]

print("Türkiye'nin büyük şehirleri:")
for i, (sehir, nufus) in enumerate(zip(sehir_isimleri, nufuslar), 1):
    print(f"{i}. {sehir}: {nufus:,} kişi")

#######################
# 9. FONKSİYONLARLA ZIP KULLANIMI
#######################

print("\n=== Fonksiyonlarla zip Kullanımı ===")

def ogrenci_raporu_olustur(isimler, notlar1, notlar2, notlar3):
    """
    Üç farklı dersten notları olan öğrenciler için rapor oluşturur
    """
    print("Öğrenci Başarı Raporu")
    print("=" * 40)
    
    gecenler = []
    kalanlar = []
    
    for isim, not1, not2, not3 in zip(isimler, notlar1, notlar2, notlar3):
        ortalama = (not1 + not2 + not3) / 3
        durum = "GEÇTİ" if ortalama >= 60 else "KALDI"
        
        print(f"{isim:10s} | {not1:3d} {not2:3d} {not3:3d} | Ort: {ortalama:5.1f} | {durum}")
        
        if ortalama >= 60:
            gecenler.append(isim)
        else:
            kalanlar.append(isim)
    
    print(f"\nGeçen öğrenci sayısı: {len(gecenler)}")
    print(f"Kalan öğrenci sayısı: {len(kalanlar)}")
    
    return gecenler, kalanlar

# Test edelim
ogrenciler = ["Ali", "Veli", "Ayşe", "Fatma"]
matematik = [75, 45, 85, 65]
fizik = [80, 50, 90, 70]
kimya = [70, 40, 88, 60]

gecenler, kalanlar = ogrenci_raporu_olustur(ogrenciler, matematik, fizik, kimya)

#######################
# 10. PERFORMANS VE OPTİMİZASYON
#######################

print("\n=== Performans ve Optimizasyon ===")

# zip vs manuel indeksleme karşılaştırması
liste1 = [1, 2, 3, 4, 5]
liste2 = ['a', 'b', 'c', 'd', 'e']

print("Manuel indeksleme (önerilmez):")
for i in range(len(liste1)):
    print(f"{liste1[i]} - {liste2[i]}")

print("\nzip kullanımı (önerilen):")
for sayi, harf in zip(liste1, liste2):
    print(f"{sayi} - {harf}")

print("\nHangisi daha okunabilir? zip! ✓")

# Büyük listelerle çalışma
print("\nBüyük listelerle çalışırken zip hafıza dostu:")
buyuk_liste1 = range(1000000)
buyuk_liste2 = range(1000000, 2000000)

# zip bir generator döndürür, hafızada yer kaplamaz
zip_nesnesi = zip(buyuk_liste1, buyuk_liste2)
print("zip nesnesi oluşturuldu (hafızada yer kaplamaz)")

# İlk 5 elemanı göster
print("İlk 5 eleman:")
for i, (a, b) in enumerate(zip_nesnesi):
    if i >= 5:
        break
    print(f"{a} - {b}")

#######################
# 11. GELIŞMIŞ ZIP KULLANIM ALANLARI
#######################

print("\n=== Gelişmiş zip Kullanım Alanları ===")

# Matris transpozlama (satır-sütun değişimi)
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Orijinal matris:")
for satir in matris:
    print(satir)

print("\nTranspoze matris:")
transpoze = list(zip(*matris))
for satir in transpoze:
    print(list(satir))

print()

# Paralel hesaplama
x_degerler = [1, 2, 3, 4, 5]
y_degerler = [2, 4, 6, 8, 10]

print("Paralel matematik işlemleri:")
for x, y in zip(x_degerler, y_degerler):
    toplam = x + y
    carpim = x * y
    print(f"x={x}, y={y} → toplam={toplam}, çarpım={carpim}")

#######################
# 12. HATA DURUMLARI VE DİKKAT EDİLECEKLER
#######################

print("\n=== Hata Durumları ve Dikkat Edilecekler ===")

print("1. Farklı uzunluktaki listeler:")
liste_a = [1, 2, 3, 4, 5]
liste_b = ['a', 'b']
print(f"Liste A uzunluğu: {len(liste_a)}")
print(f"Liste B uzunluğu: {len(liste_b)}")
print("zip sonucu:", list(zip(liste_a, liste_b)))
print("DİKKAT: Fazla elemanlar kaybolur!")

print("\n2. Boş liste durumu:")
bos_liste = []
dolu_liste = [1, 2, 3]
print("Boş liste + dolu liste:", list(zip(bos_liste, dolu_liste)))

print("\n3. Tek elementli listeler:")
tek_element_1 = [100]
tek_element_2 = [200]
print("Tek elementli listeler:", list(zip(tek_element_1, tek_element_2)))

#######################
# 13. ÖZET VE EN İYİ PRATİKLER
#######################

print("\n=== Özet ve En İyi Praktikler ===")

print("zip fonksiyonu:")
print("✓ Birden fazla listeyi paralel işlemek için kullanılır")
print("✓ En kısa liste uzunluğuna göre çalışır")
print("✓ Tuple'lar halinde sonuç döndürür")
print("✓ Hafıza dostu bir generator döndürür")

print("\nNe zaman zip kullanmalı:")
print("• Aynı indeksteki elemanları birlikte işlemek")
print("• Sözlük oluşturmak (key-value eşleştirme)")
print("• Paralel hesaplama yapmak")
print("• Veri tablolarını işlemek")

print("\nEn iyi pratikler:")
print("• Manuel indeksleme yerine zip kullanın")
print("• Farklı uzunluktaki listeler için dikkatli olun")
print("• Unzip için * operatörünü kullanın")
print("• enumerate ile birlikte kullanarak sıra numarası ekleyin")

print("\n=== Bu Derste Öğrendiklerimiz ===")
print("✓ zip() fonksiyonunun temel kullanımı")
print("✓ Birden fazla listeyi paralel işleme")
print("✓ Sözlük oluşturma teknikleri")
print("✓ Unzip işlemi ve * operatörü")
print("✓ enumerate ile birlikte kullanım")
print("✓ Pratik uygulama örnekleri")
print("✓ Performans ve optimizasyon ipuçları")
print("✓ Yaygın hatalar ve çözümleri")

print("\n=== Kullanılan Kavramlar ===")
print("• zip() fonksiyonu")
print("• Tuple unpacking")
print("• dict() ile sözlük oluşturma")
print("• * operatörü (unpack)")
print("• enumerate() ile birlikte kullanım")
print("• Generator objeler")

print("\nSıradaki ders: Lambda, map ve filter fonksiyonları")
