# =======================================================
# PYTHON DERS 12: KÜMELER (set)
# =======================================================

# Önceki derste sözlükleri öğrendik.
# Bu derste küme (set) veri türünü öğreneceğiz.
# Kümeler benzersiz elemanları saklar ve tekrarları otomatik siler.

# Öğreneceğiniz konular:
#   - Küme oluşturma
#   - Kümelerin benzersiz özelliği
#   - Kümeye eleman ekleme/çıkarma
#   - Küme işlemleri (birleşim, kesişim)
#   - Küme kontrolü
#   - Pratik uygulama örnekleri

print("Python Kümeler Dersine Hoş Geldiniz!")

# Liste: Her şey değiştirilebilir, []
# Tuple: Değiştirilemez, ()
# Sözlükler: Anahtar-Değer ilişkisiyle çalışır. 
# Set/Kümeler:

###############################################
# KÜMELER (SET)
###############################################

#######################
# Tanım ve Atama
#######################

bos_kume = set()
kume = {1, 2, 3, 3, 4, 5}  # Tekrarlı elemanlar otomatik silinir

print("bos_kume türü:", type(bos_kume))
print("kume        :", kume)  # {1, 2, 3, 4, 5}

#######################
# Eleman Ekleme ve Çıkarma
#######################

kume.add(6)
print("add(6) sonrası:", kume)

kume.remove(3)  # 3 elemanını çıkarır, yoksa hata verir
print("remove(3) sonrası:", kume)

kume.discard(10)  # 10 yok, hata vermez
print("discard(10) sonrası:", kume)

cikarilan = kume.pop()  # Rastgele bir eleman çıkarır
print("pop() ile çıkarılan:", cikarilan)
print("pop sonrası:", kume)

#######################
# Kümeler Arası İşlemler
#######################

kume1 = {1, 2, 3}
kume2 = {3, 4, 5}

print("kume1:", kume1)
print("kume2:", kume2)

print("Birleşim (union):", kume1.union(kume2))        # {1,2,3,4,5}
print("Kesişim (intersection):", kume1.intersection(kume2))  # {3}
print("Fark (difference):", kume1.difference(kume2)) # {1,2}
print("Simetrik Fark (symmetric_difference):", kume1.symmetric_difference(kume2))  # {1,2,4,5}

#######################
# Kümeden Liste ve Tuple Dönüşümleri
#######################

liste = list(kume1)
demet = tuple(kume1)
print("Listeye dönüşüm:", liste)
print("Tuple'a dönüşüm:", demet)
