# =======================================================
# PYTHON DERS 7: METİN İFADELERİ (string)
# =======================================================

# Önceki derste ondalıklı sayıları öğrendik.
# Bu derste metinlerle (string) çalışmayı öğreneceğiz.

# Öğreneceğiniz konular:
#   - String oluşturma ve özellikleri
#   - Metin uzunluğu bulma
#   - Metinleri birleştirme
#   - Temel string metodları
#   - Pratik uygulama örnekleri

print("Python Metin İfadeleri Dersine Hoş Geldiniz!")


# =======================================================
# 1. STRİNG OLUŞTURMA VE ÖZELLİKLERİ
# =======================================================
print("1. STRİNG OLUŞTURMA VE ÖZELLİKLERİ")
print("------------------------------------")

# Stringler tek veya çift tırnak ile oluşturulur
isim = "Ahmet"
soyisim = 'Yılmaz'
mesaj = "Python öğreniyorum!"
bos_metin = ""

print("İsim:", isim)
print("Soyisim:", soyisim)
print("Mesaj:", mesaj)
print("Boş metin:", bos_metin)

# type() ile türlerini kontrol edelim
print("isim'in türü:", type(isim))
print("mesaj'ın türü:", type(mesaj))
print("bos_metin'in türü:", type(bos_metin))

print("String oluşturma tamamlandı!")


# =======================================================
# 2. METİN UZUNLUĞU BULMA - len()
# =======================================================
print("2. METİN UZUNLUĞU BULMA - len()")
print("---------------------------------")

# len() fonksiyonu metnin kaç karakterden oluştuğunu söyler
ad = "Mehmet"
uzun_metin = "Python programlama dili"
bosluk = "   "

print("'Mehmet' kelimesinin uzunluğu:", len(ad))
print("'Python programlama dili' cümlesinin uzunluğu:", len(uzun_metin))
print("'   ' (3 boşluk) uzunluğu:", len(bosluk))
print("Boş metin uzunluğu:", len(""))

print("Metin uzunluğu bulma tamamlandı!")


# =======================================================
# 3. METİNLERİ BİRLEŞTİRME
# =======================================================
print("3. METİNLERİ BİRLEŞTİRME")
print("-------------------------")

# + operatörü ile metinleri birleştirebiliriz
ad = "Ali"
soyad = "Veli"
tam_isim = ad + " " + soyad  # Arada boşluk ekledik

print("Ad:", ad)
print("Soyad:", soyad)
print("Tam isim:", tam_isim)

# Sayıları metinle birleştirmek için str() gerekir
yas = 25
tanitim = "Benim adım " + ad + " ve yaşım " + str(yas)
print("Tanıtım:", tanitim)

# Daha kolay yol: print() içinde virgül kullanmak
print("Benim adım", ad, "ve yaşım", yas)

print("Metinleri birleştirme tamamlandı!")


# =======================================================
# 4. TEMEL STRİNG METODLARİ
# =======================================================
print("4. TEMEL STRİNG METODLARİ")
print("--------------------------")

metin = "python programlama dili"
print("Orijinal metin:", metin)

# upper() - tüm harfleri büyük yapar
buyuk_harf = metin.upper()
print("Büyük harfle:", buyuk_harf)

# lower() - tüm harfleri küçük yapar  
kucuk_harf = "PYTHON PROGRAMLAMA DİLİ".lower()
print("Küçük harfle:", kucuk_harf)

# capitalize() - ilk harfi büyük yapar
bas_harf = metin.capitalize()
print("İlk harf büyük:", bas_harf)

# replace() - kelime değiştirme
yeni_metin = metin.replace("python", "Java")
print("Python yerine Java:", yeni_metin)

print("Temel string metodları tamamlandı!")


# =======================================================
# 5. METİN KONTROLÜ
# =======================================================
print("5. METİN KONTROLÜ")
print("------------------")

cumle = "Python öğrenmek çok eğlenceli"
print("Kontrol edilen cümle:", cumle)

# Belirli bir kelime var mı kontrolü
python_var_mi = "Python" in cumle
java_var_mi = "Java" in cumle

print("'Python' kelimesi var mı?", python_var_mi)  # True
print("'Java' kelimesi var mı?", java_var_mi)      # False

# Cümle belirli kelime ile başlıyor mu?
python_ile_basliyor = cumle.startswith("Python")
print("'Python' ile başlıyor mu?", python_ile_basliyor)  # True

# Cümle belirli kelime ile bitiyor mu?
eglenceli_ile_bitiyor = cumle.endswith("eğlenceli")
print("'eğlenceli' ile bitiyor mu?", eglenceli_ile_bitiyor)  # True

print("Metin kontrolü tamamlandı!")


# =======================================================
# 6. PRATİK UYGULAMALAR
# =======================================================
print("6. PRATİK UYGULAMALAR")
print("----------------------")

# Uygulama 1: Kullanıcı bilgileri
kullanici_adi = "ahmet_123"
kullanici_email = "ahmet@email.com"

print("=== KULLANICI BİLGİLERİ ===")
print("Kullanıcı adı:", kullanici_adi)
print("E-mail:", kullanici_email)
print("Kullanıcı adı uzunluğu:", len(kullanici_adi), "karakter")

# Uygulama 2: Şifre kontrolü
sifre = "Python123"
print("\n=== ŞİFRE KONTROLÜ ===")
print("Şifre:", sifre)
print("Şifre uzunluğu:", len(sifre))
print("8 karakterden uzun mu?", len(sifre) > 8)
print("'Python' içeriyor mu?", "Python" in sifre)

# Uygulama 3: Dosya adı işleme
dosya_adi = "veriler.txt"
print("\n=== DOSYA ADI İŞLEME ===")
print("Dosya adı:", dosya_adi)
print("'.txt' ile bitiyor mu?", dosya_adi.endswith(".txt"))
print("Dosya adını büyük harfle:", dosya_adi.upper())

# Uygulama 4: Metni temizleme
kirli_metin = "  Python Programlama  "
temiz_metin = kirli_metin.strip()  # strip() başta ve sondaki boşlukları siler
print("\n=== METİN TEMİZLEME ===")
print("Kirli metin: '" + kirli_metin + "'")
print("Temiz metin: '" + temiz_metin + "'")

print("\nPratik uygulamalar tamamlandı!")


# =======================================================
# DERS ÖZET
# =======================================================
print("DERS ÖZETİ")
print("-----------")
print("Bu derste öğrendiğiniz string özellikleri:")
print("1. Stringler tek (') veya çift (\") tırnak ile oluşturulur")
print("2. len() fonksiyonu metin uzunluğunu verir")
print("3. + operatörü ile metinler birleştirilir")
print("4. upper(), lower(), capitalize() harfleri değiştirir")
print("5. replace() ile kelime değiştirme yapılır")
print("6. 'in' operatörü ile metin içinde arama yapılır")
print("7. startswith() ve endswith() ile başlangıç/bitiş kontrolü")
print("8. strip() başta ve sondaki boşlukları siler")

print("METİN İFADELERİ DERSİ TAMAMLANDI!")
print("Sonraki ders: Mantıksal değerleri (bool) öğreneceğiz.")

