import pypyodbc as pypyodbc

def baglanti():
    try:
        conn = pypyodbc.connect(
            "DRIVER={SQL Server};"
            "SERVER=.\\SQLEXPRESS;"
            "DATABASE=pythonDeneme;"
            "Trusted_Connection=yes;"
        )

        cursor = conn.cursor()
        return conn,cursor
    except Exception as e:
       print(f"Bağalntı hatası ! Nedeni : {e}")
       exit()

conn, cursor = baglanti()

def yardim():
        
    
    print("1. Kitapları Görüntüle")
    print("2. Kitap Ekle")
    print("3. Kitap Sil")
    print("4. Kitap Ara")
    print("5. Kitap Ödünç Al")
    print("6. Kitap Geri Getir")
    print("7. Çıkış")
    print("8. Yardım Menüsü")



class kütüphane:
    def __init__(self):
        pass

    def kitap_goruntule(self):
        cursor.execute("SELECT * FROM kitaplar")
        kitapBilgi = cursor.fetchall()
        if kitapBilgi:
            conn.commit()
            for id,ad,yazar,yayın,stok in kitapBilgi:
                print(f"Kitap id : {id} Kitap adı : {ad} Kitap yazarı : {yazar} Kitap yayın yılı : {yayın} Kitap stok durumu : {stok}")
        else:
            print("Kütüphanede herhangi bir kitap mevcut değil !")
    def kitap_ekle(self):
        try:
            kitapAdı = input("Eklemek istediğiniz kitap adı : ")
            cursor.execute("SELECT * FROM kitaplar")
            varMi = cursor.fetchall()
            if varMi:
                mevcutKitapAdi = varMi[1] 
                if kitapAdı in mevcutKitapAdi:
                    print(f"{kitapAdı} adlı kitap zaten mevcut !")
                else:
                    kitapYazarı = input(f"{kitapAdı} kitabının yazarı : ")
                    kitapYayın = int(input(f"{kitapAdı} kitabının yayın yılı : "))
                    cursor.execute("INSERT INTO kitaplar values (?,?,?,?)",([kitapAdı,kitapYazarı,kitapYayın,"Mevcut"]))
                    print(f"{kitapAdı} kitabı başarıyla kütüphaneye eklendi !")
            else:
                kitapYazarı = input(f"{kitapAdı} kitabının yazarı : ")
                kitapYayın = int(input(f"{kitapAdı} kitabının yayın yılı : "))
                cursor.execute("INSERT INTO kitaplar values (?,?,?,?)",([kitapAdı,kitapYazarı,kitapYayın,"Mevcut"]))
                print(f"{kitapAdı} kitabı başarıyla kütüphaneye eklendi !")
        except Exception as e:
            print(f"Hatalı veri girişi {e}")

    def kitap_sil(self):
        try:
            silId = int(input("Silmek istediğiniz kitabın ID'sini giriniz : "))
            cursor.execute(f"SELECT * FROM kitaplar WHERE kitap_id = {silId}")
            
            varMi = cursor.fetchone()
            if varMi:
                kitapAdi=varMi[1]
                cursor.execute(f"DELETE FROM kitaplar WHERE kitap_id = {silId}")
                print(f"{kitapAdi} başarıyla silindi !")
            else:
                print(f"{silId} ID'sinde herhangi bir kitap bulunamadı !")
        except Exception as e:
            print(f"Hatalı veri girişi {e}")
        finally:
            conn.commit()
        
    def kitap_ara(self):
        try:
            araId = int(input("Aramak istediğiniz kitabın ID'sini giriniz :"))
            cursor.execute(f"SELECT * FROM kitaplar WHERE kitap_id = {araId}")
            bul= cursor.fetchone()
            if bul:

                kitap_id = bul[0]
                kitap_adi = bul[1]
                kitap_yazari = bul[2]
                kitap_yayin = bul[3]
                kitap_stok = bul[4]
                print(f"Kitap ID : {kitap_id} Kitap adı : {kitap_adi} Kitabın yazarı : {kitap_yazari} Kitabın yayın yılı : {kitap_yayin} Kitabın stok durumu : {kitap_stok}")
            else:
                print(f"{araId} ID'sine sahip bir kitap bulunamadı !")

        except Exception as e:
            print(f"Hatalı veri girişi {e}")
        finally:
            conn.commit()
    
    def kitap_oducal(self):
        try:
            oducId = int(input("Ödün almak istediğiniz kitabın ID'sini giriniz :"))
            cursor.execute(f"SELECT * FROM kitaplar WHERE kitap_id = {oducId}")
            
            kitap = cursor.fetchone()
            if kitap:

                kitap_durumu = kitap[4]
                kitapAdı = kitap[1]
                if kitap_durumu == "Mevcut":

                    cursor.execute(f"UPDATE kitaplar SET stok_durumu = 'Ödünç Verildi' WHERE kitap_id = {oducId}")
                    print(f"{kitapAdı} başarıyla ödünç verildi...")
                else:
                    print(f"{kitapAdı} zaten ödünç alınmış!")
            else:
                print(f"{oducId} ID'sine sahip bir kitap bulunamadı !")
        except Exception as e:
            print(f"Hatalı veri girişi {e}")

    def kitap_geri_getir(self):
        try:
            geriId= int(input("Geri getirmek istediğiniz kitabın ID'sini giriniz :"))
            cursor.execute(f"SELECT * FROM kitaplar WHERE kitap_id = {geriId}")
            geriGetir = cursor.fetchone()
            if geriGetir:
                geriGetirAd = geriGetir[1]
                durum = geriGetir[4]
                if durum == "Ödünç Verildi":
                    cursor.execute(f"UPDATE kitaplar SET stok_durumu = 'Mevcut' WHERE kitap_id = {geriId}")
                    print(f"{geriGetirAd} kitabı başarıyla geri verildi !")
                else:
                    print(f"{geriGetirAd} kitabı zaten ödünç alınmamış !")
            else:
                print(f"{geriId} ID'sine sahip bir kitap bulunamadı !")
        except Exception as e:
            print(f"Hatalı veri girişi {e}")
        finally:
            conn.commit()


def main():
    yardim()
    user1 = kütüphane()
    try:
        while True:
            secim = input("Yapmak istediğiniz işlemi giriniz :")
            if secim == "1":
                user1.kitap_goruntule()
            elif secim == "2":
                
                user1.kitap_ekle()
            elif secim == "3":
                
                user1.kitap_sil()
            elif secim == "4":
                
                user1.kitap_ara()
            elif secim == "5":
                
                user1.kitap_oducal()
            elif secim == "6":
                 
                user1.kitap_geri_getir()
            elif secim == "7":
                print("Çıkış yapılıyor. İyi günler!")
                break
            elif secim == "8":
                yardim()
            else:
                print("Geçersiz seçim! Lütfen tekrar deneyin.")

    except Exception as e:
            print(f"Hatalı veri girişi {e}")

main()