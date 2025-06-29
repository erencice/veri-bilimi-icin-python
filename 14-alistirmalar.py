"""
14. ALIŞTIRMALAR - TEMEL PYTHON PRATİK UYGULAMALARI
==================================================

Bu dosya şimdiye kadar öğrendiğiniz konuları pekiştirmek 
için tasarlanmış alıştırmaları içerir.

Kullanılan Konular:
- input() fonksiyonu ile kullanıcı girdisi alma
- int() ve float() tip dönüşümleri  
- Matematiksel işlemler (+, -, *, /, %, **)
- String (metin) işlemleri
- print() fonksiyonu ve formatlama
- Temel veri tipleri (int, float, str, bool)
"""

print("=" * 50)
print("PRATİK ALIŞTIRMALAR - TEMEL PYTHON")
print("=" * 50)

# ALIŞTIRMA 1: Üç Sayının Çarpımı
print("\n1. ALIŞTIRMA: ÜÇ SAYININ ÇARPIMI")
print("-" * 35)
print("Açıklama: Kullanıcıdan 3 sayı alın ve bu sayıları çarpın.")
print()
print("Görevler:")
print("• Kullanıcıdan 3 adet sayı alın")
print("• Bu sayıları çarpın") 
print("• Sonucu ekrana yazdırın")
print("• Hem sayıları hem de sonucu güzel formatta gösterin")
print()
print("İpuçları:")
print("• input() her zaman string döndürür")
print("• Sayısal işlem için int() veya float() kullanın")
print("• Çarpma işlemi için * operatörünü kullanın")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# ALIŞTIRMA 2: Beden Kitle İndeksi Hesaplama
print("\n\n2. ALIŞTIRMA: BEDEN KİTLE İNDEKSİ")
print("-" * 35)
print("Açıklama: Kullanıcıdan kilo ve boy alarak BKİ hesaplayın.")
print()
print("Görevler:")
print("• Kullanıcıdan kilo (kg) ve boy (metre) alın")
print("• BKİ formülünü kullanarak hesaplama yapın")
print("• Sonucu ekrana yazdırın")
print()
print("Formül: BKİ = Kilo / (Boy × Boy)")
print("Örnek: 70 kg, 1.75 m => BKİ = 70 / (1.75 × 1.75) = 22.86")
print()
print("İpuçları:")
print("• Boy bilgisini metre cinsinden alın (örn: 1.75)")
print("• float() kullanarak ondalıklı sayı tipine çevirin")
print("• Parantez kullanarak işlem önceliğine dikkat edin")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# ALIŞTIRMA 3: Kişisel Bilgi Formu
print("\n\n3. ALIŞTIRMA: KİŞİSEL BİLGİ FORMU")
print("-" * 35)
print("Açıklama: Kullanıcı bilgilerini alın ve düzenli formatta gösterin.")
print()
print("Görevler:")
print("• Kullanıcıdan ad, soyad ve numara bilgilerini alın")
print("• Bu bilgileri düzenli bir şekilde alt alta yazdırın")
print("• Bilgileri temizleyip düzgün formatta gösterin")
print()
print("Beklenen Çıktı:")
print("Ad: Ahmet")
print("Soyad: Yılmaz") 
print("Numara: 12345")
print()
print("İpuçları:")
print("• strip() ile başta/sondaki boşlukları temizleyin")
print("• title() ile ilk harfleri büyük yapın")
print("• f-string formatını kullanabilirsiniz")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# ALIŞTIRMA 4: İki Sayının Değerlerini Değiştirme
print("\n\n4. ALIŞTIRMA: İKİ SAYININ DEĞERLERİNİ DEĞİŞTİRME")
print("-" * 45)
print("Açıklama: İki sayının değerlerini birbirleriyle değiştirin.")
print()
print("Görevler:")
print("• Kullanıcıdan iki sayı alın")
print("• Bu sayıların değerlerini birbirleriyle değiştirin")
print("• Değiştirilmeden önce ve sonra durumları gösterin")
print()
print("Örnek:")
print("Başlangıç: sayi1 = 5, sayi2 = 10")
print("Sonuç: sayi1 = 10, sayi2 = 5")
print()
print("İpuçları:")
print("• Python'da kolay yol: sayi1, sayi2 = sayi2, sayi1")
print("• Bu işleme 'tuple assignment' denir")
print("• Geçici değişken kullanma yöntemi de vardır")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# ALIŞTIRMA 5: Hipotenüs Hesaplama
print("\n\n5. ALIŞTIRMA: HİPOTENÜS HESAPLAMA")
print("-" * 35)
print("Açıklama: Dik üçgenin hipotenüsünü Pisagor teoremi ile hesaplayın.")
print()
print("Görevler:")
print("• Kullanıcıdan dik üçgenin iki dik kenarını alın")
print("• Hipotenüs uzunluğunu hesaplayın")
print("• Sonucu ekrana yazdırın")
print()
print("Formül:")
print("Pisagor Teoremi: c² = a² + b²")
print("Hipotenüs: c = √(a² + b²)")
print("Python'da: c = (a**2 + b**2) ** 0.5")
print()
print("İpuçları:")
print("• ** operatörü üs alma işlemi yapar")
print("• Karekök için 0.5 kuvvetini kullanın")
print("• float() kullanarak ondalıklı sayı alın")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# BONUS ALIŞTIRMA: Daire Alan ve Çevre
print("\n\n6. BONUS ALIŞTIRMA: DAİRE ALAN VE ÇEVRE")
print("-" * 40)
print("Açıklama: Dairenin yarıçapından alan ve çevresini hesaplayın.")
print()
print("Görevler:")
print("• Kullanıcıdan dairenin yarıçapını alın")
print("• Dairenin alanını ve çevresini hesaplayın")
print("• Sonuçları ekrana yazdırın")
print()
print("Formüller:")
print("Alan = π × r²")
print("Çevre = 2 × π × r")
print("π (pi) ≈ 3.14159")
print()
print("İpuçları:")
print("• pi = 3.14159 değişkenini tanımlayın")
print("• r**2 ile r²'yi hesaplayın")
print("• Sonuçları düzgün formatta gösterin")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


print("\n" + "=" * 50)
print("ALIŞTIRMA TAMAMLAMA KONTROL LİSTESİ")
print("=" * 50)
print("□ Alıştırma 1: Üç sayının çarpımı")
print("□ Alıştırma 2: BKİ hesaplama")
print("□ Alıştırma 3: Kişisel bilgi formu")
print("□ Alıştırma 4: İki sayının değerlerini değiştirme")
print("□ Alıştırma 5: Hipotenüs hesaplama")
print("□ Bonus: Daire alan ve çevre")
print()
print("🎯 Tüm alıştırmaları tamamladıktan sonra bir sonraki derse geçin!")
print("💡 Takıldığınız yerlerde önceki dersleri tekrar edin.")
print("✨ Kendi çözümlerinizi denemeyi unutmayın!")
