# =======================================================
# PYTHON DERS 4: print() FONKSIYONU VE FORMATLAMA
# =======================================================

# Önceki derslerde matematiksel işlemler, veri türleri ve tip dönüşümleri öğrendik.
# Bu derste print() fonksiyonunu daha ayrıntılı öğreneceğiz.

# Öğreneceğiniz konular:
#   - print() fonksiyonunun temel kullanımı
#   - Birden fazla değeri yazdırma
#   - sep parametresi (ayırıcı)
#   - end parametresi (satır sonu)
#   - Özel karakterler (\n, \t)
#   - Basit metin birleştirme

print("Python print() Fonksiyonu Dersine Hoş Geldiniz!")


# =======================================================
# 1. TEMEL print() KULLANIMI
# =======================================================
print("1. TEMEL print() KULLANIMI")
print("---------------------------")

# Basit metin yazdırma
print("Merhaba Dünya!")
print("Python öğreniyorum")

# Sayıları yazdırma
print(42)
print(3.14)

# Değişkenleri yazdırma
isim = "Ahmet"
yas = 25
print(isim)
print(yas)

print("Temel kullanım tamamlandı!")


# =======================================================
# 2. BİRDEN FAZLA DEĞER YAZDIRMA
# =======================================================
print("2. BİRDEN FAZLA DEĞER YAZDIRMA")
print("-------------------------------")

# Virgülle ayırarak birden fazla değer yazdırabiliriz
print("İsim:", isim)
print("Yaş:", yas)
print("İsim:", isim, "Yaş:", yas)

# Farklı türde veriler birlikte yazdırılabilir
print("Sonuç:", 5 + 3)
print("Pi sayısı:", 3.14, "Yaklaşık değer")

print("Birden fazla değer yazdırma tamamlandı!")


# =======================================================
# 3. sep PARAMETRESİ (AYIRICI)
# =======================================================
print("3. sep PARAMETRESİ (AYIRICI)")
print("-----------------------------")

# Varsayılan olarak değerler arasında boşluk vardır
print("Elma", "Armut", "Kiraz")

# sep parametresi ile ayırıcıyı değiştirebiliriz
print("Elma", "Armut", "Kiraz", sep=" - ")
print("2024", "12", "25", sep="/")
print("Python", "Java", "C++", sep=" | ")

# Ayırıcı olarak boş string de kullanabilirsiniz
print("A", "B", "C", sep="")  # ABC

print("sep parametresi tamamlandı!")


# =======================================================
# 4. end PARAMETRESİ (SATIR SONU)
# =======================================================
print("4. end PARAMETRESİ (SATIR SONU)")
print("--------------------------------")

# Varsayılan olarak print() her seferinde yeni satıra geçer
print("Birinci satır")
print("İkinci satır")

# end parametresi ile satır sonu karakterini değiştirebiliriz
print("Bu metin", end=" ")
print("aynı satırda devam eder")

print("Sayı:", end=" ")
print(42)

# end ile farklı karakterler kullanabiliriz
print("Python", end=" >>> ")
print("Harika bir dil!")

print("end parametresi tamamlandı!")

# =======================================================
# 5. ÖZEL KARAKTERLER
# =======================================================
print("5. ÖZEL KARAKTERLER")
print("--------------------")

# \n = Yeni satır karakteri
print("Birinci satır\nİkinci satır")
print("Üçüncü satır\nDördüncü satır")

# \t = Tab (sekme) karakteri  
print("İsim:\tAhmet")
print("Yaş:\t25")
print("Şehir:\tİstanbul")

# Bu karakterleri bildiğiniz metinlerle de kullanabilirsiniz
print("Python\tprogramlama\tdili")
print("Satır 1\nSatır 2\nSatır 3")

print("Özel karakterler tamamlandı!")


# =======================================================
# 6. METİN BİRLEŞTİRME
# =======================================================
print("6. METİN BİRLEŞTİRME")
print("---------------------")

# + operatörü ile metinleri birleştirebiliriz
ad = "Mehmet"
soyad = "Yılmaz"
tam_isim = ad + " " + soyad
print("Tam isim:", tam_isim)

# Sayıları metinle birleştirmek için str() gerekir
yas = 30
mesaj = "Yaşım " + str(yas) + " dir."
print(mesaj)

# Virgülle ayırarak yazdırmak daha kolaydır
print("Adım", ad, "ve yaşım", yas)

print("Metin birleştirme tamamlandı!")


# =======================================================
# 7. PRATİK UYGULAMALAR
# =======================================================
print("7. PRATİK UYGULAMALAR")
print("----------------------")

# Uygulama 1: Kişi bilgilerini yazdırma
kisi_adi = "Ayşe"
kisi_yasi = 28
kisi_sehri = "Ankara"

print("=== KİŞİ BİLGİLERİ ===")
print("Ad:", kisi_adi)
print("Yaş:", kisi_yasi)
print("Şehir:", kisi_sehri)

# Uygulama 2: Hesaplama sonuçlarını yazdırma
sayi1 = 15
sayi2 = 7
toplam = sayi1 + sayi2
fark = sayi1 - sayi2

print("=== HESAPLAMA SONUÇLARI ===")
print("Birinci sayı:", sayi1)
print("İkinci sayı:", sayi2)
print("Toplam:", toplam)
print("Fark:", fark)

# Uygulama 3: Düzenli çıktı
print("=== ÜRÜN LİSTESİ ===")
print("Ürün\t\tFiyat")
print("Elma\t\t5 TL")
print("Armut\t\t8 TL") 
print("Kiraz\t\t15 TL")

print("Pratik uygulamalar tamamlandı!")


# =======================================================
# DERS ÖZET
# =======================================================
print("DERS ÖZETİ")
print("-----------")
print("Bu derste öğrendiğiniz print() özellikleri:")
print("1. Basit metin ve sayı yazdırma")
print("2. Birden fazla değeri virgülle ayırarak yazdırma")
print("3. sep parametresi - değerler arası ayırıcı")
print("4. end parametresi - satır sonu karakteri")
print("5. Özel karakterler: \\n (yeni satır), \\t (tab)")
print("6. + operatörü ile metin birleştirme")
print("7. str() ile sayıları metne çevirme")

print("print() FONKSIYONU DERSİ TAMAMLANDI!")
print("Sonraki ders: Tam sayılarla ileri düzey işlemleri öğreneceğiz.")
