# =======================================================
# PYTHON DERS 3: TİP DÖNÜŞÜMLERİ
# =======================================================

# Önceki derslerde matematiksel işlemler ve veri türlerini öğrendik.
# Bu derste bir veri türünü başka bir türe nasıl dönüştüreceğimizi öğreneceğiz.

# Öğreneceğiniz dönüşüm fonksiyonları:
#   - int()   → Tam sayıya çevirir
#   - float() → Ondalıklı sayıya çevirir  
#   - str()   → Metne çevirir
#   - bool()  → Mantıksal değere çevirir

print("Python Tip Dönüşümleri Dersine Hoş Geldiniz!")


# =======================================================
# 1. TAM SAYIYA ÇEVİRME - int()
# =======================================================
print("1. TAM SAYIYA ÇEVİRME - int()")
print("-------------------------------")

# Ondalıklı sayıdan tam sayıya
ondalik = 3.99
tam_sayi = int(ondalik)
print("3.99'u tam sayıya çevirirsek:", tam_sayi)  # 3 (ondalık kısım atılır)

# Metinden tam sayıya
sayi_metni = "42"
sayi = int(sayi_metni)
print("'42' metnini tam sayıya çevirirsek:", sayi)  # 42

# Mantıksal değerden tam sayıya
dogru_deger = True
yanlis_deger = False
print("True'yu tam sayıya çevirirsek:", int(dogru_deger))    # 1
print("False'u tam sayıya çevirirsek:", int(yanlis_deger))   # 0

print("int() dönüşümü tamamlandı!")


# =======================================================
# 2. ONDALIKLI SAYIYA ÇEVİRME - float()
# =======================================================
print("2. ONDALIKLI SAYIYA ÇEVİRME - float()")
print("---------------------------------------")

# Tam sayıdan ondalıklı sayıya
tam = 5
ondalik = float(tam)
print("5'i ondalıklı sayıya çevirirsek:", ondalik)  # 5.0

# Metinden ondalıklı sayıya
pi_metni = "3.14"
pi_sayisi = float(pi_metni)
print("'3.14' metnini ondalıklı sayıya çevirirsek:", pi_sayisi)  # 3.14

# Mantıksal değerden ondalıklı sayıya
print("True'yu ondalıklı sayıya çevirirsek:", float(True))   # 1.0
print("False'u ondalıklı sayıya çevirirsek:", float(False))  # 0.0

print("float() dönüşümü tamamlandı!")


# =======================================================
# 3. METİNE ÇEVİRME - str()
# =======================================================
print("3. METİNE ÇEVİRME - str()")
print("--------------------------")

# Tam sayıdan metne
sayi = 100
metin = str(sayi)
print("100 sayısını metne çevirirsek:", metin)        # "100"
print("Türü:", type(metin))                           # <class 'str'>

# Ondalıklı sayıdan metne
pi = 3.14159
pi_metni = str(pi)
print("3.14159 sayısını metne çevirirsek:", pi_metni) # "3.14159"

# Mantıksal değerden metne
print("True'yu metne çevirirsek:", str(True))         # "True"
print("False'u metne çevirirsek:", str(False))        # "False"

print("str() dönüşümü tamamlandı!")


# =======================================================
# 4. MANTIKSAL DEĞERE ÇEVİRME - bool()
# =======================================================
print("4. MANTIKSAL DEĞERE ÇEVİRME - bool()")
print("-------------------------------------")

# Sayılardan mantıksal değere
print("1 sayısını mantıksal değere çevirirsek:", bool(1))    # True
print("0 sayısını mantıksal değere çevirirsek:", bool(0))    # False
print("42 sayısını mantıksal değere çevirirsek:", bool(42))  # True
print("-5 sayısını mantıksal değere çevirirsek:", bool(-5))  # True

# Metinlerden mantıksal değere
print("'Python' metnini mantıksal değere çevirirsek:", bool("Python"))  # True
print("Boş metni mantıksal değere çevirirsek:", bool(""))                # False

# ÖNEMLİ KURAL:
# - Sıfır sayılar (0, 0.0) → False
# - Boş metinler ("") → False  
# - Diğer tüm değerler → True

print("bool() dönüşümü tamamlandı!")



# =======================================================
# 5. PRATİK UYGULAMALAR
# =======================================================
print("5. PRATİK UYGULAMALAR")
print("----------------------")

# Örnek 1: Yaş hesaplama
dogum_yili_metni = "1995"
su_anki_yil = 2024
yas = su_anki_yil - int(dogum_yili_metni)  # Metni tam sayıya çevirdik
print("Doğum yılı:", dogum_yili_metni, "- Yaş:", yas)

# Örnek 2: Not ortalaması
not1_metni = "85.5"
not2_metni = "90.0"
not3_metni = "77.5"

# Metinleri ondalıklı sayıya çevirip ortalama hesaplayalım
not1 = float(not1_metni)
not2 = float(not2_metni)
not3 = float(not3_metni)
ortalama = (not1 + not2 + not3) / 3

print("Not ortalaması:", ortalama)

# Örnek 3: Başarı durumu
gecme_notu = 70.0
basarili_mi = ortalama >= gecme_notu  # Bu bir mantıksal değer (bool) döner
print("Başarılı mı?", basarili_mi)
print("Başarı durumu metni:", str(basarili_mi))  # bool'u metne çevirdik

print("Pratik uygulamalar tamamlandı!")


# =======================================================
# DERS ÖZET
# =======================================================
print("DERS ÖZETİ")
print("-----------")
print("Bu derste öğrendiğiniz dönüşüm fonksiyonları:")
print("1. int() - Tam sayıya çevirir")
print("2. float() - Ondalıklı sayıya çevirir")
print("3. str() - Metne çevirir")
print("4. bool() - Mantıksal değere çevirir")
print("")
print("ÖNEMLİ KURALLAR:")
print("- int() ondalık kısmı atar (3.99 → 3)")
print("- Sıfır ve boş değerler bool() ile False olur")
print("- Diğer tüm değerler bool() ile True olur")

print("TİP DÖNÜŞÜMLERİ DERSİ TAMAMLANDI!")
print("Sonraki ders: print() fonksiyonu ve formatlamayı öğreneceğiz.")