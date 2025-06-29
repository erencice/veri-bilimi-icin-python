###############################################
# 27. DERS: HATA YAKALAMA (TRY-EXCEPT)
###############################################

# Bu derste öğreneceğimiz konular:
# - try-except yapısı
# - Farklı hata türleri
# - else ve finally blokları
# - Hata mesajlarını yakalama
# - Manuel hata fırlatma (raise)

print("=== HATA YAKALAMA (TRY-EXCEPT) ===")

# Programda hatalar kaçınılmazdır
# Hata yakalama ile programımızın çökmesini engelleriz

#######################
# 1. TEMEL TRY-EXCEPT YAPISI
#######################

print("\n=== Temel Try-Except Yapısı ===")

# Hatalı kod örneği (çökme riski)
print("Hatalı kod örneği:")
try:
    # Hata oluşabilecek kod
    sonuc = 10 / 0
    print("Sonuç:", sonuc)
except ZeroDivisionError:
    # Hata durumunda çalışacak kod
    print("Hata: Sıfıra bölme yapılamaz!")

print("Program devam ediyor...")

# Başka örnek
print("\nString işlemi örneği:")
try:
    metin = "Python"
    print(metin[10])  # Index hatası
except IndexError:
    print("Hata: Geçersiz index!")

#######################
# 2. FARKLI HATA TÜRLERİ
#######################

print("\n=== Farklı Hata Türleri ===")

# ValueError örneği
print("ValueError örneği:")
try:
    sayi = int("abc")  # String'i sayıya çevirmede hata
    print("Sayı:", sayi)
except ValueError:
    print("Hata: Geçersiz sayı formatı!")

# TypeError örneği
print("\nTypeError örneği:")
try:
    sonuc = "5" + 3  # String ile sayı toplama hatası
    print("Sonuç:", sonuc)
except TypeError:
    print("Hata: Uyumsuz veri tipleri!")

# KeyError örneği
print("\nKeyError örneği:")
try:
    sozluk = {"isim": "Ali", "yas": 25}
    print(sozluk["meslek"])  # Olmayan anahtar
except KeyError:
    print("Hata: Sözlükte bu anahtar yok!")

#######################
# 3. BİRDEN FAZLA EXCEPT BLOĞU
#######################

print("\n=== Birden Fazla Except Bloğu ===")

def sayisal_islem(metin):
    """Metni sayıya çevirerek matematik işlemi yapar"""
    try:
        # Farklı hatalar oluşabilir
        sayi = int(metin)           # ValueError
        sonuc = 100 / sayi          # ZeroDivisionError
        liste = [1, 2, 3]
        print(liste[sayi])          # IndexError
        
    except ValueError:
        print("Hata: Geçersiz sayı formatı!")
    except ZeroDivisionError:
        print("Hata: Sıfıra bölme yapılamaz!")
    except IndexError:
        print("Hata: Liste index sınırı dışında!")
    except Exception as e:
        print(f"Bilinmeyen hata: {e}")

# Test etme
sayisal_islem("abc")    # ValueError
sayisal_islem("0")      # ZeroDivisionError
sayisal_islem("5")      # IndexError
sayisal_islem("2")      # Başarılı

#######################
# 4. HATA MESAJINI YAKALAMA
#######################

print("\n=== Hata Mesajını Yakalama ===")

def hata_detayli(kod):
    """Hata mesajını detaylı gösterir"""
    try:
        exec(kod)  # Verilen kodu çalıştır
    except Exception as e:
        print(f"Hata Türü: {type(e).__name__}")
        print(f"Hata Mesajı: {e}")
        print("Program devam ediyor...")

# Test etme
hata_detayli("print(10 / 0)")
hata_detayli("int('abc')")
hata_detayli("print(liste_yok)")

#######################
# 5. ELSE VE FINALLY BLOKLARI
#######################

print("\n=== Else ve Finally Blokları ===")

def dosya_islemleri(dosya_adi):
    """
    Dosya işlemlerinde else ve finally kullanımı
    
    else: Hata yoksa çalışır
    finally: Her durumda çalışır
    """
    try:
        print(f"'{dosya_adi}' dosyası açılmaya çalışılıyor...")
        # Gerçek dosya işlemi yerine simülasyon
        if dosya_adi == "mevcut.txt":
            icerik = "Dosya içeriği başarıyla okundu"
            print("Dosya başarıyla açıldı")
        else:
            raise FileNotFoundError("Dosya bulunamadı")
            
    except FileNotFoundError as e:
        print(f"Hata: {e}")
        icerik = None
        
    else:
        # Hata yoksa burası çalışır
        print("Dosya işlemi başarıyla tamamlandı")
        print(f"İçerik: {icerik}")
        
    finally:
        # Her durumda burası çalışır
        print("Dosya işlemi sona erdi\n")
    
    return icerik

# Test etme
dosya_islemleri("mevcut.txt")    # Başarılı
dosya_islemleri("olmayan.txt")   # Hatalı

#######################
# 6. KULLANICI GİRİŞİ VE HATA YAKALAMA
#######################

print("\n=== Kullanıcı Girişi ve Hata Yakalama ===")

def guvenli_sayi_alma():
    """Kullanıcıdan güvenli şekilde sayı alır"""
    while True:
        try:
            # gerçek kullanımda input() kullanılır
            # Burada örnekleme için direkt değer verelim
            kullanici_girdisi = "123"  # input("Bir sayı giriniz: ")
            print(f"Girdi: {kullanici_girdisi}")
            
            sayi = float(kullanici_girdisi)
            print(f"Başarılı! Girilen sayı: {sayi}")
            return sayi
            
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı giriniz!")
            # gerçek uygulamada döngü devam eder
            break  # Demo için döngüyü kır
        except KeyboardInterrupt:
            print("\nProgram kullanıcı tarafından durduruldu")
            return None

# Test etme
sonuc = guvenli_sayi_alma()

#######################
# 7. MANUEL HATA FIRLLATMA (RAISE)
#######################

print("\n=== Manuel Hata Fırlatma (raise) ===")

def yas_kontrol(yas):
    """Yaş kontrolü yapar, geçersizse hata fırlatır"""
    try:
        yas = int(yas)
        
        if yas < 0:
            raise ValueError("Yaş negatif olamaz!")
        elif yas > 150:
            raise ValueError("Yaş 150'den büyük olamaz!")
        elif yas < 18:
            raise ValueError("18 yaşından küçük olamazsınız!")
        else:
            print(f"Yaş geçerli: {yas}")
            return yas
            
    except ValueError as e:
        print(f"Yaş hatası: {e}")
        return None

# Test etme
yas_kontrol("25")    # Geçerli
yas_kontrol("-5")    # Negatif
yas_kontrol("200")   # Çok büyük
yas_kontrol("15")    # Çok küçük
yas_kontrol("abc")   # Geçersiz format

def email_kontrol(email):
    """Email formatını kontrol eder"""
    if "@" not in email:
        raise ValueError("Email '@' karakteri içermeli!")
    if "." not in email:
        raise ValueError("Email '.' karakteri içermeli!")
    
    print(f"Email geçerli: {email}")
    return True

# Test etme
try:
    email_kontrol("test@example.com")  # Geçerli
except ValueError as e:
    print(f"Email hatası: {e}")

try:
    email_kontrol("test.com")  # Hatalı
except ValueError as e:
    print(f"Email hatası: {e}")

#######################
# 8. VERİ İŞLEME UYGULAMASI
#######################

print("\n=== Veri İşleme Uygulaması ===")

def veri_temizle(veri_listesi):
    """Veri listesini temizler ve sayısal değerlere çevirir"""
    temiz_veri = []
    hata_sayisi = 0
    
    print(f"İşlenecek veri: {veri_listesi}")
    
    for i, veri in enumerate(veri_listesi):
        try:
            # Veriyi sayıya çevir
            sayi = float(veri)
            
            # Geçerlilik kontrolü
            if sayi < 0:
                raise ValueError("Negatif değer")
            
            temiz_veri.append(sayi)
            print(f"✓ {i+1}. veri işlendi: {veri} -> {sayi}")
            
        except ValueError as e:
            hata_sayisi += 1
            print(f"✗ {i+1}. veri hatası: '{veri}' - {e}")
            
        except Exception as e:
            hata_sayisi += 1
            print(f"✗ {i+1}. veri bilinmeyen hata: '{veri}' - {e}")
    
    print(f"\nÖzet:")
    print(f"Toplam veri: {len(veri_listesi)}")
    print(f"Başarılı: {len(temiz_veri)}")
    print(f"Hatalı: {hata_sayisi}")
    print(f"Temiz veri: {temiz_veri}")
    
    return temiz_veri

# Test etme
ham_veri = ["10", "20.5", "abc", "30", "-5", "", "40.0", "def", "50"]
temiz_veri = veri_temizle(ham_veri)

#######################
# 9. HESAP MAKİNESİ İLE HATA YAKALAMA
#######################

print("\n=== Hesap Makinesi ile Hata Yakalama ===")

def guvenli_hesap_makinesi(sayi1, islem, sayi2):
    """Hata yakalama ile güvenli hesap makinesi"""
    try:
        # Sayıları kontrol et
        num1 = float(sayi1)
        num2 = float(sayi2)
        
        # İşlemi yap
        if islem == "+":
            sonuc = num1 + num2
        elif islem == "-":
            sonuc = num1 - num2
        elif islem == "*":
            sonuc = num1 * num2
        elif islem == "/":
            if num2 == 0:
                raise ZeroDivisionError("Sıfıra bölme hatası!")
            sonuc = num1 / num2
        elif islem == "**":
            sonuc = num1 ** num2
        elif islem == "%":
            if num2 == 0:
                raise ZeroDivisionError("Sıfıra bölme hatası!")
            sonuc = num1 % num2
        else:
            raise ValueError(f"Geçersiz işlem: {islem}")
        
        print(f"Sonuç: {num1} {islem} {num2} = {sonuc}")
        return sonuc
        
    except ValueError as e:
        print(f"Değer hatası: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"Matematik hatası: {e}")
        return None
    except Exception as e:
        print(f"Bilinmeyen hata: {e}")
        return None

# Test etme
guvenli_hesap_makinesi("10", "+", "5")     # Başarılı
guvenli_hesap_makinesi("10", "/", "0")     # Sıfıra bölme
guvenli_hesap_makinesi("abc", "+", "5")    # Geçersiz sayı
guvenli_hesap_makinesi("10", "@", "5")     # Geçersiz işlem

#######################
# 10. EN İYİ PRATİKLER
#######################

print("\n=== En İyi Pratikler ===")

print("Hata yakalama best practices:")
print("✓ Spesifik hata türlerini yakalayın (Exception yerine)")
print("✓ Hata mesajlarını kullanıcı dostu yapın")
print("✓ finally bloğunda temizlik işlemleri yapın")
print("✓ Hataları log'layın (gelişmiş uygulamalarda)")
print("✓ Kullanıcıdan tekrar giriş alma imkanı sunun")

# İyi örnek
def iyi_ornek():
    try:
        # Riskli işlem
        pass
    except ValueError:
        # Spesifik hata
        print("Değer hatası")
    except FileNotFoundError:
        # Spesifik hata
        print("Dosya hatası")
    except Exception as e:
        # Genel hata (son çare)
        print(f"Bilinmeyen hata: {e}")
    finally:
        # Temizlik işlemleri
        print("İşlem tamamlandı")

print("\n=== Bu Derste Öğrendiklerimiz ===")
print("✓ try-except yapısı")
print("✓ Farklı hata türleri (ValueError, TypeError, etc.)")
print("✓ Birden fazla except bloğu")
print("✓ Hata mesajını yakalama (as e)")
print("✓ else ve finally blokları")
print("✓ Manuel hata fırlatma (raise)")
print("✓ Kullanıcı girişi ile hata yakalama")
print("✓ Veri işlemede hata yakalama")
print("✓ En iyi pratikler")

print("\nSıradaki ders: Sınıflar (Classes)")
