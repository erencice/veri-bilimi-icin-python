# =======================================================
# PYTHON DERS 9: LİSTELER (list)
# =======================================================

# Önceki derste mantıksal değerleri öğrendik.
# Bu derste birden fazla veriyi saklamak için listeleri öğreneceğiz.

# Öğreneceğiniz konular:
#   - Liste oluşturma
#   - Liste elemanlarına erişim
#   - Liste uzunluğu bulma
#   - Listeye eleman ekleme
#   - Listeden eleman çıkarma
#   - Pratik uygulama örnekleri

print("Python Listeler Dersine Hoş Geldiniz!")


# =======================================================
# 1. LİSTE OLUŞTURMA
# =======================================================
print("1. LİSTE OLUŞTURMA")
print("-------------------")

# Listeler köşeli parantez [] ile oluşturulur
bos_liste = []               # Boş liste
sayilar = [1, 2, 3, 4, 5]    # Sayı listesi
isimler = ["Ali", "Ayşe", "Mehmet"]  # Metin listesi
karisik = [1, "iki", 3.0, True]      # Karışık türde liste

print("Boş liste:", bos_liste)
print("Sayılar listesi:", sayilar)
print("İsimler listesi:", isimler)
print("Karışık liste:", karisik)

# type() ile türlerini kontrol edelim
print("sayilar'ın türü:", type(sayilar))
print("isimler'in türü:", type(isimler))

print("Liste oluşturma tamamlandı!")


# =======================================================
# 2. LİSTE ELEMANLERINA ERİŞİM
# =======================================================
print("2. LİSTE ELEMANLERINA ERİŞİM")
print("------------------------------")

# İndeksler 0'dan başlar
meyveler = ["elma", "armut", "muz", "kiraz"]
print("Meyve listesi:", meyveler)
print()

# Pozitif indekslerle erişim
print("İlk meyve (0. indeks):", meyveler[0])      # elma
print("İkinci meyve (1. indeks):", meyveler[1])   # armut
print("Üçüncü meyve (2. indeks):", meyveler[2])   # muz

# Negatif indekslerle erişim (sondan başlar)
print("Son meyve (-1. indeks):", meyveler[-1])    # kiraz
print("Sondan 2. meyve (-2. indeks):", meyveler[-2])  # muz

print("Liste elemanlarına erişim tamamlandı!")


# =======================================================
# 3. LİSTE UZUNLUĞU BULMA
# =======================================================
print("3. LİSTE UZUNLUĞU BULMA")
print("------------------------")

# len() fonksiyonu listenin kaç elemana sahip olduğunu söyler
sayilar = [10, 20, 30, 40, 50]
renkler = ["kırmızı", "mavi", "yeşil"]
bos = []

print("Sayılar listesi:", sayilar)
print("Sayılar listesi uzunluğu:", len(sayilar))

print("Renkler listesi:", renkler) 
print("Renkler listesi uzunluğu:", len(renkler))

print("Boş liste uzunluğu:", len(bos))

print("Liste uzunluğu bulma tamamlandı!")


# =======================================================
# 4. LİSTEYE ELEMAN EKLEME
# =======================================================
print("4. LİSTEYE ELEMAN EKLEME")
print("-------------------------")

# append() metodu listenin sonuna eleman ekler
hayvanlar = ["kedi", "köpek"]
print("Başlangıç listesi:", hayvanlar)

hayvanlar.append("kuş")
print("'kuş' eklendikten sonra:", hayvanlar)

hayvanlar.append("balık")
print("'balık' eklendikten sonra:", hayvanlar)

# insert() metodu belirli bir konuma eleman ekler
hayvanlar.insert(0, "aslan")  # 0. indekse (başa) ekle
print("'aslan' başa eklendikten sonra:", hayvanlar)

hayvanlar.insert(2, "tavşan")  # 2. indekse ekle
print("'tavşan' 2. indekse eklendikten sonra:", hayvanlar)

print("Listeye eleman ekleme tamamlandı!")


# =======================================================
# 5. LİSTEDEN ELEMAN ÇIKARMA
# =======================================================
print("5. LİSTEDEN ELEMAN ÇIKARMA")
print("----------------------------")

# remove() metodu belirtilen elemanı listeden çıkarır
sehirler = ["İstanbul", "Ankara", "İzmir", "Bursa"]
print("Başlangıç listesi:", sehirler)

sehirler.remove("Ankara")
print("'Ankara' çıkarıldıktan sonra:", sehirler)

# pop() metodu belirtilen indeksteki elemanı çıkarır ve döndürür
cikartilan = sehirler.pop()  # Son elemanı çıkarır
print("Son eleman çıkarıldı:", cikartilan)
print("Liste son hali:", sehirler)

# Belirli indeksten çıkarma
ikinci_eleman = sehirler.pop(1)  # 1. indeksteki elemanı çıkar
print("1. indeksten çıkarılan:", ikinci_eleman)
print("Liste son hali:", sehirler)

print("Listeden eleman çıkarma tamamlandı!")


# =======================================================
# 6. LİSTE KONTROLÜ
# =======================================================
print("6. LİSTE KONTROLÜ")
print("------------------")

# 'in' operatörü ile listede eleman var mı kontrolü
notlar = [85, 92, 78, 96, 88]
print("Notlar listesi:", notlar)

print("85 notu var mı?", 85 in notlar)      # True
print("90 notu var mı?", 90 in notlar)      # False
print("100 notu var mı?", 100 in notlar)    # False

# Metin listesi ile kontrol
diller = ["Python", "Java", "C++", "JavaScript"]
print("Diller listesi:", diller)

print("'Python' var mı?", "Python" in diller)    # True
print("'C#' var mı?", "C#" in diller)             # False

print("Liste kontrolü tamamlandı!")


# =======================================================
# 7. PRATİK UYGULAMALAR
# =======================================================
print("7. PRATİK UYGULAMALAR")
print("----------------------")

# Uygulama 1: Alışveriş listesi
alisveris = []
print("=== ALIŞVERİŞ LİSTESİ ===")
print("Başlangıç:", alisveris)

alisveris.append("ekmek")
alisveris.append("süt")
alisveris.append("yumurta")
print("Ürünler eklendikten sonra:", alisveris)
print("Toplam ürün sayısı:", len(alisveris))

# Uygulama 2: Öğrenci notları
notlar = [75, 82, 90, 68, 95]
print("\n=== ÖĞRENCİ NOTLARI ===")
print("Notlar:", notlar)
print("En yüksek not:", max(notlar))  # max() en büyük değeri bulur
print("En düşük not:", min(notlar))   # min() en küçük değeri bulur
print("Toplam:", sum(notlar))         # sum() toplamı bulur
print("Ortalama:", sum(notlar) / len(notlar))

# Uygulama 3: Kullanıcı listesi yönetimi
kullanicilar = ["admin", "user1", "user2"]
print("\n=== KULLANICI YÖNETİMİ ===")
print("Mevcut kullanıcılar:", kullanicilar)

kullanicilar.append("user3")
print("Yeni kullanıcı eklendi:", kullanicilar)

kullanicilar.remove("user1")
print("user1 silindi:", kullanicilar)

print("admin var mı?", "admin" in kullanicilar)

print("Pratik uygulamalar tamamlandı!")


# =======================================================
# DERS ÖZET
# =======================================================
print("DERS ÖZETİ")
print("-----------")
print("Bu derste öğrendiğiniz liste özellikleri:")
print("1. Listeler [] ile oluşturulur")
print("2. İndeksler 0'dan başlar")
print("3. Negatif indeksler sondan başlar")
print("4. len() liste uzunluğunu verir")
print("5. append() sona eleman ekler")
print("6. insert() belirli konuma eleman ekler")
print("7. remove() belirtilen elemanı siler")
print("8. pop() belirtilen indeksteki elemanı siler ve döndürür")
print("9. 'in' operatörü ile eleman varlığı kontrol edilir")
print("10. max(), min(), sum() faydalı fonksiyonlar")

print("LİSTELER DERSİ TAMAMLANDI!")
print("Sonraki ders: Tuple (demet) veri türünü öğreneceğiz.")