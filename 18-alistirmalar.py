"""
18. ALIŞTIRMALAR - DÖNGÜLER VE STRING İŞLEMLERİ
==============================================

Bu dosya döngüler, koşullar ve string işlemlerini birleştiren
pratik alıştırmalar içerir.

Kullanılan Konular:
- for ve while döngüleri
- if-elif-else koşul yapıları
- String indeksleme ve işlemleri
- range() fonksiyonu
- enumerate() fonksiyonu
- String metodları (upper(), lower(), etc.)
- Fonksiyon tanımlama
"""

print("=" * 50)
print("ALIŞTIRMALAR - DÖNGÜLER VE STRING İŞLEMLERİ")
print("=" * 50)

# ALIŞTIRMA 1: Çift İndeksli Karakterleri Büyütme
print("\n1. ALIŞTIRMA: ÇİFT İNDEKSLİ KARAKTERLERİ BÜYÜTME")
print("-" * 50)
print("Açıklama: Bir string'in çift indeksli karakterlerini büyük harf yapın.")
print()
print("Görev:")
print("• Verilen bir string'de çift indeksli karakterleri büyük harf yapın")
print("• Tek indeksli karakterler küçük harf kalacak")
print("• Sonucu ekrana yazdırın")
print()
print("Örnek:")
orjinal_metin = "hi my name is john and i am learning python"
print(f"Girdi:  '{orjinal_metin}'")
print("Çıktı:  'Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN'")
print()
print("Kural:")
print("• İndeks 0, 2, 4, 6, 8, ... → BÜYÜK HARF")
print("• İndeks 1, 3, 5, 7, 9, ... → küçük harf")
print()
print("İpuçları:")
print("• enumerate() fonksiyonu kullanın")
print("• % operatörü ile çift/tek kontrolü yapın")
print("• upper() ve lower() metodlarını kullanın")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# ALIŞTIRMA 2: Sayı Tahmin Oyunu
print("\n\n2. ALIŞTIRMA: SAYI TAHMİN OYUNU")
print("-" * 35)
print("Açıklama: Bilgisayarın tuttuğu sayıyı tahmin etme oyunu yapın.")
print()
print("Görevler:")
print("• 1-100 arası rastgele bir sayı belirleyin (50 olarak sabit alabilirsiniz)")
print("• Kullanıcıdan tahmin isteyin")
print("• 'Daha büyük' veya 'Daha küçük' ipucu verin")
print("• Doğru tahmin edildiğinde tebrik edin")
print("• Maksimum 7 tahmin hakkı verin")
print()
print("Örnek Akış:")
print("Tahmin edin (1-100): 75")
print("Daha küçük!")
print("Tahmin edin (1-100): 25")
print("Daha büyük!")
print("Tahmin edin (1-100): 50")
print("Tebrikler! 3 tahminde bildiniz!")
print()
print("İpuçları:")
print("• while döngüsü kullanın")
print("• Sayaç ile tahmin sayısını takip edin")
print("• input() ve int() kullanın")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# ALIŞTIRMA 3: Kelime Analizi
print("\n\n3. ALIŞTIRMA: KELİME ANALİZİ")
print("-" * 30)
print("Açıklama: Bir cümledeki kelimeleri analiz edin.")
print()
print("Görevler:")
print("• Kullanıcıdan bir cümle alın")
print("• Cümledeki toplam kelime sayısını bulun")
print("• En uzun ve en kısa kelimeyi bulun")
print("• Her kelimenin uzunluğunu listeleyin")
print("• Sonuçları düzgün formatta gösterin")
print()
print("Örnek:")
ornek_cumle = "Python öğrenmek çok eğlenceli ve faydalı"
print(f"Cümle: '{ornek_cumle}'")
print("Analiz:")
print("• Toplam kelime sayısı: 5")
print("• En uzun kelime: 'eğlenceli' (9 harf)")
print("• En kısa kelime: 've' (2 harf)")
print("• Kelime uzunlukları: Python(6), öğrenmek(8), çok(3), eğlenceli(9), ve(2), faydalı(7)")
print()
print("İpuçları:")
print("• split() metodu ile kelimeleri ayırın")
print("• len() fonksiyonu ile uzunluk ölçün")
print("• max() ve min() fonksiyonlarını kullanın")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# ALIŞTIRMA 4: Çarpım Tablosu
print("\n\n4. ALIŞTIRMA: ÇARPIM TABLOSU")
print("-" * 30)
print("Açıklama: Belirtilen sayının çarpım tablosunu oluşturun.")
print()
print("Görevler:")
print("• Kullanıcıdan bir sayı alın")
print("• O sayının 1'den 10'a kadar çarpım tablosunu yazdırın")
print("• Sonuçları düzgün formatta gösterin")
print()
print("Örnek (sayı = 7):")
print("7 x 1 = 7")
print("7 x 2 = 14")
print("7 x 3 = 21")
print("...")
print("7 x 10 = 70")
print()
print("İpuçları:")
print("• for döngüsü ve range(1, 11) kullanın")
print("• f-string ile düzgün formatlama yapın")
print("• input() ve int() kullanın")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# ALIŞTIRMA 5: Asal Sayı Kontrolü
print("\n\n5. ALIŞTIRMA: ASAL SAYI KONTROLÜ")
print("-" * 35)
print("Açıklama: Verilen sayının asal olup olmadığını kontrol edin.")
print()
print("Görevler:")
print("• Kullanıcıdan bir sayı alın")
print("• Sayının asal olup olmadığını kontrol edin")
print("• Sonucu açıklayıcı mesajla gösterin")
print("• Asal değilse bölenlerini de gösterin")
print()
print("Asal Sayı Kuralı:")
print("• 1'den büyük sayılar")
print("• Sadece 1 ve kendisi ile bölünebilen sayılar")
print("• Örnek asal sayılar: 2, 3, 5, 7, 11, 13, 17, 19, 23...")
print()
print("Örnek:")
print("Sayı: 17 → Asal sayıdır!")
print("Sayı: 15 → Asal değildir. Bölenleri: 1, 3, 5, 15")
print()
print("İpuçları:")
print("• for döngüsü ile 2'den sayının yarısına kadar kontrol edin")
print("• % operatörü ile bölünebilirlik kontrolü yapın")
print("• Boolean değişken kullanın")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# ALIŞTIRMA 6: Palindrom Kontrolü
print("\n\n6. ALIŞTIRMA: PALİNDROM KONTROLÜ")
print("-" * 35)
print("Açıklama: Bir kelimenin palindrom olup olmadığını kontrol edin.")
print()
print("Görevler:")
print("• Kullanıcıdan bir kelime alın")
print("• Kelimenin palindrom olup olmadığını kontrol edin")
print("• Sonucu açıklayıcı mesajla gösterin")
print()
print("Palindrom Nedir?")
print("• Tersten okunuşu da aynı olan kelimeler")
print("• Örnek: 'kayak', 'radar', 'aba', 'sos'")
print()
print("Örnek:")
print("Kelime: 'kayak' → Palindromdur!")
print("Kelime: 'python' → Palindrom değildir.")
print()
print("İpuçları:")
print("• String'i ters çevirmek için [::-1] kullanın")
print("• lower() ile büyük-küçük harf sorununu çözün")
print("• strip() ile boşlukları temizleyin")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# BONUS ALIŞTIRMA: Fibonacci Serisi
print("\n\n7. BONUS ALIŞTIRMA: FİBONACCİ SERİSİ")
print("-" * 40)
print("Açıklama: Fibonacci serisinin ilk N terimini yazdırın.")
print()
print("Görevler:")
print("• Kullanıcıdan kaç terim istediğini alın")
print("• Fibonacci serisinin o kadar terimini yazdırın")
print("• Terimleri yan yana, virgülle ayırarak gösterin")
print()
print("Fibonacci Serisi:")
print("• Her sayı kendinden önceki iki sayının toplamı")
print("• Başlangıç: 0, 1")
print("• Devam: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...")
print()
print("Örnek (10 terim):")
print("0, 1, 1, 2, 3, 5, 8, 13, 21, 34")
print()
print("İpuçları:")
print("• İlk iki sayıyı 0 ve 1 olarak başlatın")
print("• Döngüde bir sonraki sayıyı önceki ikisinin toplamı yapın")
print("• Liste kullanarak terimleri saklayabilirsiniz")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


print("\n" + "=" * 50)
print("ALIŞTIRMA TAMAMLAMA KONTROL LİSTESİ")
print("=" * 50)
print("□ Alıştırma 1: Çift indeksli karakterleri büyütme")
print("□ Alıştırma 2: Sayı tahmin oyunu")
print("□ Alıştırma 3: Kelime analizi")
print("□ Alıştırma 4: Çarpım tablosu")
print("□ Alıştırma 5: Asal sayı kontrolü")
print("□ Alıştırma 6: Palindrom kontrolü")
print("□ Bonus: Fibonacci serisi")
print()
print("🎯 Bu alıştırmalar döngüler ve string işlemlerini pekiştirir!")
print("💡 Her alıştırmada farklı algoritma teknikleri öğreniyorsunuz.")
print("✨ Kendi çözümlerinizi geliştirmekten çekinmeyin!")
