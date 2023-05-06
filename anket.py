import random
import string
from colorama import Fore, Style
from tabulate import tabulate
from faker import Faker

class Anket():
    def __init__(self):
        self.sorular = []
        self.cevaplar = {}

    def soru_ekle(self, soru):
        self.sorular.append(soru)

    def soru_sor(self):
        for soru in self.sorular:
            cevap = input(soru + ": ")
            self.cevaplar[soru] = cevap

    def rasgele_cevaplar(self):
        fake = Faker()
        for soru in self.sorular:
            if soru == "Adınız nedir?":
                cevap = fake.first_name()
            elif soru == "Yaşınız kaç?":
                cevap = str(random.randint(18, 60))
            elif soru == "Mesleğiniz nedir?":
                cevap = fake.job()
            elif soru == "En sevdiğiniz renk nedir?":
                cevap = random.choice(["Kırmızı", "Mavi", "Yeşil", "Sarı", "Mor"])
            elif soru == "Hobileriniz neler?":
                cevap = ", ".join(random.sample(["Spor yapmak", "Kitap okumak", "Resim çizmek", "Müzik dinlemek"], 2))
            else:
                cevap = "Bilinmiyor"
            self.cevaplar[soru] = cevap

    def sonuclari_goster(self):
        print(Fore.GREEN + "Anket Sonuçları:")
        print(Style.RESET_ALL)
        tablo = []
        for soru, cevap in self.cevaplar.items():
            tablo.append([soru, cevap])
        print(tabulate(tablo, headers=["Soru", "Cevap"], tablefmt="fancy_grid"))


anket = Anket()
anket.soru_ekle("Adınız nedir?")
anket.soru_ekle("Yaşınız kaç?")
anket.soru_ekle("Mesleğiniz nedir?")
anket.soru_ekle("En sevdiğiniz renk nedir?")
anket.soru_ekle("Hobileriniz neler?")

print("Anket Programına Hoş Geldiniz!")
print("-----------------------------")
print("1. Anket Doldur")
print("2. Rastgele Cevaplarla Doldur")
print("3. Sonuçları Görüntüle")
print("q. Çıkış")

while True:
    secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/q): ")

    if secim == "1":
        print("Lütfen aşağıdaki soruları yanıtlayın:")
        anket.soru_sor()
    elif secim == "2":
        print("Rastgele cevaplarla anket dolduruluyor...")
        anket.rasgele_cevaplar()
    elif secim == "3":
        anket.sonuclari_goster()
    elif secim.lower() == "q":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz bir seçim yaptınız. Tekrar deneyin.")

