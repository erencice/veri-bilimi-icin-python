###############################################
# 23. DERS: LIST COMPREHENSIONS (LISTE KAVRAMA)
###############################################

# Bu derste öğreneceğimiz konular:
# - List comprehension temel kullanımı
# - Koşullu list comprehension (if-else)
# - Birden fazla döngüde list comprehension
# - Performans avantajları ve best practices

print("=== LIST COMPREHENSIONS (LISTE KAVRAMA) ===")

# List comprehension: Listeyi tek satırda oluşturmanın pratik yolu
# Normal for döngüsünün daha kısa ve okunabilir hali

#######################
# 1. TEMEL LIST COMPREHENSION
#######################

print("\n=== Temel List Comprehension ===")

# Basit bir listeyle başlayalım
sayilar = [1, 2, 3, 4, 5]

# Normal yöntem: For döngüsü ile kareler
kareler_normal = []
for sayi in sayilar:
    kareler_normal.append(sayi ** 2)
print("Normal for döngüsü ile kareler:", kareler_normal)

# List comprehension ile kareler (tek satır!)
kareler_comprehension = [sayi ** 2 for sayi in sayilar]
print("List comprehension ile kareler:", kareler_comprehension)

# Başka örnekler
print("\nBaşka örnekler:")
print("Sayıları 2 ile çarpma:", [sayi * 2 for sayi in sayilar])
print("Sayıları 10 ile toplama:", [sayi + 10 for sayi in sayilar])

# String listesi ile işlemler
isimler = ["ahmet", "mehmet", "ayşe", "fatma"]
print("\nİsimleri büyük harfe çevirme:", [isim.upper() for isim in isimler])
print("İsim uzunlukları:", [len(isim) for isim in isimler])

#######################
# 2. KOŞULLU LIST COMPREHENSION (IF KULLANIMI)
#######################

print("\n=== Koşullu List Comprehension ===")

# Sadece çift sayıları alma
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Normal yöntem
cift_sayilar_normal = []
for sayi in sayilar:
    if sayi % 2 == 0:
        cift_sayilar_normal.append(sayi)
print("Normal yöntemle çift sayılar:", cift_sayilar_normal)

# List comprehension ile (if sonda kullanılır)
cift_sayilar = [sayi for sayi in sayilar if sayi % 2 == 0]
print("List comprehension ile çift sayılar:", cift_sayilar)

# Başka koşullu örnekler
print("5'ten büyük sayılar:", [sayi for sayi in sayilar if sayi > 5])
print("Tek sayıların kareleri:", [sayi ** 2 for sayi in sayilar if sayi % 2 == 1])

#######################
# 3. IF-ELSE KOMBINASYONU
#######################

print("\n=== If-Else Kombinasyonu ===")

# Çift sayıları 2 ile çarp, tek sayıları 3 ile çarp
sayilar = [1, 2, 3, 4, 5, 6]

# Normal yöntem
sonuclar_normal = []
for sayi in sayilar:
    if sayi % 2 == 0:
        sonuclar_normal.append(sayi * 2)
    else:
        sonuclar_normal.append(sayi * 3)
print("Normal yöntem:", sonuclar_normal)

# List comprehension ile (if-else ifadesi başta kullanılır)
sonuclar = [sayi * 2 if sayi % 2 == 0 else sayi * 3 for sayi in sayilar]
print("List comprehension:", sonuclar)

# Daha fazla örnek
notlar = [45, 67, 89, 23, 95, 78]
gecme_durumu = ["Geçti" if notum >= 50 else "Kaldı" for notum in notlar]
print("Geçme durumları:", gecme_durumu)

#######################
# 4. STRING İŞLEMLERİ
#######################

print("\n=== String İşlemleri ===")

kelimeler = ["python", "java", "javascript", "c++", "go"]

# Uzun kelimeleri (5+ harf) büyük harfe çevir
uzun_kelimeler = [kelime.upper() if len(kelime) >= 5 else kelime for kelime in kelimeler]
print("Uzun kelimeler büyük:", uzun_kelimeler)

# Sadece 'a' harfi içeren kelimeleri al
a_iceren = [kelime for kelime in kelimeler if 'a' in kelime]
print("'a' harfi içeren kelimeler:", a_iceren)

#######################
# 5. İÇ İÇE LIST COMPREHENSION
#######################

print("\n=== İç İçe List Comprehension ===")

# 2 boyutlu liste (matris) oluşturma
matris = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Çarpım tablosu matrisi:")
for satir in matris:
    print(satir)

# Düz listeye çevirme
sayilar_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
duz_liste = [sayi for satir in sayilar_2d for sayi in satir]
print("\n2D listeden düz liste:", duz_liste)

#######################
# 6. FONKSİYON İLE KULLANIM
#######################

print("\n=== Fonksiyon ile Kullanım ===")

def kare_al(x):
    """Sayının karesini döndürür"""
    return x ** 2

def cift_mi(x):
    """Sayının çift olup olmadığını kontrol eder"""
    return x % 2 == 0

sayilar = [1, 2, 3, 4, 5, 6, 7, 8]

# Fonksiyon kullanarak
kareler = [kare_al(sayi) for sayi in sayilar]
print("Fonksiyon ile kareler:", kareler)

# Fonksiyon koşulu ile
cift_sayilar = [sayi for sayi in sayilar if cift_mi(sayi)]
print("Fonksiyon koşulu ile çift sayılar:", cift_sayilar)

#######################
# 7. PERFORMANS KARŞILAŞTIRMASI
#######################

print("\n=== Performans Karşılaştırması ===")

# List comprehension genellikle daha hızlıdır
# Çünkü C seviyesinde optimize edilmiştir

print("List comprehension avantajları:")
print("• Daha kısa ve okunabilir kod")
print("• Daha hızlı çalışma")
print("• Tek satırda liste oluşturma")
print("• Pythonic kod yazımı")

# Format özetleri
print("\nList Comprehension formatları:")
print("Temel: [ifade for öğe in liste]")
print("Koşullu filtre: [ifade for öğe in liste if koşul]")
print("If-else: [doğru_ifade if koşul else yanlış_ifade for öğe in liste]")

#######################
# 8. PRATİK ÖRNEKLER
#######################

print("\n=== Pratik Örnekler ===")

# Örnek 1: Sıcaklık dönüştürme (Celsius'tan Fahrenheit'a)
celsius = [0, 20, 30, 40, 100]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print("Celsius -> Fahrenheit:", list(zip(celsius, fahrenheit)))

# Örnek 2: Kelime sayısı
cumle = "Python öğrenmek çok eğlenceli ve kullanışlı"
kelime_uzunlukları = [len(kelime) for kelime in cumle.split()]
print("Kelime uzunlukları:", kelime_uzunlukları)

# Örnek 3: Sadece pozitif sayılar
karma_sayilar = [-5, -2, 0, 3, 7, -1, 8]
pozitif_sayilar = [sayi for sayi in karma_sayilar if sayi > 0]
print("Pozitif sayılar:", pozitif_sayilar)

# Örnek 4: Dictionary'den liste
ogrenciler = {"Ali": 85, "Veli": 92, "Ayşe": 78, "Fatma": 95}
basarili_ogrenciler = [isim for isim, notum in ogrenciler.items() if notum >= 80]
print("Başarılı öğrenciler:", basarili_ogrenciler)

#######################
# 9. LAMBDA İLE KOMBINASYON
#######################

print("\n=== Lambda ile Kombinasyon ===")

# Lambda fonksiyonları list comprehension ile kullanabiliriz
sayilar = [1, 2, 3, 4, 5]

# Lambda ile kare alma
kare_lambda = lambda x: x ** 2
kareler_lambda = [kare_lambda(sayi) for sayi in sayilar]
print("Lambda ile kareler:", kareler_lambda)

# Direkt lambda kullanımı
kareler_direkt = [(lambda x: x ** 2)(sayi) for sayi in sayilar]
print("Direkt lambda kullanımı:", kareler_direkt)

#######################
# 10. EN İYİ PRATİKLER
#######################

print("\n=== En İyi Pratikler ===")

print("✓ Basit işlemler için list comprehension kullanın")
print("✓ Karmaşık mantık için normal for döngüsü tercih edin")
print("✓ Okunabilirliği her zaman önceleyın")
print("✓ Çok uzun list comprehension'ları parçalayın")
print("✓ İç içe list comprehension'da dikkatli olun")

# Kötü örnek: Çok karmaşık
# result = [x*2 if x%2==0 else x*3 if x%3==0 else x*5 for x in range(10) if x>0]

# İyi örnek: Basit ve anlaşılır
sayilar = [x for x in range(10) if x > 0]
result = []
for sayi in sayilar:
    if sayi % 2 == 0:
        result.append(sayi * 2)
    elif sayi % 3 == 0:
        result.append(sayi * 3)
    else:
        result.append(sayi * 5)

print("Temiz kod örneği:", result)

print("\n=== Bu Derste Öğrendiklerimiz ===")
print("✓ List comprehension temel kullanımı")
print("✓ Koşullu filtreleme (if)")
print("✓ If-else kombinasyonları")
print("✓ String işlemleri")
print("✓ İç içe list comprehension")
print("✓ Fonksiyon ve lambda kombinasyonları")
print("✓ Performans avantajları")
print("✓ En iyi pratikler")

print("\nSıradaki ders: Dictionary Comprehensions")
