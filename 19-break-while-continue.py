###############################################
# 19. DERS: BREAK, CONTINUE VE WHILE DÖNGÜ KONTROL YAPILARI
###############################################

# Bu derste öğreneceğimiz konular:
# - break komutu ile döngüyü sonlandırma
# - continue komutu ile döngü adımını atlama
# - while döngüsü kullanımı
# - Döngü kontrol yapılarının pratik uygulamaları

print("=== BREAK, CONTINUE VE WHILE DÖNGÜ KONTROL YAPILARI ===")

#######################
# 1. break KOMUTU - DÖNGÜYÜ SONLANDIRMA
#######################

print("\n=== break Komutu - Döngüyü Sonlandırma ===")

# break komutu döngüyü anında sonlandırır
# Kalan elemanlar işlenmez

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Sayılarda 5'i bulana kadar devam et:")
for sayi in sayilar:
    print("İncelenen sayı:", sayi)
    if sayi == 5:
        print("5 bulundu! Döngü sonlandırılıyor.")
        break
    print("5 değil, devam ediliyor...")

print("Döngü bitti\n")

# Başka bir örnek: İlk çift sayıyı bulma
print("İlk çift sayıyı bulma:")
sayilar = [1, 3, 7, 8, 9, 12, 15]

for sayi in sayilar:
    print("Kontrol edilen:", sayi)
    if sayi % 2 == 0:
        print("İlk çift sayı bulundu:", sayi)
        break
else:
    print("Hiç çift sayı bulunamadı")

#######################
# 2. continue KOMUTU - ADIM ATLAMA
#######################

print("\n=== continue Komutu - Adım Atlama ===")

# continue komutu o anki döngü adımını atlar
# Döngü devam eder, sadece o adım işlenmez

print("1'den 10'a kadar, sadece çift sayıları yazdır:")
for i in range(1, 11):
    if i % 2 == 1:  # Tek sayı ise
        continue    # Bu adımı atla
    print("Çift sayı:", i)

print()

# Başka bir örnek: Belirli karakterleri atlama
print("Kelimede sadece sesli harfleri yazdır:")
kelime = "python programlama"

for harf in kelime:
    if harf in "bcdfghjklmnpqrstvwxyz":  # Sessiz harf ise
        continue  # Bu harfi atla
    print("Sesli harf:", harf)

#######################
# 3. while DÖNGÜSÜ TEMELLERİ
#######################

print("\n=== while Döngüsü Temelleri ===")

# while döngüsü koşul doğru olduğu sürece çalışır
# for döngüsünden farkı: kaç kez çalışacağını bilmeyiz

print("1'den 5'e kadar sayma:")
sayac = 1

while sayac <= 5:
    print("Sayaç:", sayac)
    sayac = sayac + 1  # Sayacı artırmayı unutmayın!

print("while döngüsü bitti")

# Başka bir örnek: Koşula bağlı döngü
print("\nSayıları 2'yle bölerek 1'e ulaşma:")
sayi = 16

while sayi > 1:
    print("Mevcut sayı:", sayi)
    sayi = sayi // 2  # Tam bölme işlemi

print("Final sayı:", sayi)

#######################
# 4. while DÖNGÜSÜNDE BREAK
#######################

print("\n=== while Döngüsünde break ===")

# Sonsuz döngü + break ile kontrollü çıkış
print("Kullanıcı 'q' girene kadar devam et:")

sayac = 0
while True:  # Sonsuz döngü
    sayac += 1
    print(f"Döngü adımı: {sayac}")
    
    # Belirli bir koşulda çık
    if sayac >= 5:
        print("5 adım tamamlandı, çıkılıyor...")
        break

print("Sonsuz döngüden çıkıldı")

# Sayı tahmin oyunu örneği
print("\nSayı tahmin oyunu simülasyonu:")
gizli_sayi = 7
tahmin = 1

while True:
    print(f"Tahmin: {tahmin}")
    
    if tahmin == gizli_sayi:
        print("Doğru tahmin! Oyun bitti.")
        break
    elif tahmin < gizli_sayi:
        print("Daha büyük bir sayı dene")
    else:
        print("Daha küçük bir sayı dene")
    
    tahmin += 1
    
    # Güvenlik önlemi: çok fazla deneme
    if tahmin > 10:
        print("Çok fazla deneme yapıldı!")
        break

#######################
# 5. while DÖNGÜSÜNDE CONTINUE
#######################

print("\n=== while Döngüsünde continue ===")

print("1'den 10'a kadar, 5'i atla:")
i = 0

while i < 10:
    i += 1  # Önce artır
    
    if i == 5:
        continue  # 5'i atla
    
    print("Sayı:", i)

print()

# Çift sayıları atlama örneği
print("1'den 10'a kadar sadece tek sayılar:")
sayac = 0

while sayac < 10:
    sayac += 1
    
    if sayac % 2 == 0:  # Çift sayı ise
        continue        # Atla
    
    print("Tek sayı:", sayac)

#######################
# 6. İÇ İÇE DÖNGÜLERDE BREAK VE CONTINUE
#######################

print("\n=== İç İçe Döngülerde break ve continue ===")

print("Çarpım tablosu (5'e kadar, 3'ün katlarını atla):")

for i in range(1, 6):
    print(f"\n{i}'in çarpım tablosu:")
    
    for j in range(1, 6):
        if j == 3:
            continue  # 3'ü atla
        
        sonuc = i * j
        print(f"{i} x {j} = {sonuc}")

print()

# break sadece içindeki döngüyü etkiler
print("Dış döngü devam eder, iç döngü break ile durur:")

for i in range(1, 4):
    print(f"Dış döngü: {i}")
    
    for j in range(1, 6):
        print(f"  İç döngü: {j}")
        if j == 3:
            print("  İç döngü break ile durdu")
            break

#######################
# 7. PRATİK UYGULAMA ÖRNEKLERİ
#######################

print("\n=== Pratik Uygulama Örnekleri ===")

# Örnek 1: Asal sayı kontrolü
def asal_mi(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # break yerine return
    
    return True

print("1'den 20'ye kadar asal sayılar:")
for sayi in range(1, 21):
    if asal_mi(sayi):
        print("Asal:", sayi)

print()

# Örnek 2: Liste içinde arama
def liste_arama(liste, aranan):
    for i, eleman in enumerate(liste):
        if eleman == aranan:
            return f"'{aranan}' bulundu, indeks: {i}"
    
    return f"'{aranan}' bulunamadı"

meyveler = ["elma", "armut", "muz", "çilek", "kiraz"]
print("Meyve listesi:", meyveler)
print(liste_arama(meyveler, "muz"))
print(liste_arama(meyveler, "portakal"))

print()

# Örnek 3: Şifre doğrulama simülasyonu
def sifre_kontrol():
    dogru_sifre = "python123"
    deneme_hakki = 3
    
    while deneme_hakki > 0:
        # Simülasyon için farklı şifreler deneyelim
        test_sifreler = ["123456", "python", "python123"]
        sifre = test_sifreler[3 - deneme_hakki]
        
        print(f"Denenen şifre: {sifre}")
        
        if sifre == dogru_sifre:
            print("Şifre doğru! Giriş başarılı.")
            break
        else:
            deneme_hakki -= 1
            if deneme_hakki > 0:
                print(f"Yanlış şifre! Kalan deneme hakkı: {deneme_hakki}")
            else:
                print("Deneme hakkınız bitti! Hesap kilitlendi.")

sifre_kontrol()

#######################
# 8. PERFORMANS VE OPTİMİZASYON
#######################

print("\n=== Performans ve Optimizasyon ===")

# break kullanarak gereksiz işlemleri önleme
print("Liste içinde büyük sayı arama:")

buyuk_liste = list(range(1, 1000000))  # 1 milyon elemanlı liste
aranan = 500000

# break kullanmadan (verimsiz)
def verimsiz_arama(liste, aranan):
    bulundu = False
    indeks = -1
    for i, eleman in enumerate(liste):
        if eleman == aranan:
            bulundu = True
            indeks = i
    
    return bulundu, indeks

# break kullanarak (verimli)
def verimli_arama(liste, aranan):
    for i, eleman in enumerate(liste):
        if eleman == aranan:
            return True, i
    
    return False, -1

print("Verimli arama ile", aranan, "bulundu mu?", verimli_arama(buyuk_liste[:1000], 500)[0])

#######################
# 9. YAYGKIN HATALAR VE ÇÖZÜMLER
#######################

print("\n=== Yaygın Hatalar ve Çözümleri ===")

# Hata 1: while döngüsünde sayaç unutma
print("YANLIŞ kullanım (sonsuz döngü):")
print("# i = 0")
print("# while i < 5:")
print("#     print(i)")
print("#     # i += 1  # UNUTULDU!")

print("\nDOĞRU kullanım:")
i = 0
while i < 3:  # 3 ile sınırladık
    print("i =", i)
    i += 1  # Sayaç artırımı

# Hata 2: continue öncesi sayaç artırımı
print("\nwhile + continue kullanımında dikkat:")
print("Sayaç artırımı continue'dan önce olmalı")

sayac = 0
while sayac < 5:
    sayac += 1  # ÖNCE artır
    
    if sayac == 3:
        continue  # SONRA kontrol et
    
    print("İşlenen sayı:", sayac)

#######################
# 10. ÖZET VE EN İYİ PRATİKLER
#######################

print("\n=== Özet ve En İyi Praktikler ===")

print("break komutu:")
print("• Döngüyü tamamen sonlandırır")
print("• Sadece içinde bulunduğu döngüyü etkiler")
print("• Erken çıkış için kullanılır")

print("\ncontinue komutu:")
print("• Sadece o anki döngü adımını atlar")
print("• Döngü bir sonraki adımla devam eder")
print("• Belirli koşullarda işlem atlamak için kullanılır")

print("\nwhile döngüsü:")
print("• Koşul doğru olduğu sürece çalışır")
print("• Sayaç artırımını unutmayın!")
print("• Sonsuz döngü riskine dikkat edin")

print("\nBest Practices:")
print("• while True + break kombinasyonu güçlüdür")
print("• continue kullanırken sayaç yerini kontrol edin")
print("• Performans için erken break kullanın")
print("• Sonsuz döngülerde güvenlik kontrolleri ekleyin")

print("\n=== Bu Derste Öğrendiklerimiz ===")
print("✓ break komutu ile döngü sonlandırma")
print("✓ continue komutu ile adım atlama")
print("✓ while döngüsü ve koşullu tekrar")
print("✓ Döngü kontrol yapılarının kombinasyonları")
print("✓ İç içe döngülerde kontrol yapıları")
print("✓ Pratik uygulama örnekleri")
print("✓ Performans optimizasyonu teknikleri")
print("✓ Yaygın hatalar ve çözümleri")

print("\nSıradaki ders: Enumerate ve Zip fonksiyonları")
