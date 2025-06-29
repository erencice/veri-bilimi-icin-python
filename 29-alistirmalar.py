"""
29. ALIŞTIRMALAR - SINIF VE OOP ALIŞTIRMALARı
===========================================

Bu dosya nesne yönelimli programlama (OOP) konularını pekiştirmek 
için tasarlanmış kapsamlı alıştırmaları içerir.

Kullanılan Konular:
- Sınıflar (class) ve nesne oluşturma
- __init__ metodları (constructor)
- Instance ve class değişkenleri
- Metodlar ve fonksiyonlar
- Inheritance (kalıtım)
- Encapsulation (kapsülleme)
- Hata yakalama ile entegrasyon
- Gerçek hayat uygulamaları
"""

print("=" * 50)
print("SINIF VE OOP ALIŞTIRMALARı")
print("=" * 50)

# ALIŞTIRMA 1: Öğrenci Sınıfı
print("\n1. ALIŞTIRMA: ÖĞRENCİ SINIFI")
print("-" * 30)
print("Açıklama: Öğrenci bilgilerini yöneten bir sınıf oluşturun.")
print()
print("Görevler:")
print("• Ogrenci sınıfı oluşturun")
print("• __init__ metodu: ad, soyad, numara, notlar=[])") 
print("• not_ekle(ders, not) metodu")
print("• ortalama_hesapla() metodu")
print("• durum_belirle() metodu (geçti/kaldı)")
print("• bilgi_goster() metodu")
print()
print("Kurallar:")
print("• Ortalama >= 60: Geçti")
print("• Ortalama < 60: Kaldı")
print("• Notlar 0-100 arası olmalı")
print()
print("Test Kodu:")
print("ogrenci = Ogrenci('Ali', 'Veli', '123')")
print("ogrenci.not_ekle('Matematik', 85)")
print("ogrenci.not_ekle('Fizik', 90)")
print("print(ogrenci.ortalama_hesapla())  # 87.5")
print("print(ogrenci.durum_belirle())     # Geçti")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# ALIŞTIRMA 2: Banka Hesabı Sınıfı
print("\n\n2. ALIŞTIRMA: BANKA HESABI SINIFI")
print("-" * 35)
print("Açıklama: Banka hesabı işlemlerini yöneten sınıf oluşturun.")
print()
print("Görevler:")
print("• BankaHesabi sınıfı oluşturun")
print("• __init__ metodu: hesap_no, ad, bakiye=0")
print("• para_yatir(miktar) metodu")
print("• para_cek(miktar) metodu")
print("• bakiye_goster() metodu") 
print("• transfer(diger_hesap, miktar) metodu")
print()
print("Kurallar:")
print("• Bakiye negatif olamaz")
print("• Para çekme işleminde bakiye kontrolü")
print("• Transfer işleminde hem çekme hem yatırma")
print()
print("Hata Kontrolü:")
print("• Yetersiz bakiye durumu")
print("• Negatif miktar girişi")
print("• Geçersiz hesap numarası")
print()
print("Test Kodu:")
print("hesap1 = BankaHesabi('001', 'Ahmet', 1000)")
print("hesap2 = BankaHesabi('002', 'Mehmet', 500)")
print("hesap1.transfer(hesap2, 200)")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# ALIŞTIRMA 3: Araç Sınıfı Hiyerarşisi
print("\n\n3. ALIŞTIRMA: ARAÇ SINIFI HİYERARŞİSİ")
print("-" * 40)
print("Açıklama: Inheritance kullanarak araç sınıfları oluşturun.")
print()
print("Görevler:")
print("• Ana sınıf: Arac(marka, model, yil)")
print("• Alt sınıflar: Otomobil, Motorsiklet")
print("• Her sınıfın kendine özgü özellikleri olmalı")
print("• bilgi_goster() metodu her sınıfta olmalı")
print("• yakit_tuketimi_hesapla() metodu ekleyin")
print()
print("Sınıf Özellikleri:")
print("• Arac: marka, model, yil")
print("• Otomobil: + kapi_sayisi, bagaj_hacmi")
print("• Motorsiklet: + motor_hacmi, vites_sayisi")
print()
print("Metodlar:")
print("• Otomobil.bilgi_goster(): 'Marka Model (Yıl) - 4 kapılı'")
print("• Motorsiklet.bilgi_goster(): 'Marka Model (Yıl) - 250cc'")
print()
print("Test Kodu:")
print("araba = Otomobil('Toyota', 'Corolla', 2020, 4, 470)")
print("motor = Motorsiklet('Yamaha', 'R25', 2021, 250, 6)")
print("araba.bilgi_goster()")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# ALIŞTIRMA 4: Kütüphane Yönetim Sistemi
print("\n\n4. ALIŞTIRMA: KÜTÜPHANE YÖNETİM SİSTEMİ")
print("-" * 40)
print("Açıklama: Kitap ve kütüphane yönetimi için sınıflar oluşturun.")
print()
print("Görevler:")
print("• Kitap sınıfı: isbn, baslik, yazar, durum='mevcut'")
print("• Kutuphane sınıfı: kitap listesi yönetimi")
print("• kitap_ekle(), kitap_ara(), odunc_ver() metodları")
print("• kitap_iade_al(), mevcut_kitaplar() metodları")
print("• İstatistik metodları ekleyin")
print()
print("Kitap Sınıfı:")
print("• __init__(isbn, baslik, yazar)")
print("• __str__ metodu güzel çıktı için")
print("• odunc_durumu_degistir() metodu")
print()
print("Kütüphane Sınıfı:")
print("• kitap_ekle(kitap) - kitap objesi ekler")
print("• kitap_ara(baslik) - başlığa göre arar")
print("• odunc_ver(isbn) - ödünç verme işlemi")
print("• raporla() - genel istatistikleri gösterir")
print()
print("Test Kodu:")
print("kitap1 = Kitap('123', '1984', 'Orwell')")
print("kutuphane = Kutuphane()")
print("kutuphane.kitap_ekle(kitap1)")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# ALIŞTIRMA 5: Oyun Karakteri Sistemi
print("\n\n5. ALIŞTIRMA: OYUN KARAKTERİ SİSTEMİ")
print("-" * 40)
print("Açıklama: RPG oyunu için karakter sistemi oluşturun.")
print()
print("Görevler:")
print("• Karakter ana sınıfı: ad, seviye, can, guc")
print("• Alt sınıflar: Savasci, Buyucu, Okcu")
print("• Her karakterin özel yetenekleri olmalı")
print("• Savaş sistemi ekleyin")
print("• Seviye atlama sistemi")
print()
print("Karakter Sınıfı:")
print("• __init__(ad): başlangıç değerleri")
print("• saldir(hedef) metodu")
print("• hasar_al(miktar) metodu")
print("• seviye_atla() metodu")
print("• durum_goster() metodu")
print()
print("Alt Sınıflar:")
print("• Savasci: yüksek can, normal güç")
print("• Buyucu: düşük can, yüksek büyü gücü")
print("• Okcu: orta can, uzaktan saldırı")
print()
print("Özel Yetenekler:")
print("• Savasci.kalkani_aktifle()")
print("• Buyucu.buyucu_saldir()")
print("• Okcu.kritik_ok()")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# ALIŞTIRMA 6: E-Ticaret Sistemi
print("\n\n6. ALIŞTIRMA: E-TİCARET SİSTEMİ")
print("-" * 35)
print("Açıklama: Basit e-ticaret sistemi sınıfları oluşturun.")
print()
print("Görevler:")
print("• Urun sınıfı: ad, fiyat, stok")
print("• Sepet sınıfı: ürün listesi yönetimi")
print("• Musteri sınıfı: müşteri bilgileri")
print("• Siparis sınıfı: sipariş işlemleri")
print()
print("Urun Sınıfı:")
print("• __init__(ad, fiyat, stok)")
print("• stok_guncelle(miktar) metodu")
print("• indirim_uygula(yuzde) metodu")
print()
print("Sepet Sınıfı:")
print("• urun_ekle(urun, adet) metodu")
print("• urun_cikar(urun) metodu")
print("• toplam_tutar() metodu")
print("• sepeti_bosalt() metodu")
print()
print("Özellikler:")
print("• Stok kontrolü")
print("• İndirim hesaplama")
print("• KDV dahil fiyat")
print("• Kargo ücreti hesaplama")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


# BONUS ALIŞTIRMA: Dosya Yöneticisi
print("\n\n7. BONUS ALIŞTIRMA: DOSYA YÖNETİCİSİ")
print("-" * 40)
print("Açıklama: Dosya işlemlerini yöneten sınıf sistemi oluşturun.")
print()
print("Görevler:")
print("• Dosya sınıfı: dosya bilgileri")
print("• Klasor sınıfı: klasör yönetimi")
print("• DosyaYoneticisi sınıfı: genel işlemler")
print("• Dosya/klasör oluşturma, silme, taşıma")
print("• Arama ve filtreleme özellikleri")
print()
print("Özellikler:")
print("• Dosya boyutu hesaplama")
print("• Dosya tipi belirleme")
print("• Son değişiklik tarihi")
print("• Dosya izinleri kontrolü")
print()
print("DosyaYoneticisi Metodları:")
print("• dosya_olustur(ad, icerik)")
print("• klasor_olustur(ad)")
print("• dosya_ara(desen)")
print("• dosya_boyutu_hesapla()")
print("• yedek_olustur()")

# ÇÖZÜM ALANI:
print("\n--- ÇÖZÜMÜNÜZÜ BURAYA YAZIN ---")


print("\n" + "=" * 50)
print("ALIŞTIRMA TAMAMLAMA KONTROL LİSTESİ")
print("=" * 50)
print("□ Alıştırma 1: Öğrenci sınıfı")
print("□ Alıştırma 2: Banka hesabı sınıfı")
print("□ Alıştırma 3: Araç sınıfı hiyerarşisi")
print("□ Alıştırma 4: Kütüphane yönetim sistemi")
print("□ Alıştırma 5: Oyun karakteri sistemi")
print("□ Alıştırma 6: E-ticaret sistemi")
print("□ Bonus: Dosya yöneticisi")
print()
print("🎯 Bu alıştırmalar nesne yönelimli programlamayı pekiştirir!")
print("💡 Her alıştırma gerçek dünya uygulamalarını simüle eder.")
print("✨ Sınıfları tamamladıktan sonra Python'da uzman seviyesindesiniz!")
print("🚀 Artık kendi projelerinizi geliştirebilirsiniz!")
