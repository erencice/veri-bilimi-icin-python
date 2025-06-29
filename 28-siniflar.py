###############################################
# 28. DERS: SINIFLAR (CLASSES) - NESNE TABANLI PROGRAMLAMA
###############################################

# Bu derste öğreneceğimiz konular:
# - Sınıf (class) kavramı
# - Nesne (object) oluşturma
# - __init__ yapıcı metod
# - Sınıf ve örnek değişkenleri
# - Metod tanımlama
# - Nesne tabanlı programlama temelieri

print("=== SINIFLAR (CLASSES) - NESNE TABANLI PROGRAMLAMA ===")

# Nesne Tabanlı Programlama (OOP): Gerçek hayattaki nesneleri 
# programda modellemek için kullanılan programlama yaklaşımı

#######################
# 1. SINIF NEDİR?
#######################

print("\n=== Sınıf Nedir? ===")

# Sınıf: Benzer özelliklere sahip nesnelerin şablonudur
# Nesne: Sınıfın somut bir örneğidir

print("Örnek: Araba sınıfı")
print("- Özellikler: marka, model, renk, hız")
print("- Davranışlar: hızlan(), fren_yap(), kornaya_bas()")

print("\nÖrnek: Öğrenci sınıfı")
print("- Özellikler: isim, yaş, not_ortalaması")
print("- Davranışlar: ders_al(), sınav_ol(), mezun_ol()")

#######################
# 2. BASİT SINIF TANIMLAMA
#######################

print("\n=== Basit Sınıf Tanımlama ===")

class Araba:
    """Basit bir araba sınıfı"""
    
    # Sınıf değişkeni (tüm nesneler için ortak)
    teker_sayisi = 4
    
    def bilgi_ver(self):
        """Araba hakkında bilgi verir"""
        print(f"Bu bir araba, {self.teker_sayisi} tekeri var")

# Nesne oluşturma (sınıfın örneği)
araba1 = Araba()
araba1.bilgi_ver()

araba2 = Araba()
araba2.bilgi_ver()

print(f"Araba 1 teker sayısı: {araba1.teker_sayisi}")
print(f"Araba 2 teker sayısı: {araba2.teker_sayisi}")

#######################
# 3. __init__ YAPICI METOD
#######################

print("\n=== __init__ Yapıcı Metod ===")

class Ogrenci:
    """Öğrenci sınıfı"""
    
    # Sınıf değişkeni
    okul_adi = "Python Öğrenme Akademisi"
    
    def __init__(self, isim, yas, numara):
        """
        Yapıcı metod - nesne oluştururken çalışır
        
        Args:
            isim (str): Öğrencinin ismi
            yas (int): Öğrencinin yaşı
            numara (int): Öğrenci numarası
        """
        # Örnek değişkenleri (her nesne için farklı)
        self.isim = isim
        self.yas = yas
        self.numara = numara
        self.notlar = []  # Boş not listesi
        
        print(f"{self.isim} adlı öğrenci oluşturuldu")
    
    def bilgi_goster(self):
        """Öğrenci bilgilerini gösterir"""
        print(f"İsim: {self.isim}")
        print(f"Yaş: {self.yas}")
        print(f"Numara: {self.numara}")
        print(f"Okul: {self.okul_adi}")
        print(f"Not sayısı: {len(self.notlar)}")

# Nesneler oluşturma
ogrenci1 = Ogrenci("Ali", 20, 123)
ogrenci2 = Ogrenci("Ayşe", 19, 124)

print("\nÖğrenci 1 bilgileri:")
ogrenci1.bilgi_goster()

print("\nÖğrenci 2 bilgileri:")
ogrenci2.bilgi_goster()

#######################
# 4. METOD TANIMLAMA
#######################

print("\n=== Metod Tanımlama ===")

class Hesap_Makinesi:
    """Basit hesap makinesi sınıfı"""
    
    def __init__(self, sahip):
        self.sahip = sahip
        self.gecmis = []  # İşlem geçmişi
        print(f"{self.sahip} için hesap makinesi hazır")
    
    def topla(self, a, b):
        """İki sayıyı toplar"""
        sonuc = a + b
        islem = f"{a} + {b} = {sonuc}"
        self.gecmis.append(islem)
        print(islem)
        return sonuc
    
    def cikar(self, a, b):
        """İki sayıyı çıkarır"""
        sonuc = a - b
        islem = f"{a} - {b} = {sonuc}"
        self.gecmis.append(islem)
        print(islem)
        return sonuc
    
    def carp(self, a, b):
        """İki sayıyı çarpar"""
        sonuc = a * b
        islem = f"{a} × {b} = {sonuc}"
        self.gecmis.append(islem)
        print(islem)
        return sonuc
    
    def bol(self, a, b):
        """İki sayıyı böler"""
        if b != 0:
            sonuc = a / b
            islem = f"{a} ÷ {b} = {sonuc}"
            self.gecmis.append(islem)
            print(islem)
            return sonuc
        else:
            print("Hata: Sıfıra bölme yapılamaz!")
            return None
    
    def gecmis_goster(self):
        """İşlem geçmişini gösterir"""
        print(f"\n{self.sahip}'in işlem geçmişi:")
        if self.gecmis:
            for i, islem in enumerate(self.gecmis, 1):
                print(f"{i}. {islem}")
        else:
            print("Henüz işlem yapılmamış")

# Test etme
hesap_makinesi = Hesap_Makinesi("Ahmet")

hesap_makinesi.topla(10, 5)
hesap_makinesi.cikar(20, 8)
hesap_makinesi.carp(6, 7)
hesap_makinesi.bol(15, 3)
hesap_makinesi.bol(10, 0)  # Hata durumu

hesap_makinesi.gecmis_goster()

#######################
# 5. __str__ METODU
#######################

print("\n=== __str__ Metodu ===")

class Kitap:
    """Kitap sınıfı"""
    
    def __init__(self, baslik, yazar, sayfa_sayisi):
        self.baslik = baslik
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
    
    def __str__(self):
        """Nesne yazdırıldığında gösterilecek format"""
        return f"'{self.baslik}' - {self.yazar} ({self.sayfa_sayisi} sayfa)"
    
    def bilgi_ver(self):
        """Detaylı kitap bilgisi"""
        print(f"Kitap: {self.baslik}")
        print(f"Yazar: {self.yazar}")
        print(f"Sayfa Sayısı: {self.sayfa_sayisi}")

# Test etme
kitap1 = Kitap("Python Öğreniyorum", "Ahmet Yılmaz", 300)
kitap2 = Kitap("Veri Bilimi", "Mehmet Demir", 450)

print("Kitap 1:", kitap1)  # __str__ metodu çalışır
print("Kitap 2:", kitap2)

print("\nDetaylı bilgi:")
kitap1.bilgi_ver()

#######################
# 6. SINIF VE ÖRNEK DEĞİŞKENLERİ
#######################

print("\n=== Sınıf ve Örnek Değişkenleri ===")

class Calisan:
    """Çalışan sınıfı"""
    
    # Sınıf değişkenleri (tüm nesneler için ortak)
    sirket_adi = "Python Teknoloji A.Ş."
    calisan_sayisi = 0
    
    def __init__(self, isim, pozisyon, maas):
        # Örnek değişkenleri (her nesne için farklı)
        self.isim = isim
        self.pozisyon = pozisyon
        self.maas = maas
        
        # Sınıf değişkenini güncelle
        Calisan.calisan_sayisi += 1
        print(f"{self.isim} şirkete katıldı. Toplam çalışan: {Calisan.calisan_sayisi}")
    
    def bilgi_goster(self):
        """Çalışan bilgilerini gösterir"""
        print(f"İsim: {self.isim}")
        print(f"Pozisyon: {self.pozisyon}")
        print(f"Maaş: {self.maas} TL")
        print(f"Şirket: {self.sirket_adi}")
    
    def zam_yap(self, oran):
        """Maaşa zam yapar"""
        eski_maas = self.maas
        self.maas = self.maas * (1 + oran / 100)
        print(f"{self.isim}'in maaşı {eski_maas} TL'den {self.maas} TL'ye yükseldi")

# Test etme
print(f"Başlangıç çalışan sayısı: {Calisan.calisan_sayisi}")

calisan1 = Calisan("Emre", "Yazılım Geliştirici", 8000)
calisan2 = Calisan("Zeynep", "Veri Analisti", 7500)
calisan3 = Calisan("Can", "Proje Yöneticisi", 9000)

print(f"\nGüncel çalışan sayısı: {Calisan.calisan_sayisi}")

print("\nÇalışan 1 bilgileri:")
calisan1.bilgi_goster()

print("\nMaaş zammı:")
calisan1.zam_yap(15)  # %15 zam

#######################
# 7. PRATİK UYGULAMA: BANKA HESABI
#######################

print("\n=== Pratik Uygulama: Banka Hesabı ===")

class BankaHesabi:
    """Banka hesabı sınıfı"""
    
    # Sınıf değişkenleri
    banka_adi = "Python Bank"
    hesap_sayisi = 0
    
    def __init__(self, hesap_sahibi, baslangic_bakiye=0):
        # Hesap numarası otomatik oluştur
        BankaHesabi.hesap_sayisi += 1
        self.hesap_no = f"PY{BankaHesabi.hesap_sayisi:04d}"
        
        self.hesap_sahibi = hesap_sahibi
        self.bakiye = baslangic_bakiye
        self.islem_gecmisi = []
        
        print(f"{self.hesap_sahibi} için hesap açıldı")
        print(f"Hesap No: {self.hesap_no}")
        print(f"Başlangıç Bakiyesi: {self.bakiye} TL\n")
    
    def __str__(self):
        return f"Hesap No: {self.hesap_no} - {self.hesap_sahibi} - Bakiye: {self.bakiye} TL"
    
    def para_yatir(self, miktar):
        """Hesaba para yatırır"""
        if miktar > 0:
            self.bakiye += miktar
            islem = f"Para Yatırma: +{miktar} TL"
            self.islem_gecmisi.append(islem)
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")
        else:
            print("Hata: Yatırılacak miktar pozitif olmalıdır!")
    
    def para_cek(self, miktar):
        """Hesaptan para çeker"""
        if miktar > 0:
            if miktar <= self.bakiye:
                self.bakiye -= miktar
                islem = f"Para Çekme: -{miktar} TL"
                self.islem_gecmisi.append(islem)
                print(f"{miktar} TL çekildi. Yeni bakiye: {self.bakiye} TL")
            else:
                print("Hata: Yetersiz bakiye!")
        else:
            print("Hata: Çekilecek miktar pozitif olmalıdır!")
    
    def bakiye_sorgula(self):
        """Bakiye sorgulama"""
        print(f"Güncel bakiye: {self.bakiye} TL")
        return self.bakiye
    
    def hesap_ozeti(self):
        """Hesap özeti gösterir"""
        print("="*40)
        print("HESAP ÖZETİ")
        print("="*40)
        print(f"Hesap No: {self.hesap_no}")
        print(f"Hesap Sahibi: {self.hesap_sahibi}")
        print(f"Banka: {self.banka_adi}")
        print(f"Güncel Bakiye: {self.bakiye} TL")
        print(f"İşlem Sayısı: {len(self.islem_gecmisi)}")
        
        if self.islem_gecmisi:
            print("\nSon İşlemler:")
            for i, islem in enumerate(self.islem_gecmisi[-5:], 1):  # Son 5 işlem
                print(f"{i}. {islem}")
        print("="*40)

# Test etme
hesap1 = BankaHesabi("Ali Yılmaz", 1000)
hesap2 = BankaHesabi("Ayşe Demir", 500)

print("Hesap 1:")
print(hesap1)

print("\nHesap 1 işlemleri:")
hesap1.para_yatir(500)
hesap1.para_cek(200)
hesap1.para_cek(2000)  # Yetersiz bakiye
hesap1.bakiye_sorgula()

print("\nHesap 2 işlemleri:")
hesap2.para_yatir(300)
hesap2.para_cek(100)

print("\nHesap özetleri:")
hesap1.hesap_ozeti()
hesap2.hesap_ozeti()

print(f"\nToplam açılan hesap sayısı: {BankaHesabi.hesap_sayisi}")

print("\n=== Bu Derste Öğrendiklerimiz ===")
print("✓ Sınıf (class) kavramı")
print("✓ Nesne (object) oluşturma")
print("✓ __init__ yapıcı metod")
print("✓ Sınıf ve örnek değişkenleri")
print("✓ Metod tanımlama")
print("✓ __str__ metodu")
print("✓ self parametresi")
print("✓ Pratik uygulamalar")

print("\nSıradaki ders: Kalıtım ve İleri OOP Konuları")

