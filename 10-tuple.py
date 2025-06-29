# =======================================================
# PYTHON DERS 10: TUPLE (DEMET)
# =======================================================

# Önceki derste listeleri öğrendik.
# Bu derste tuple (demet) veri türünü öğreneceğiz.
# Tuple, liste gibi birden fazla veri saklayabilir ama değiştirilemez.

# Öğreneceğiniz konular:
#   - Tuple oluşturma
#   - Tuple ve liste farkları
#   - Tuple elemanlarına erişim
#   - Tuple'ın değiştirilemez özelliği
#   - Tuple metodları
#   - Pratik uygulama örnekleri

print("Python Tuple Dersine Hoş Geldiniz!")


# =======================================================
# 1. TUPLE OLUŞTURMA
# =======================================================
print("1. TUPLE OLUŞTURMA")
print("-------------------")

# Tuple'lar parantez () ile oluşturulur
bos_tuple = ()                          # Boş tuple
sayilar = (1, 2, 3, 4, 5)              # Sayı tuple'ı
isimler = ("Ali", "Ayşe", "Mehmet")     # Metin tuple'ı
karisik = (1, "iki", 3.0, True)        # Karışık türde tuple

print("Boş tuple:", bos_tuple)
print("Sayılar tuple'ı:", sayilar)
print("İsimler tuple'ı:", isimler)
print("Karışık tuple:", karisik)

# Tek elemanlı tuple oluştururken virgül gerekir!
tek_eleman = (42,)                      # Virgül olmadan (42) sayı olur
print("Tek elemanlı tuple:", tek_eleman)

# type() ile türlerini kontrol edelim
print("sayilar'ın türü:", type(sayilar))
print("tek_eleman'ın türü:", type(tek_eleman))

print("Tuple oluşturma tamamlandı!")


# =======================================================
# 2. TUPLE VE LİSTE FARKLARI
# =======================================================
print("2. TUPLE VE LİSTE FARKLARI")
print("----------------------------")

# Liste [] ile oluşturulur, tuple () ile
liste_ornek = [1, 2, 3]
tuple_ornek = (1, 2, 3)

print("Liste örneği:", liste_ornek, "- Türü:", type(liste_ornek))
print("Tuple örneği:", tuple_ornek, "- Türü:", type(tuple_ornek))

# Liste değiştirilebilir (mutable)
liste_ornek[0] = 100
print("Liste değiştirildikten sonra:", liste_ornek)

# Tuple değiştirilemez (immutable) 
# tuple_ornek[0] = 100  # Bu HATA verir!
print("Tuple değiştirilemez:", tuple_ornek)

print("Tuple ve liste farkları tamamlandı!")


# =======================================================
# 3. TUPLE ELEMANLERINA ERİŞİM
# =======================================================
print("3. TUPLE ELEMANLERINA ERİŞİM")
print("------------------------------")

# Tuple elemanlarına da indekslerle erişilir (liste gibi)
meyveler = ("elma", "armut", "muz", "kiraz")
print("Meyve tuple'ı:", meyveler)
print()

# Pozitif indekslerle erişim
print("İlk meyve (0. indeks):", meyveler[0])      # elma
print("İkinci meyve (1. indeks):", meyveler[1])   # armut
print("Üçüncü meyve (2. indeks):", meyveler[2])   # muz

# Negatif indekslerle erişim
print("Son meyve (-1. indeks):", meyveler[-1])    # kiraz
print("Sondan 2. meyve (-2. indeks):", meyveler[-2])  # muz

print("Tuple elemanlarına erişim tamamlandı!")


# =======================================================
# 4. TUPLE'IN DEĞİŞTİRİLEMEZ ÖZELLİĞİ
# =======================================================
print("4. TUPLE'IN DEĞİŞTİRİLEMEZ ÖZELLİĞİ")
print("-------------------------------------")

koordinatlar = (10, 20)
print("Koordinatlar:", koordinatlar)

# Bu işlemler HATA verir:
# koordinatlar[0] = 30        # Eleman değiştirme - HATA!
# koordinatlar.append(30)     # Eleman ekleme - HATA!
# koordinatlar.remove(10)     # Eleman silme - HATA!

print("Tuple elemanları değiştirilemez, eklenemez, silinemez!")

# Neden tuple kullanırız?
# 1. Verinin değişmemesini garanti eder
# 2. Liste'den daha hızlıdır
# 3. Dictionary'de anahtar olarak kullanılabilir

print("Tuple'ın değiştirilemez özelliği tamamlandı!")


# =======================================================
# 5. TUPLE UZUNLUĞU VE KONTROL
# =======================================================
print("5. TUPLE UZUNLUĞU VE KONTROL")
print("-----------------------------")

# len() fonksiyonu tuple uzunluğunu verir
renkler = ("kırmızı", "mavi", "yeşil", "sarı")
print("Renkler tuple'ı:", renkler)
print("Tuple uzunluğu:", len(renkler))

# 'in' operatörü ile eleman varlığı kontrol edilir
print("'mavi' var mı?", "mavi" in renkler)      # True
print("'mor' var mı?", "mor" in renkler)        # False

print("Tuple uzunluğu ve kontrol tamamlandı!")


# =======================================================
# 6. TUPLE METODLARI
# =======================================================
print("6. TUPLE METODLARI")
print("-------------------")

# Tuple'ın sadece 2 metodu vardır (değiştirilemez olduğu için)
sayilar = (1, 2, 3, 2, 4, 2, 5)
print("Sayılar tuple'ı:", sayilar)

# count() metodu: Belirtilen değerin kaç kez geçtiğini sayar
print("2 sayısı kaç kez var?", sayilar.count(2))      # 3
print("5 sayısı kaç kez var?", sayilar.count(5))      # 1
print("9 sayısı kaç kez var?", sayilar.count(9))      # 0

# index() metodu: Belirtilen değerin ilk indeksini verir
print("2 sayısının ilk indeksi:", sayilar.index(2))   # 1
print("4 sayısının indeksi:", sayilar.index(4))       # 4

print("Tuple metodları tamamlandı!")


# =======================================================
# 7. PRATİK UYGULAMALAR
# =======================================================
print("7. PRATİK UYGULAMALAR")
print("----------------------")

# Uygulama 1: Koordinat sistemi
nokta1 = (3, 5)
nokta2 = (7, 2)
print("=== KOORDİNAT SİSTEMİ ===")
print("1. nokta:", nokta1)
print("2. nokta:", nokta2)
print("1. noktanın x koordinatı:", nokta1[0])
print("1. noktanın y koordinatı:", nokta1[1])

# Uygulama 2: RGB renk kodları
kirmizi = (255, 0, 0)
yesil = (0, 255, 0)
mavi = (0, 0, 255)
print("\n=== RGB RENK KODLARI ===")
print("Kırmızı:", kirmizi)
print("Yeşil:", yesil)
print("Mavi:", mavi)

# Uygulama 3: Öğrenci bilgileri (değişmemesi gereken veriler)
ogrenci1 = ("Ali", "Veli", 12345, "Bilgisayar Mühendisliği")
print("\n=== ÖĞRENCİ BİLGİLERİ ===")
print("Ad:", ogrenci1[0])
print("Soyad:", ogrenci1[1])
print("Numara:", ogrenci1[2])
print("Bölüm:", ogrenci1[3])

# Uygulama 4: Aylar (değişmeyen veri)
aylar = ("Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
         "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık")
print("\n=== AYLAR ===")
print("1. ay:", aylar[0])
print("6. ay:", aylar[5])
print("Son ay:", aylar[-1])
print("Toplam ay sayısı:", len(aylar))

print("Pratik uygulamalar tamamlandı!")


# =======================================================
# DERS ÖZET
# =======================================================
print("DERS ÖZETİ")
print("-----------")
print("Bu derste öğrendiğiniz tuple özellikleri:")
print("1. Tuple'lar () ile oluşturulur")
print("2. Tuple değiştirilemez (immutable), liste değiştirilebilir")
print("3. Tek elemanlı tuple için virgül gerekir: (42,)")
print("4. İndekslerle erişim liste ile aynı")
print("5. len() ile uzunluk, 'in' ile eleman kontrolü")
print("6. count() ve index() metodları vardır")
print("7. Koordinat, renk kodu gibi değişmeyen veriler için ideal")

print("TUPLE DERSİ TAMAMLANDI!")
print("Sonraki ders: Sözlükler (dictionary) veri türünü öğreneceğiz.")
