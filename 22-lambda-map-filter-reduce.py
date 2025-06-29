###############################################
# 22. DERS: LAMBDA, MAP VE FILTER FONKSİYONLARI
###############################################

# Bu derste öğreneceğimiz konular:
# - Lambda fonksiyonları (kısa fonksiyon tanımlama)
# - map() fonksiyonu (listeler üzerinde toplu işlem)
# - filter() fonksiyonu (listeden seçim yapma)
# - Bu fonksiyonların pratik uygulamaları

print("=== LAMBDA, MAP VE FILTER FONKSİYONLARI ===")

#######################
# 1. LAMBDA FONKSİYONLARI
#######################

print("\n=== Lambda Fonksiyonları ===")

# Lambda kısa, tek satırlık fonksiyon tanımlamak için kullanılır
# def ile normal fonksiyon vs lambda ile kısa fonksiyon

print("Normal fonksiyon tanımlama:")
def topla(a, b):
    return a + b

print("5 + 3 =", topla(5, 3))

print("\nLambda ile aynı işlev:")
lambda_topla = lambda a, b: a + b
print("7 + 4 =", lambda_topla(7, 4))

print("\nLambda syntaxı: lambda parametreler: ifade")

# Daha fazla lambda örneği
print("\nFarklı lambda örnekleri:")

# Sayının karesi
kare_al = lambda x: x * x
print("5'in karesi:", kare_al(5))

# Sayının çift mi kontrolü
cift_mi = lambda x: x % 2 == 0
print("8 çift mi?", cift_mi(8))
print("7 çift mi?", cift_mi(7))

# String'i büyük harfe çevirme
buyuk_harf = lambda metin: metin.upper()
print("'python' büyük harfle:", buyuk_harf("python"))

# İki sayının büyüğünü bulma
buyuk_olan = lambda a, b: a if a > b else b
print("15 ve 23'ün büyüğü:", buyuk_olan(15, 23))

#######################
# 2. LAMBDA NE ZAMAN KULLANILIR?
#######################

print("\n=== Lambda Ne Zaman Kullanılır? ===")

print("Lambda kullanım alanları:")
print("✓ Kısa, tek satırlık işlemler")
print("✓ map() ve filter() ile birlikte")
print("✓ Geçici fonksiyon ihtiyaçları")
print("✓ Basit matematik işlemleri")

print("\nLambda kullanılmaması gereken durumlar:")
print("✗ Karmaşık, çok satırlı işlemler")
print("✗ Çok kez kullanılacak fonksiyonlar")
print("✗ Hata kontrolü gereken durumlar")

# Karşılaştırma örneği
print("\nKarşılaştırma örneği:")

# Basit işlem - lambda uygun
print("Lambda ile (uygun):")
fahrenheit_cevir = lambda celsius: (celsius * 9/5) + 32
print("25°C =", fahrenheit_cevir(25), "°F")

# Karmaşık işlem - normal fonksiyon daha iyi
print("\nNormal fonksiyon ile (daha uygun):")
def sicaklik_degerlendirme(celsius):
    fahrenheit = (celsius * 9/5) + 32
    if celsius < 0:
        durum = "Donuyor"
    elif celsius < 15:
        durum = "Soğuk"
    elif celsius < 25:
        durum = "Ilık"
    else:
        durum = "Sıcak"
    
    return f"{celsius}°C = {fahrenheit}°F ({durum})"

print(sicaklik_degerlendirme(25))

#######################
# 3. MAP FONKSİYONU
#######################

print("\n=== map() Fonksiyonu ===")

# map() bir listedeki tüm elemanlara aynı fonksiyonu uygular

sayilar = [1, 2, 3, 4, 5]
print("Orijinal liste:", sayilar)

# Normal yöntem: for döngüsü ile
print("\nFor döngüsü ile kareleri alma:")
kareler_manuel = []
for sayi in sayilar:
    kareler_manuel.append(sayi * sayi)
print("Kareler:", kareler_manuel)

# map() ile aynı işlem
print("\nmap() ile kareleri alma:")
kareler_map = list(map(lambda x: x * x, sayilar))
print("Kareler:", kareler_map)

print("\nmap() syntaxı: map(fonksiyon, liste)")

# Başka map örnekleri
print("\nDaha fazla map örneği:")

# String'leri büyük harfe çevirme
kelimeler = ["python", "java", "javascript", "go"]
print("Orijinal:", kelimeler)
buyuk_kelimeler = list(map(lambda x: x.upper(), kelimeler))
print("Büyük harfle:", buyuk_kelimeler)

# Sayıları 2 ile çarpma
print("\nSayıları 2 ile çarpma:")
cift_katlar = list(map(lambda x: x * 2, sayilar))
print("Orijinal:", sayilar)
print("2 katı:", cift_katlar)

# Float'a çevirme
string_sayilar = ["10", "20", "30", "40"]
print("\nString'leri float'a çevirme:")
print("String'ler:", string_sayilar)
float_sayilar = list(map(float, string_sayilar))
print("Float'lar:", float_sayilar)

#######################
# 4. NORMAL FONKSİYON İLE MAP
#######################

print("\n=== Normal Fonksiyon ile map ===")

# map() sadece lambda ile değil, normal fonksiyonlarla da kullanılır

def faiz_hesapla(anapara):
    """5% faiz hesaplama"""
    return anapara * 1.05

bakiyeler = [1000, 2500, 5000, 7500, 10000]
print("Ana paralar:", bakiyeler)

faizli_bakiyeler = list(map(faiz_hesapla, bakiyeler))
print("Faizli bakiyeler:", faizli_bakiyeler)

# Başka bir örnek
def notlari_harflendir(puan):
    """Notları harf sistemine çevirir"""
    if puan >= 90:
        return "AA"
    elif puan >= 80:
        return "BA"
    elif puan >= 70:
        return "BB"
    elif puan >= 60:
        return "CB"
    else:
        return "FF"

puanlar = [95, 87, 76, 64, 52, 88]
print("\nPuanlar:", puanlar)
harf_notlari = list(map(notlari_harflendir, puanlar))
print("Harf notları:", harf_notlari)

#######################
# 5. FILTER FONKSİYONU
#######################

print("\n=== filter() Fonksiyonu ===")

# filter() bir listeden belirli koşulu sağlayan elemanları seçer

tum_sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Tüm sayılar:", tum_sayilar)

# Normal yöntem: for döngüsü ile
print("\nFor döngüsü ile çift sayıları bulma:")
cift_sayilar_manuel = []
for sayi in tum_sayilar:
    if sayi % 2 == 0:
        cift_sayilar_manuel.append(sayi)
print("Çift sayılar:", cift_sayilar_manuel)

# filter() ile aynı işlem
print("\nfilter() ile çift sayıları bulma:")
cift_sayilar_filter = list(filter(lambda x: x % 2 == 0, tum_sayilar))
print("Çift sayılar:", cift_sayilar_filter)

print("\nfilter() syntaxı: filter(koşul_fonksiyonu, liste)")

# Daha fazla filter örneği
print("\nDaha fazla filter örneği:")

# 5'ten büyük sayılar
buyuk_sayilar = list(filter(lambda x: x > 5, tum_sayilar))
print("5'ten büyük sayılar:", buyuk_sayilar)

# Tek sayılar
tek_sayilar = list(filter(lambda x: x % 2 == 1, tum_sayilar))
print("Tek sayılar:", tek_sayilar)

# String örnekleri
isimler = ["Ahmet", "Ayşe", "Mehmet", "Ali", "Fatma", "Can"]
print("\nİsimler:", isimler)

# 4 harften uzun isimler
uzun_isimler = list(filter(lambda x: len(x) > 4, isimler))
print("4 harften uzun isimler:", uzun_isimler)

# A harfi ile başlayan isimler
a_ile_baslayanlar = list(filter(lambda x: x.startswith("A"), isimler))
print("A ile başlayan isimler:", a_ile_baslayanlar)

#######################
# 6. NORMAL FONKSİYON İLE FILTER
#######################

print("\n=== Normal Fonksiyon ile filter ===")

def basarili_mi(not_degeri):
    """Öğrenci başarılı mı kontrol eder"""
    return not_degeri >= 70

ogrenci_notlari = [85, 62, 78, 45, 92, 67, 88, 54]
print("Tüm notlar:", ogrenci_notlari)

basarili_notlar = list(filter(basarili_mi, ogrenci_notlari))
print("Başarılı notlar:", basarili_notlar)

# Başka bir örnek
def yetiskin_mi(yas):
    """18 yaş üstü mü kontrol eder"""
    return yas >= 18

yaslar = [15, 22, 17, 25, 16, 19, 14, 21]
print("\nYaşlar:", yaslar)

yetiskin_yaslar = list(filter(yetiskin_mi, yaslar))
print("Yetişkin yaşlar:", yetiskin_yaslar)

#######################
# 7. MAP VE FILTER BİRLİKTE
#######################

print("\n=== map ve filter Birlikte ===")

# Önce filter ile seçim, sonra map ile işlem

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Orijinal sayılar:", sayilar)

# Adım 1: Çift sayıları seç
cift_sayilar = list(filter(lambda x: x % 2 == 0, sayilar))
print("Çift sayılar:", cift_sayilar)

# Adım 2: Çift sayıların karelerini al
cift_sayilarin_kareleri = list(map(lambda x: x * x, cift_sayilar))
print("Çift sayıların kareleri:", cift_sayilarin_kareleri)

# Tek komutla yapma
print("\nTek komutla (filter + map):")
sonuc = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, sayilar)))
print("Çift sayıların kareleri:", sonuc)

#######################
# 8. PRATİK UYGULAMA ÖRNEKLERİ
#######################

print("\n=== Pratik Uygulama Örnekleri ===")

# Örnek 1: Maaş sistemi
print("Maaş sistemi uygulaması:")
calisanlar = [
    {"ad": "Ahmet", "maas": 8000, "departman": "IT"},
    {"ad": "Ayşe", "maas": 12000, "departman": "Pazarlama"},
    {"ad": "Mehmet", "maas": 6000, "departman": "İnsan Kaynakları"},
    {"ad": "Fatma", "maas": 15000, "departman": "IT"},
    {"ad": "Can", "maas": 9000, "departman": "Satış"}
]

# IT departmanındaki çalışanları bul
it_calisanlari = list(filter(lambda c: c["departman"] == "IT", calisanlar))
print("IT çalışanları:")
for calisan in it_calisanlari:
    print(f"  {calisan['ad']}: {calisan['maas']} TL")

# Tüm maaşlara %10 zam yap
zamlı_maaslar = list(map(lambda c: c["maas"] * 1.1, calisanlar))
print("\n%10 zamlı maaşlar:", [int(maas) for maas in zamlı_maaslar])

print()

# Örnek 2: Öğrenci sistemi
ogrenciler = [
    {"ad": "Ali", "notlar": [85, 90, 78]},
    {"ad": "Veli", "notlar": [92, 88, 95]},
    {"ad": "Ayşe", "notlar": [76, 82, 79]},
    {"ad": "Fatma", "notlar": [68, 75, 72]}
]

# Her öğrencinin ortalamasını hesapla
ortalamalar = list(map(lambda o: {"ad": o["ad"], "ortalama": sum(o["notlar"])/len(o["notlar"])}, ogrenciler))

print("Öğrenci ortalamaları:")
for org in ortalamalar:
    print(f"  {org['ad']}: {org['ortalama']:.1f}")

# 80 üstü ortalamaya sahip öğrenciler
basarili_ogrenciler = list(filter(lambda o: o["ortalama"] >= 80, ortalamalar))
print("\nBaşarılı öğrenciler (80+ ortalama):")
for ogrenci in basarili_ogrenciler:
    print(f"  {ogrenci['ad']}: {ogrenci['ortalama']:.1f}")

#######################
# 9. PERFORMANS KARŞILAŞTIRMASI
#######################

print("\n=== Performans Karşılaştırması ===")

# Büyük liste ile test
buyuk_liste = list(range(1, 1001))  # 1'den 1000'e kadar

print("1'den 1000'e kadar sayılarla test:")

# For döngüsü yöntemi
print("For döngüsü ile çift sayıların karelerini alma:")
sonuc_dongu = []
for sayi in buyuk_liste:
    if sayi % 2 == 0:
        sonuc_dongu.append(sayi * sayi)

print(f"İlk 5 sonuç: {sonuc_dongu[:5]}")
print(f"Toplam çift sayı: {len(sonuc_dongu)}")

# map + filter yöntemi
print("\nmap + filter ile:")
sonuc_functional = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, buyuk_liste)))
print(f"İlk 5 sonuç: {sonuc_functional[:5]}")
print(f"Toplam çift sayı: {len(sonuc_functional)}")

print("İki yöntem de aynı sonucu verir!")

#######################
# 10. EN İYİ PRATİKLER VE İPUÇLARI
#######################

print("\n=== En İyi Praktikler ve İpuçları ===")

print("Lambda kullanımında:")
print("✓ Kısa ve basit işlemler için kullanın")
print("✓ Tek satırda ifade edilebiliyorsa uygun")
print("✓ map() ve filter() ile birlikte etkili")
print("✗ Karmaşık işlemler için normal fonksiyon tercih edin")

print("\nmap() kullanımında:")
print("✓ Tüm elemanlara aynı işlem uygulamak için")
print("✓ Tip dönüşümü işlemleri için (str, int, float)")
print("✓ Hesaplama işlemleri için")
print("✗ Koşullu işlemler için filter() kullanın")

print("\nfilter() kullanımında:")
print("✓ Koşula göre eleman seçimi için")
print("✓ Veri temizleme işlemleri için")
print("✓ Boolean döndüren fonksiyonlarla")
print("✗ İşlem uygulamak için map() kullanın")

print("\nOkunabilirlik:")
print("• Karmaşık lambda'lar yerine normal fonksiyon kullanın")
print("• Çok iç içe map/filter'dan kaçının")
print("• Değişken isimleri anlamlı olsun")

#######################
# 11. ÖZET VE KARŞILAŞTIRMA
#######################

print("\n=== Özet ve Karşılaştırma ===")

test_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Aynı işlemi farklı yöntemlerle yapma:")
print("Görev: Çift sayıları seç ve karelerini al")

# Yöntem 1: For döngüsü (anlaşılır)
print("\n1. For döngüsü:")
sonuc1 = []
for sayi in test_liste:
    if sayi % 2 == 0:
        sonuc1.append(sayi * sayi)
print("Sonuç:", sonuc1)

# Yöntem 2: List comprehension (Python'ik)
print("\n2. List comprehension:")
sonuc2 = [sayi * sayi for sayi in test_liste if sayi % 2 == 0]
print("Sonuç:", sonuc2)

# Yöntem 3: map + filter (fonksiyonel)
print("\n3. map + filter:")
sonuc3 = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, test_liste)))
print("Sonuç:", sonuc3)

print("\nÜç yöntem de aynı sonucu verir!")
print("Hangi yöntemi seçmeli?")
print("• Başlangıç seviyesi: For döngüsü")
print("• Python deneyimi: List comprehension")
print("• Fonksiyonel programlama: map/filter")

print("\n=== Bu Derste Öğrendiklerimiz ===")
print("✓ Lambda fonksiyonları ve kısa fonksiyon tanımlama")
print("✓ map() ile listeler üzerinde toplu işlem")
print("✓ filter() ile koşullu eleman seçimi")
print("✓ Normal fonksiyon vs lambda karşılaştırması")
print("✓ map ve filter'in birlikte kullanımı")
print("✓ Pratik uygulama örnekleri")
print("✓ Performans karşılaştırması")
print("✓ En iyi pratikler ve kullanım alanları")

print("\n=== Kullanılan Kavramlar ===")
print("• lambda fonksiyonları")
print("• map() fonksiyonu")
print("• filter() fonksiyonu")
print("• list() ile generator'ları listeye çevirme")
print("• Fonksiyonel programlama yaklaşımı")

print("\nSıradaki ders: List comprehensions - Listelerle ileri teknikler")
