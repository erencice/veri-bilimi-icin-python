###############################################
# 13. DERS: KULLANICIDAN VERİ ALMA - input() FONKSİYONU
###############################################

# Bu derste öğreneceğimiz konular:
# - input() fonksiyonu nedir?
# - Kullanıcıdan metin alma
# - Sayısal veri alma ve tip dönüşümü
# - String metodları ile girdi temizleme

#######################
# 1. input() FONKSİYONU NEDİR?
#######################

# input() fonksiyonu, kullanıcıdan klavye ile veri almak için kullanılır
# Bu fonksiyon her zaman string (metin) tipinde sonuç döndürür

print("=== Basit Girdi Alma ===")

# Kullanıcıdan isim alalım
isim = input("İsminizi girin: ")
print("Merhaba " + isim + "!")

# Tip kontrolü yapalım
print("Girdiğiniz verinin tipi:", type(isim))

#######################
# 2. SAYISAL VERİ ALMA VE TİP DÖNÜŞÜMü
#######################

print("\n=== Sayısal Veri Alma ===")

# input() her zaman string döndürür
# Sayısal işlem yapmak için tip dönüşümü gerekir

yas_metin = input("Yaşınızı girin: ")
print("Yaş (metin olarak):", yas_metin, "- Tip:", type(yas_metin))

# String'i integer'a çevirelim
yas_sayi = int(yas_metin)
print("Yaş (sayı olarak):", yas_sayi, "- Tip:", type(yas_sayi))

# Şimdi matematiksel işlem yapabiliriz
gelecek_yas = yas_sayi + 10
print("10 yıl sonra yaşınız:", gelecek_yas)

#######################
# 3. ONDALIKLI SAYI ALMA
#######################

print("\n=== Ondalıklı Sayı Alma ===")

boy_metin = input("Boyunuzu metre cinsinden girin (örn: 1.75): ")
print("Boy (metin olarak):", boy_metin, "- Tip:", type(boy_metin))

# String'i float'a çevirelim
boy_sayi = float(boy_metin)
print("Boy (sayı olarak):", boy_sayi, "- Tip:", type(boy_sayi))

# Hesaplama yapalım
boy_cm = boy_sayi * 100
print("Boyunuz santimetre cinsinden:", boy_cm)

#######################
# 4. GİRDİ TEMİZLEME - strip() METODU
#######################

print("\n=== Girdi Temizleme ===")

# Kullanıcı bazen başında veya sonunda boşluk bırakabilir
# strip() metodu bu boşlukları temizler

sehir = input("Hangi şehirde yaşıyorsunuz: ")
print("Girdiğiniz (ham hali): '" + sehir + "'")

# Boşlukları temizleyelim
sehir_temiz = sehir.strip()
print("Temizlenmiş hali: '" + sehir_temiz + "'")

#######################
# 5. BÜYÜK/KÜÇÜK HARF DÜZENLEMESİ
#######################

print("\n=== Büyük/Küçük Harf Düzenlemesi ===")

renk = input("En sevdiğiniz rengi yazın: ")
print("Girdiğiniz (ham hali):", renk)

# Tümünü küçük harfe çevirelim
renk_kucuk = renk.lower()
print("Küçük harflerle:", renk_kucuk)

# Tümünü büyük harfe çevirelim  
renk_buyuk = renk.upper()
print("Büyük harflerle:", renk_buyuk)

# İlk harfi büyük, diğerleri küçük
renk_baslik = renk.title()
print("Başlık formatında:", renk_baslik)

#######################
# 6. BİRDEN FAZLA İŞLEM BİRLEŞTİRME
#######################

print("\n=== Birden Fazla İşlem Birleştirme ===")

# strip() ve lower() işlemlerini birleştirebiliriz
cevap = input("Veri bilimine ilginiz var mı? (evet/hayır): ")
cevap_temiz = cevap.strip().lower()

print("Temizlenmiş cevap:", cevap_temiz)

# Cevaba göre mesaj gösterelim
# (Bu yapı 16. derste detaylı anlatılacak)
# Şimdilik sadece basit karşılaştırma yapalım
print("Cevabınız 'evet' mi?", cevap_temiz == "evet")
print("Cevabınız 'hayır' mı?", cevap_temiz == "hayır")

#######################
# 7. PRATİK UYGULAMALAR
#######################

print("\n=== Pratik Uygulama 1: Kişisel Bilgiler ===")

# Kullanıcıdan bilgi alalım ve gösterelim
ad = input("Adınız: ").strip().title()
soyad = input("Soyadınız: ").strip().title()  
yas = int(input("Yaşınız: "))
boy = float(input("Boyunuz (metre): "))

print("\n--- Girdiğiniz Bilgiler ---")
print("Ad Soyad:", ad + " " + soyad)
print("Yaş:", yas)
print("Boy (metre):", boy)
print("Boy (santimetre):", boy * 100)

print("\n=== Pratik Uygulama 2: Hesap Makinesi ===")

# Basit toplama işlemi
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

toplam = sayi1 + sayi2
print("Toplam:", toplam)

#######################
# 8. ÖNEMLİ NOKTALAR VE İPUÇLARI
#######################

# 1. input() her zaman string döndürür
# 2. Sayısal işlem için int() veya float() kullanılmalı
# 3. strip() ile baş/son boşlukları temizleyin
# 4. lower() ile küçük harf, upper() ile büyük harf
# 5. title() ile kelime başlarını büyük harf yapın
# 6. Birden fazla string metodunu birleştirebilirsiniz

print("\n=== Bu Derste Öğrendiklerimiz ===")
print("✓ input() fonksiyonu kullanımı")
print("✓ String to integer/float dönüşümü")  
print("✓ strip(), lower(), upper(), title() metodları")
print("✓ Kullanıcıdan güvenli veri alma teknikleri")

print("\nSıradaki ders: Ödev çözümleri ve pratik uygulamalar")