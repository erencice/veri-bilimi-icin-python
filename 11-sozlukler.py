# =======================================================
# PYTHON DERS 11: SÖZLÜKLER (dictionary)
# =======================================================

# Önceki derste tuple'ları öğrendik.
# Bu derste sözlük (dictionary) veri türünü öğreneceğiz.
# Sözlükler anahtar-değer çiftlerini saklar.

# Öğreneceğiniz konular:
#   - Sözlük oluşturma
#   - Anahtar-değer çiftleri
#   - Sözlük elemanlarına erişim
#   - Sözlüğe eleman ekleme/çıkarma
#   - Sözlük metodları
#   - Pratik uygulama örnekleri

print("Python Sözlükler Dersine Hoş Geldiniz!")


# =======================================================
# 1. SÖZLÜK OLUŞTURMA
# =======================================================
print("1. SÖZLÜK OLUŞTURMA")
print("--------------------")

# Sözlükler süslü parantez {} ile oluşturulur
# Anahtar : Değer şeklinde çiftler halinde yazılır
bos_sozluk = {}                        # Boş sözlük

kisi = {
    "ad": "Ahmet",
    "soyad": "Yılmaz", 
    "yas": 25,
    "sehir": "İstanbul"
}

urun = {
    "isim": "Laptop",
    "fiyat": 15000,
    "stok": True,
    "marka": "Dell"
}

print("Boş sözlük:", bos_sozluk)
print("Kişi sözlüğü:", kisi)
print("Ürün sözlüğü:", urun)

# type() ile türlerini kontrol edelim
print("kisi'nin türü:", type(kisi))
print("urun'ün türü:", type(urun))

print("Sözlük oluşturma tamamlandı!")


# =======================================================
# 2. SÖZLÜK ELEMANLERINA ERİŞİM
# =======================================================
print("2. SÖZLÜK ELEMANLERINA ERİŞİM")
print("-------------------------------")

# Köşeli parantez içinde anahtar adını yazarak erişim
print("Kişi bilgileri:")
print("Ad:", kisi["ad"])
print("Soyad:", kisi["soyad"])
print("Yaş:", kisi["yas"])
print("Şehir:", kisi["sehir"])

print("\nÜrün bilgileri:")
print("İsim:", urun["isim"])
print("Fiyat:", urun["fiyat"])
print("Stok durumu:", urun["stok"])

print("Sözlük elemanlarına erişim tamamlandı!")


# =======================================================
# 3. get() METODUYLa GÜVENLİ ERİŞİM
# =======================================================
print("3. get() METODUYLA GÜVENLİ ERİŞİM")
print("----------------------------------")

# get() metodu ile güvenli erişim
# Anahtar yoksa hata vermez, None döner
print("Ad (get ile):", kisi.get("ad"))
print("Telefon (get ile):", kisi.get("telefon"))  # None döner

# Varsayılan değer belirtebiliriz
print("Telefon (varsayılan değerle):", kisi.get("telefon", "Kayıtlı değil"))

# Direkt erişimde olmayan anahtar hata verir:
# print(kisi["telefon"])  # KeyError hatası!

print("get() metoduyla güvenli erişim tamamlandı!")


# =======================================================
# 4. SÖZLÜĞE ELEMAN EKLEME VE GÜNCELLEME
# =======================================================
print("4. SÖZLÜĞE ELEMAN EKLEME VE GÜNCELLEME")
print("---------------------------------------")

# Yeni anahtar-değer çifti ekleme
kisi["telefon"] = "555-1234"
kisi["email"] = "ahmet@email.com"

print("Telefon eklendikten sonra:", kisi)

# Mevcut değeri güncelleme
kisi["yas"] = 26
print("Yaş güncellendikten sonra:", kisi["yas"])

# Birden fazla güncelleme
urun["fiyat"] = 14000
urun["renk"] = "Siyah"
print("Ürün güncellenmiş hali:", urun)

print("Sözlüğe eleman ekleme ve güncelleme tamamlandı!")


# =======================================================
# 5. SÖZLÜKTEN ELEMAN ÇIKARMA
# =======================================================
print("5. SÖZLÜKTEN ELEMAN ÇIKARMA")
print("-----------------------------")

# pop() metodu ile eleman çıkarma
çıkarılan_email = kisi.pop("email")
print("Çıkarılan email:", çıkarılan_email)
print("Email çıkarıldıktan sonra:", kisi)

# del anahtar kelimesi ile silme
del kisi["telefon"]
print("Telefon silindikten sonra:", kisi)

print("Sözlükten eleman çıkarma tamamlandı!")


# =======================================================
# 6. SÖZLÜK UZUNLUĞU VE KONTROL
# =======================================================
print("6. SÖZLÜK UZUNLUĞU VE KONTROL")
print("------------------------------")

# len() fonksiyonu kaç anahtar olduğunu söyler
print("Kişi sözlüğü uzunluğu:", len(kisi))
print("Ürün sözlüğü uzunluğu:", len(urun))

# 'in' operatörü ile anahtar varlığı kontrol edilir
print("'ad' anahtarı var mı?", "ad" in kisi)          # True
print("'telefon' anahtarı var mı?", "telefon" in kisi)  # False
print("'fiyat' anahtarı var mı?", "fiyat" in urun)     # True

print("Sözlük uzunluğu ve kontrol tamamlandı!")


# =======================================================
# 7. SÖZLÜK METODLARI
# =======================================================
print("7. SÖZLÜK METODLARI")
print("--------------------")

# keys() metodu: Tüm anahtarları verir
print("Kişi anahtarları:", list(kisi.keys()))

# values() metodu: Tüm değerleri verir
print("Kişi değerleri:", list(kisi.values()))

# items() metodu: Anahtar-değer çiftlerini verir
print("Kişi öğeleri:", list(kisi.items()))

# clear() metodu: Tüm elemanları siler
test_sozluk = {"a": 1, "b": 2}
print("Temizlemeden önce:", test_sozluk)
test_sozluk.clear()
print("Temizledikten sonra:", test_sozluk)

print("Sözlük metodları tamamlandı!")


# =======================================================
# 8. PRATİK UYGULAMALAR
# =======================================================
print("8. PRATİK UYGULAMALAR")
print("----------------------")

# Uygulama 1: Öğrenci not sistemi
ogrenci = {
    "ad": "Zeynep",
    "numara": 12345,
    "matematik": 85,
    "fizik": 78,
    "kimya": 92
}

print("=== ÖĞRENCİ NOT SİSTEMİ ===")
print("Öğrenci adı:", ogrenci["ad"])
print("Numara:", ogrenci["numara"])
print("Matematik notu:", ogrenci["matematik"])
print("Fizik notu:", ogrenci["fizik"])
print("Kimya notu:", ogrenci["kimya"])

# Not ortalaması hesaplama
toplam = ogrenci["matematik"] + ogrenci["fizik"] + ogrenci["kimya"]
ortalama = toplam / 3
print("Not ortalaması:", round(ortalama, 2))

# Uygulama 2: Stok takip sistemi
stok = {
    "elma": 50,
    "armut": 30,
    "muz": 25,
    "kiraz": 15
}

print("\n=== STOK TAKİP SİSTEMİ ===")
print("Elma stoğu:", stok["elma"])
print("Toplam meyve çeşidi:", len(stok))

# Satış sonrası stok güncelleme
stok["elma"] = stok["elma"] - 10  # 10 kilo elma satıldı
print("Satış sonrası elma stoğu:", stok["elma"])

# Uygulama 3: Şirket çalışan bilgileri
calisan = {
    "ad": "Mehmet",
    "departman": "Yazılım",
    "maas": 15000,
    "deneyim_yili": 5,
    "dil_seviyeleri": {
        "Python": "İleri",
        "JavaScript": "Orta",
        "SQL": "İleri"
    }
}

print("\n=== ÇALIŞAN BİLGİLERİ ===")
print("Ad:", calisan["ad"])
print("Departman:", calisan["departman"])
print("Maaş:", calisan["maas"])
print("Python seviyesi:", calisan["dil_seviyeleri"]["Python"])

print("Pratik uygulamalar tamamlandı!")


# =======================================================
# DERS ÖZET
# =======================================================
print("DERS ÖZETİ")
print("-----------")
print("Bu derste öğrendiğiniz sözlük özellikleri:")
print("1. Sözlükler {} ile oluşturulur")
print("2. Anahtar:değer çiftleri saklar")
print("3. Anahtarlarla erişim: sozluk['anahtar']")
print("4. get() metodu güvenli erişim sağlar")
print("5. Yeni eleman ekleme: sozluk['yeni'] = değer")
print("6. pop() ve del ile eleman silme")
print("7. len() uzunluk, 'in' ile anahtar kontrolü")
print("8. keys(), values(), items() metodları")
print("9. İç içe sözlükler kullanılabilir")

print("SÖZLÜKLER DERSİ TAMAMLANDI!")
print("Sonraki ders: Kümeler (set) veri türünü öğreneceğiz.")