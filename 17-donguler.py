###############################################
# 17. DERS: DÖNGÜLER - TEKRAR YAPILARI
###############################################

# Bu derste öğreneceğimiz konular:
# - Döngü nedir ve neden kullanılır?
# - for döngüsü
# - range() fonksiyonu
# - while döngüsü
# - Döngülerde koşullar
# - Pratik örnekler

print("=== DÖNGÜLER - TEKRAR YAPILARI ===")

#######################
# 1. DÖNGÜ NEDİR?
#######################

print("\n=== Döngü Nedir? ===")

# Döngüler, aynı işi tekrar tekrar yapmamıza yarar
# Manuel olarak tekrar yazmak yerine döngü kullanırız

print("Manuel tekrar:")
print("1. öğrenci")
print("2. öğrenci") 
print("3. öğrenci")
print("4. öğrenci")
print("5. öğrenci")

print("\nDöngü ile tekrar:")
for i in range(1, 6):
    print(str(i) + ". öğrenci")

#######################
# 2. LİSTELERDE for DÖNGÜSÜ
#######################

print("\n=== Listelerde for Döngüsü ===")

# Liste elemanları üzerinde döngü
meyveler = ["elma", "armut", "muz", "çilek", "kiraz"]

print("Meyveler:")
for meyve in meyveler:
    print("- " + meyve)

# Sayılarla çalışma
sayilar = [1, 2, 3, 4, 5]

print("\nSayılar:")
for sayi in sayilar:
    print("Sayı:", sayi)

# Matematiksel işlemler
print("\nSayıların kareleri:")
for sayi in sayilar:
    kare = sayi * sayi
    print(sayi, "nin karesi:", kare)

#######################
# 3. range() FONKSİYONU
#######################

print("\n=== range() Fonksiyonu ===")

# range(n): 0'dan n-1'e kadar sayılar
print("range(5):")
for i in range(5):
    print(i)

# range(başlangıç, bitiş): başlangıçtan bitiş-1'e kadar
print("\nrange(3, 8):")
for i in range(3, 8):
    print(i)

# range(başlangıç, bitiş, adım): belirli adımlarla
print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(i)

# Geriye doğru sayma
print("\nrange(10, 0, -1):")
for i in range(10, 0, -1):
    print(i)

#######################
# 4. PRATİK ÖRNEKLER
#######################

print("\n=== Pratik Örnekler ===")

# Örnek 1: Çarpım tablosu
print("5'in çarpım tablosu:")
for i in range(1, 11):
    sonuc = 5 * i
    print("5 x", i, "=", sonuc)

# Örnek 2: 1'den 10'a kadar sayıların toplamı
toplam = 0
for i in range(1, 11):
    toplam = toplam + i
    print("Şu ana kadar toplam:", toplam)

print("Final toplam:", toplam)

# Örnek 3: Faktöriyel hesaplama
sayi = 5
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel = faktoriyel * i
    print(i, "! =", faktoriyel)

#######################
# 5. while DÖNGÜSÜ
#######################

print("\n=== while Döngüsü ===")

# while koşul doğru olduğu sürece çalışır
sayac = 1

print("1'den 5'e kadar sayma:")
while sayac <= 5:
    print("Sayaç:", sayac)
    sayac = sayac + 1  # Sayacı artırmayı unutmayın!

print("Döngü bitti, sayaç:", sayac)

# Başka bir örnek
toplam = 0
sayi = 1

print("\n1'den 100'e kadar sayıların toplamı:")
while sayi <= 100:
    toplam = toplam + sayi
    sayi = sayi + 1

print("Toplam:", toplam)

#######################
# 6. DÖNGÜLERDE KOŞULLAR
#######################

print("\n=== Döngülerde Koşullar ===")

# Çift sayıları yazdırma
print("1'den 10'a kadar çift sayılar:")
for i in range(1, 11):
    if i % 2 == 0:  # % operatörü kalanı verir
        print(i, "çift sayı")

# Tek sayıları yazdırma
print("\n1'den 10'a kadar tek sayılar:")
for i in range(1, 11):
    if i % 2 == 1:
        print(i, "tek sayı")

# Farklı koşullar
print("\nSayıları kategorilere ayırma:")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "→ Hem 3'e hem 5'e bölünebilir")
    elif i % 3 == 0:
        print(i, "→ 3'e bölünebilir")
    elif i % 5 == 0:
        print(i, "→ 5'e bölünebilir")

#######################
# 7. LİSTELERDE DÖNGÜ VE KOŞUL
#######################

print("\n=== Listelerde Döngü ve Koşul ===")

# Öğrenci notları
notlar = [85, 92, 67, 78, 96, 54, 89, 73]

print("Not değerlendirmesi:")
for not_degeri in notlar:
    if not_degeri >= 85:
        print("Not:", not_degeri, "→ Pekiyi")
    elif not_degeri >= 70:
        print("Not:", not_degeri, "→ İyi")
    elif not_degeri >= 55:
        print("Not:", not_degeri, "→ Orta")
    else:
        print("Not:", not_degeri, "→ Kaldı")

# Maaş zammı örneği
maaslar = [3000, 5000, 7000, 2000, 8000]

print("\nMaaş zammı uygulaması:")
for maas in maaslar:
    if maas >= 6000:
        zam_orani = 10
    elif maas >= 4000:
        zam_orani = 15
    else:
        zam_orani = 20
    
    yeni_maas = maas + (maas * zam_orani / 100)
    print("Eski maaş:", maas, "Zam:", zam_orani, "% Yeni maaş:", yeni_maas)

#######################
# 8. FONKSİYONLARLA DÖNGÜLER
#######################

print("\n=== Fonksiyonlarla Döngüler ===")

def sayi_analizi(sayi):
    if sayi % 2 == 0:
        return "çift"
    else:
        return "tek"

def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True

# 1'den 20'ye kadar sayıları analiz edelim
print("Sayı analizi:")
for i in range(1, 21):
    tip = sayi_analizi(i)
    asal = "asal" if asal_mi(i) else "asal değil"
    print(i, "→", tip + ",", asal)

#######################
# 9. İÇ İÇE DÖNGÜLER
#######################

print("\n=== İç İçe Döngüler ===")

# Çarpım tablosu (tüm rakamlar)
print("Çarpım tablosu:")
for i in range(1, 6):  # 1'den 5'e kadar
    for j in range(1, 6):  # 1'den 5'e kadar
        sonuc = i * j
        print(i, "x", j, "=", sonuc)
    print("---")  # Her dış döngü sonunda ayraç

# Yıldız deseni
print("\nYıldız deseni:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")  # end="" aynı satırda yazdırır
    print()  # Yeni satıra geç

#######################
# 10. PRAKTİK UYGULAMALAR
#######################

print("\n=== Pratik Uygulamalar ===")

# Uygulama 1: Fibonaci dizisi
print("Fibonaci dizisi (ilk 10 terim):")
a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()

# Uygulama 2: En büyük ve en küçük sayı bulma
sayilar = [45, 23, 78, 12, 89, 34, 56]
en_buyuk = sayilar[0]
en_kucuk = sayilar[0]

for sayi in sayilar:
    if sayi > en_buyuk:
        en_buyuk = sayi
    if sayi < en_kucuk:
        en_kucuk = sayi

print("Sayılar:", sayilar)
print("En büyük:", en_buyuk)
print("En küçük:", en_kucuk)

# Uygulama 3: Kelime sayma
metin = "python veri bilimi için çok güçlü bir programlama dilidir"
kelimeler = metin.split()
harf_sayilari = []

for kelime in kelimeler:
    harf_sayilari.append(len(kelime))

print("Metin:", metin)
print("Kelimeler ve harf sayıları:")
for i in range(len(kelimeler)):
    print(kelimeler[i], "→", harf_sayilari[i], "harf")

#######################
# 11. ÖNEMLİ İPUÇLARI
#######################

print("\n=== Önemli İpuçları ===")

# 1. Sonsuz döngüden kaçının
print("UYARI: while döngüsünde sayacı artırmayı unutmayın!")

# 2. range() kullanımına dikkat edin
print("range(5) → 0, 1, 2, 3, 4 (5 dahil değil)")
print("range(1, 6) → 1, 2, 3, 4, 5 (6 dahil değil)")

# 3. Liste elemanlarına ulaşım
liste = ["a", "b", "c"]
print("Doğru kullanım:")
for eleman in liste:
    print(eleman)

print("\nİndeks ile kullanım:")
for i in range(len(liste)):
    print("İndeks", i, ":", liste[i])

print("\n=== Bu Derste Öğrendiklerimiz ===")
print("✓ for döngüsü ile listeler üzerinde gezinme")
print("✓ range() fonksiyonu kullanımı")
print("✓ while döngüsü ve sayaç mantığı")
print("✓ Döngülerde koşullar kullanma")
print("✓ İç içe döngüler")
print("✓ Fonksiyonlarla döngü kombinasyonları")
print("✓ Pratik matematik uygulamaları")

print("\nSıradaki ders: Pratik uygulama örnekleri")
