###############################################
# 25. DERS: UYGULAMALAR VE ÖRNEKLERİ
###############################################

# Bu derste öğreneceğimiz konular:
# - Şimdiye kadar öğrenilen konuların pratiği
# - Gerçek hayat benzeri problemler
# - Fonksiyon, döngü, comprehension kombinasyonları
# - Veri işleme uygulamaları

print("=== UYGULAMALAR VE ÖRNEKLERİ ===")

# Bu derste şimdiye kadar öğrendiğimiz tüm konuları bir araya getireceğiz

#######################
# 1. ÖĞRENCİ DERS YÖNETİM SİSTEMİ
#######################

print("\n=== Öğrenci Ders Yönetim Sistemi ===")

# Öğrenci bilgileri
ogrenciler = {
    "Ali": {"Matematik": 85, "Fizik": 78, "Kimya": 92},
    "Veli": {"Matematik": 67, "Fizik": 89, "Kimya": 76},
    "Ayşe": {"Matematik": 94, "Fizik": 87, "Kimya": 91},
    "Mehmet": {"Matematik": 73, "Fizik": 65, "Kimya": 88},
    "Fatma": {"Matematik": 89, "Fizik": 95, "Kimya": 83}
}

print("Öğrenci bilgileri:")
for ogrenci, notlar in ogrenciler.items():
    print(f"{ogrenci}: {notlar}")

# Öğrenci ortalamalarını hesaplama
def ogrenci_ortalamasi(notlar):
    """Öğrencinin not ortalamasını hesaplar"""
    return sum(notlar.values()) / len(notlar.values())

ogrenci_ortalamalari = {
    ogrenci: ogrenci_ortalamasi(notlar) 
    for ogrenci, notlar in ogrenciler.items()
}

print("\nÖğrenci ortalamaları:")
for ogrenci, ortalama in ogrenci_ortalamalari.items():
    print(f"{ogrenci}: {ortalama:.1f}")

# Ders ortalamalarını hesaplama
dersler = ["Matematik", "Fizik", "Kimya"]
ders_ortalamalari = {}

for ders in dersler:
    ders_notlari = [ogrenciler[ogrenci][ders] for ogrenci in ogrenciler.keys()]
    ders_ortalamalari[ders] = sum(ders_notlari) / len(ders_notlari)

print("\nDers ortalamaları:")
for ders, ortalama in ders_ortalamalari.items():
    print(f"{ders}: {ortalama:.1f}")

# En başarılı öğrenci
en_basarili = max(ogrenci_ortalamalari, key=ogrenci_ortalamalari.get)
print(f"\nEn başarılı öğrenci: {en_basarili} ({ogrenci_ortalamalari[en_basarili]:.1f})")

# Geçen öğrenciler (ortalama 70+)
gecen_ogrenciler = [
    ogrenci for ogrenci, ortalama in ogrenci_ortalamalari.items() 
    if ortalama >= 70
]
print(f"Geçen öğrenciler: {gecen_ogrenciler}")

#######################
# 2. ÜRÜN SATIŞ ANALİZİ
#######################

print("\n=== Ürün Satış Analizi ===")

# Aylık satış verileri
satis_verileri = {
    "Ocak": {"Laptop": 45, "Telefon": 120, "Tablet": 67, "Kulaklık": 89},
    "Şubat": {"Laptop": 52, "Telefon": 135, "Tablet": 71, "Kulaklık": 95},
    "Mart": {"Laptop": 38, "Telefon": 98, "Tablet": 59, "Kulaklık": 102},
    "Nisan": {"Laptop": 61, "Telefon": 156, "Tablet": 84, "Kulaklık": 78}
}

# Ürün fiyatları
urun_fiyatlari = {
    "Laptop": 5000,
    "Telefon": 3000,
    "Tablet": 2000,
    "Kulaklık": 500
}

print("Aylık satış miktarları:")
for ay, satislar in satis_verileri.items():
    print(f"{ay}: {satislar}")

# Toplam satış miktarları (tüm aylar)
toplam_satislar = {}
for urun in urun_fiyatlari.keys():
    toplam_satislar[urun] = sum(satis_verileri[ay][urun] for ay in satis_verileri.keys())

print("\nToplam satış miktarları:")
for urun, miktar in toplam_satislar.items():
    print(f"{urun}: {miktar} adet")

# Aylık gelir hesaplama
aylik_gelirler = {}
for ay, satislar in satis_verileri.items():
    aylik_gelir = sum(miktar * urun_fiyatlari[urun] for urun, miktar in satislar.items())
    aylik_gelirler[ay] = aylik_gelir

print("\nAylık gelirler:")
for ay, gelir in aylik_gelirler.items():
    print(f"{ay}: {gelir:,} TL")

# En çok satılan ürün
en_cok_satan = max(toplam_satislar, key=toplam_satislar.get)
print(f"\nEn çok satılan ürün: {en_cok_satan} ({toplam_satislar[en_cok_satan]} adet)")

# En karlı ay
en_karli_ay = max(aylik_gelirler, key=aylik_gelirler.get)
print(f"En karlı ay: {en_karli_ay} ({aylik_gelirler[en_karli_ay]:,} TL)")

#######################
# 3. METİN ANALİZİ UYGULAMASI
#######################

print("\n=== Metin Analizi Uygulaması ===")

metin = """
Python programlama dili çok güçlü ve esnek bir dildir. 
Python ile web geliştirme, veri analizi, makine öğrenmesi ve
daha birçok alanda çalışabilirsiniz. Python öğrenmek kolay
ve eğlencelidir. Python topluluğu çok yardımcıdır.
"""

print("Analiz edilen metin:")
print(metin.strip())

# Metni temizle ve kelimelere ayır
temiz_metin = metin.lower().replace(",", "").replace(".", "").replace("\n", " ")
kelimeler = temiz_metin.split()
kelimeler = [kelime for kelime in kelimeler if kelime]  # Boş stringleri kaldır

print(f"\nToplam kelime sayısı: {len(kelimeler)}")

# Benzersiz kelimeler
benzersiz_kelimeler = list(set(kelimeler))
print(f"Benzersiz kelime sayısı: {len(benzersiz_kelimeler)}")

# Kelime frekansları
kelime_frekanslari = {}
for kelime in kelimeler:
    if kelime in kelime_frekanslari:
        kelime_frekanslari[kelime] += 1
    else:
        kelime_frekanslari[kelime] = 1

# En sık kullanılan kelimeler (dict comprehension ile)
kelime_frekanslari_sirali = {
    kelime: frekans for kelime, frekans in 
    sorted(kelime_frekanslari.items(), key=lambda x: x[1], reverse=True)
}

print("\nKelime frekansları (ilk 10):")
sayac = 0
for kelime, frekans in kelime_frekanslari_sirali.items():
    if sayac >= 10:
        break
    print(f"{kelime}: {frekans}")
    sayac += 1

# Uzun kelimeler (5+ harf)
uzun_kelimeler = [kelime for kelime in benzersiz_kelimeler if len(kelime) >= 5]
print(f"\nUzun kelimeler (5+ harf): {uzun_kelimeler}")

#######################
# 4. SAYISAL ANALİZ UYGULAMASI
#######################

print("\n=== Sayısal Analiz Uygulaması ===")

# Rastgele sayı listesi
sayilar = [23, 45, 12, 67, 89, 34, 56, 78, 90, 11, 25, 43, 65, 87, 32]

print(f"Sayı listesi: {sayilar}")

# Temel istatistikler
def istatistik_hesapla(liste):
    """Liste için temel istatistikleri hesaplar"""
    return {
        "toplam": sum(liste),
        "ortalama": sum(liste) / len(liste),
        "minimum": min(liste),
        "maksimum": max(liste),
        "adet": len(liste)
    }

istatistikler = istatistik_hesapla(sayilar)
print("\nTemel istatistikler:")
for istatistik, deger in istatistikler.items():
    if isinstance(deger, float):
        print(f"{istatistik}: {deger:.2f}")
    else:
        print(f"{istatistik}: {deger}")

# Sayıları kategorilere ayırma
kategoriler = {
    "küçük": [sayi for sayi in sayilar if sayi < 30],
    "orta": [sayi for sayi in sayilar if 30 <= sayi < 70],
    "büyük": [sayi for sayi in sayilar if sayi >= 70]
}

print("\nKategoriler:")
for kategori, kategori_sayilari in kategoriler.items():
    print(f"{kategori}: {kategori_sayilari} (Adet: {len(kategori_sayilari)})")

# Çift ve tek sayılar
cift_sayilar = [sayi for sayi in sayilar if sayi % 2 == 0]
tek_sayilar = [sayi for sayi in sayilar if sayi % 2 == 1]

print(f"\nÇift sayılar: {cift_sayilar}")
print(f"Tek sayılar: {tek_sayilar}")

#######################
# 5. LİSTE MANIPÜLASYONU PROJESİ
#######################

print("\n=== Liste Manipülasyonu Projesi ===")

# Çok boyutlu liste
matris = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Orijinal matris:")
for satir in matris:
    print(satir)

# Matrisi düz listeye çevir
duz_liste = [eleman for satir in matris for eleman in satir]
print(f"\nDüz liste: {duz_liste}")

# Satır toplamları
satir_toplamlari = [sum(satir) for satir in matris]
print(f"Satır toplamları: {satir_toplamlari}")

# Sütun toplamları
sutun_toplamlari = [sum(matris[i][j] for i in range(len(matris))) for j in range(len(matris[0]))]
print(f"Sütun toplamları: {sutun_toplamlari}")

# Köşegen elemanları
kosegen = [matris[i][i] for i in range(len(matris))]
print(f"Ana köşegen: {kosegen}")

# Çift sayıların konumları
cift_konumlar = [(i, j) for i in range(len(matris)) for j in range(len(matris[0])) if matris[i][j] % 2 == 0]
print(f"Çift sayıların konumları: {cift_konumlar}")

print("\n=== Bu Derste Uyguladıklarımız ===")
print("✓ Öğrenci ders yönetim sistemi")
print("✓ Ürün satış analizi")
print("✓ Metin analizi uygulaması")
print("✓ Sayısal analiz uygulaması")
print("✓ Liste manipülasyonu projesi")
print("✓ Dictionary ve list comprehension kombinasyonları")
print("✓ Fonksiyon ve döngü kullanımları")
print("✓ Gerçek hayat benzeri problemler")

print("\nSıradaki ders: Ödevler ve Pratik Sorular")
