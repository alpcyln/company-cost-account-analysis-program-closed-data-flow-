import sys
from PyQt6 import QtWidgets
from PyQt6.QtSql import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QFont, QScreen, QGuiApplication, QDoubleValidator, QMouseEvent
from tasarim import *
from kayit import *
import sqlite3

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
layout = QVBoxLayout()
connection = sqlite3.connect("veritabani.db")
cursor = connection.cursor()
screen = QGuiApplication.primaryScreen()



class Kayit(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)




        
class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
                
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)       
        self.dragging = False
        self.offset = None
        self.ui.sekil.currentIndexChanged.connect(self.change_page)
        self.frame_visible = False

        veri = "global"
        veri_2 = "global"
        veri_3 = "global"
        operation = "global"
        seçilen_marka = "global"
        name = "global"
        data_id = "global"
        eklenen_tarih = "global"

        vardiyaadeti = "global"
        vardiyaadeti_2 = "global"
        vardiyaadeti_3 = "global"
        vardiyaadeti_4 = "global"
        vardiyaadeti_5 = "global"
        vardiyaadeti_6 = "global"
        vardiyaadeti_7 = "global"
        vardiyaadeti_8 = "global"

        karmarji = "global"
        vadefarki = "global"
        vadesuresi = "global"
        son_kar = "global"
        vadesuresi_2 = "global"




        connection = sqlite3.connect("veritabani.db")
        cursor = connection.cursor()

        self.ui.frame_206.hide()
        self.ui.frame_6.hide()
        self.ui.lineEdit_3.hide()
        self.ui.label_4.hide()
        self.ui.label_25.hide()
        self.ui.lineEdit_7.hide()
        self.ui.lineEdit_13.hide()
        self.ui.lineEdit_11.hide()
        self.ui.table_marka_bilgi.setColumnHidden(3, True)
        self.ui.table_makine_bilgi.setColumnHidden(4, True)
        self.ui.table_calisan_bilgi.setColumnHidden(2, True)
        self.ui.table_kw_bilgi.setColumnHidden(2, True)
        self.ui.label_29.setText("Çalışan maaş'ı (7 günlük)")
        self.kayit = Kayit()

        self.kayit.ui.stackedWidget.setCurrentIndex(1)
        self.ui.stackedWidget_12.setCurrentIndex(0)


        self.kayit.ui.btn_save.clicked.connect(self.data_1_save)
        self.kayit.ui.btn_save.clicked.connect(self.kayit_id)

        self.kayit.ui.btn_makine_bilgi_6.clicked.connect(self.error_close)        

        self.kayit.ui.btn_makine_bilgi_7.clicked.connect(self.data_marka_change)
        self.kayit.ui.btn_makine_bilgi_9.clicked.connect(self.data_makine_change)        

        



        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_8))
        self.ui.btn_maliyet.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        
        self.ui.btn_calisan_bilgi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_marka_bilgi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.btn_makine_bilgi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.btn_devam.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_7))
        self.ui.btn_devam_3.clicked.connect(lambda: self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_11))
        self.ui.btn_kwh_bilgi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))
        

        self.ui.pushButton_18.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_8))
        self.ui.pushButton_16.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pushButton_8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.pushButton_15.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.pushButton_14.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))

        self.ui.pushButton.clicked.connect(self.menu_ac)
        self.ui.pushButton_17.clicked.connect(self.menu_kapat)

        self.ui.btn_kaydet_page.clicked.connect(self.open_save)
        self.ui.pushButton_19.clicked.connect(self.open_save)

        self.ui.btn_maliyet.clicked.connect(self.data_refresh)
        self.ui.btn_maliyet.clicked.connect(self.tabloyuYenile)        
        self.ui.btn_maliyet.clicked.connect(self.tabloyuYenile_2)
        self.ui.btn_maliyet.clicked.connect(self.tabloyuYenile_3)
        self.ui.btn_maliyet.clicked.connect(self.tabloyuYenile_4)


        self.ui.btn_calisan_bilgi.clicked.connect(self.tabloyuYenile)       
        self.ui.btn_marka_bilgi.clicked.connect(self.tabloyuYenile_2)
        self.ui.btn_makine_bilgi.clicked.connect(self.tabloyuYenile_3)
        self.ui.btn_kwh_bilgi.clicked.connect(self.tabloyuYenile_4)
        self.ui.btn_home.clicked.connect(self.data_refresh)

        
        self.ui.table_marka_bilgi.cellClicked.connect(self.guncelleme_sayfasi)
        self.ui.table_calisan_bilgi.cellClicked.connect(self.guncelleme_sayfasi_3)
        self.ui.table_makine_bilgi.cellClicked.connect(self.guncelleme_sayfasi_2)
        self.ui.table_kw_bilgi.cellClicked.connect(self.guncelleme_sayfasi_4)
        self.ui.data_bilgi.cellClicked.connect(self.data_update)




        self.kilitle = False
        self.ui.data_detay.clicked.connect(self.data_detay)
        self.ui.data_sil.clicked.connect(self.data_delete)
        self.ui.data_yenile.clicked.connect(self.data_refresh)
        self.ui.btn_makine_bilgi_4.clicked.connect(self.data_refresh)
        self.ui.btn_makine_bilgi_4.clicked.connect(self.data_close)
        self.ui.btn_makine_bilgi_3.clicked.connect(self.data_delete)
        self.ui.btn_makine_bilgi_3.clicked.connect(self.data_close)

        self.ui.kwh_ekle.clicked.connect(self.veriEkle_4)
        self.ui.kwh_ekle.clicked.connect(self.tabloyuYenile_4)
        self.ui.kwh_yenile.clicked.connect(self.tabloyuYenile_4)
        self.ui.kwh_sil.clicked.connect(self.sil_4)
        self.ui.kwh_guncelle.clicked.connect(self.guncelle_4)
        self.ui.kwh_temizle.clicked.connect(self.tabloyuYenile_4)

        self.ui.calisan_ekle.clicked.connect(self.veriEkle)
        self.ui.calisan_ekle.clicked.connect(self.tabloyuYenile)
        self.ui.calisan_yenile.clicked.connect(self.tabloyuYenile)
        self.ui.calisan_sil.clicked.connect(self.sil)
        self.ui.calisan_guncelle.clicked.connect(self.guncelle)
        self.ui.calisan_temizle.clicked.connect(self.tabloyuYenile)
        
        self.ui.marka_ekle.clicked.connect(self.veriEkle_2)
        self.ui.marka_ekle.clicked.connect(self.tabloyuYenile_2)
        self.ui.marka_yenile.clicked.connect(self.tabloyuYenile_2)
        self.ui.marka_sil.clicked.connect(self.sil_2)
        self.ui.marka_guncelle.clicked.connect(self.guncelle_2)
        self.ui.marka_temizle.clicked.connect(self.tabloyuYenile_2)

        self.ui.makine_ekle.clicked.connect(self.veriEkle_3)
        self.ui.makine_ekle.clicked.connect(self.tabloyuYenile_3)
        self.ui.makine_yenile.clicked.connect(self.tabloyuYenile_3)
        self.ui.makine_sil.clicked.connect(self.sil_3)
        self.ui.makine_guncelle.clicked.connect(self.guncelle_3)
        self.ui.makine_temizle.clicked.connect(self.tabloyuYenile_3)

        current_date = QDate.currentDate()
        self.ui.dateEdit.setDate(current_date)


        # SQLite veritabanı bağlantısı
        self.connection = sqlite3.connect("veritabani.db")
        self.cursor = self.connection.cursor()

        # Veritabanı tablosunu oluşturma
    
        self.cursor.execute("CREATE TABLE IF NOT EXISTS marka_bilgi (marka_adi TEXT, marka_fiyat FLOAT, marka_kutle FLOAT, marka_id INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS makine_marka (uretim TEXT, makine_adi TEXT, makine_gunlugu FLOAT, makine_kw FLOAT, makine_kodu INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS calisan_bilgi (tarih INTEGER, calisan_gunlugu FLOAT, calisan_id INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kw_bilgi (tarih INTEGER, kwh FLOAT, kw_id INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data_1 (tarih INTEGER, data_id INTEGER, name TEXT, malzeme TEXT, sekil TEXT, veri FLOAT, veri_2 FLOAT, Veri_3 FLOAT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data_2 (data_id INTEGER, makine_name TEXT, makine_name_2 TEXT, makine_name_3 TEXT, makine_name_4 TEXT, makine_name_5 TEXT, makine_name_6 TEXT, makine_name_7 TEXT, makine_name_8 TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data_3 (data_id INTEGER, vardiye_adet TEXT, vardiye_adet_2 TEXT, vardiye_adet_3 TEXT, vardiye_adet_4 TEXT, vardiye_adet_5 TEXT, vardiye_adet_6 TEXT, vardiye_adet_7 TEXT, vardiye_adet_8 TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data_4 (data_id INTEGER, kar_marjı FLOAT, vade_suresi FLOAT, vade_farki FLOAT, istenilen_fiyat FLOAT, vade_suresi_2 FLOAT)")
       

        
        
        self.ui.sekil.currentIndexChanged.connect(self.ham_hesap)
        self.ui.marka_secim.currentIndexChanged.connect(self.ham_hesap)
        self.ui.makine_secim.currentIndexChanged.connect(self.ham_hesap)
        self.ui.makine_secim_2.currentIndexChanged.connect(self.ham_hesap)
        self.ui.makine_secim_3.currentIndexChanged.connect(self.ham_hesap)
        self.ui.makine_secim_4.currentIndexChanged.connect(self.ham_hesap)
        self.ui.makine_secim_5.currentIndexChanged.connect(self.ham_hesap)
        self.ui.makine_secim_6.currentIndexChanged.connect(self.ham_hesap)
        self.ui.makine_secim_7.currentIndexChanged.connect(self.ham_hesap)
        self.ui.makine_secim_8.currentIndexChanged.connect(self.ham_hesap)
      
         

        self.ui.cikan_talas.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.cikan_talas)
        self.ui.talas_fiyat.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.talas_fiyat)


        cursor.execute("SELECT data_id FROM data_1 ORDER BY data_id DESC LIMIT 1")
        eklenen_tarih = self.ui.dateEdit.dateTime().toString()
        son_sayi_2 = cursor.fetchone()
  
        # Son sayıyı almak
        if son_sayi_2 is not None:
          son_sayi = son_sayi_2[0]
          data_id = son_sayi + 1

        else:
           data_id = 0               
       
        self.ui.label.setText(f"{data_id}")          
        
        self.ui.dis_cap.textChanged.connect(self.ham_hesap)
        layout.addWidget(self.ui.dis_cap)

        self.ui.uzunluk.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.uzunluk)
        
        self.ui.dis_cap_3.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.dis_cap_3)
        self.ui.uzunluk_3.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.uzunluk_3)
        self.ui.ic_cap_2.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.ic_cap_2)
        
        self.ui.en_3.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.en_3)
        self.ui.genislik_3.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.genislik_3)
        self.ui.uzunluk_4.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.uzunluk_4)
        
        self.ui.en_4.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.en_4)
        self.ui.genislik_4.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.genislik_4)
        self.ui.uzunluk_5.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.uzunluk_5)

        #self.ui.dis_cap.textChanged.connect(self.ham_hesap)  
        #layout.addWidget(self.ui.dis_cap)
        #self.ui.dis_cap.textChanged.connect(self.ham_hesap)  
        #layout.addWidget(self.ui.dis_cap)

        self.ui.en_7.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.en_7)
        self.ui.uzunluk_10.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.uzunluk_10)
        
        self.ui.agirlik_6.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.agirlik_6)

        self.ui.vardiya_adeti.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.vardiya_adeti)
        self.ui.vardiya_adeti_2.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.vardiya_adeti_2)
        self.ui.vardiya_adeti_3.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.vardiya_adeti_3)
        self.ui.vardiya_adeti_4.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.vardiya_adeti_4)
        self.ui.vardiya_adeti_5.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.vardiya_adeti_5)
        self.ui.vardiya_adeti_6.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.vardiya_adeti_6)
        self.ui.vardiya_adeti_7.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.vardiya_adeti_7)
        self.ui.vardiya_adeti_8.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.vardiya_adeti_8)
        self.ui.toplam_urun.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.toplam_urun)

 
        

        
        self.ui.kar_marji.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.kar_marji)
        self.ui.vade_suresi.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.vade_suresi)
        self.ui.vade_farki.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.vade_farki)
        self.ui.vade_suresi_2.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.vade_suresi_2)
        self.ui.vade_farki_2.textChanged.connect(self.ham_hesap)  
        layout.addWidget(self.ui.vade_farki_2)
        self.ui.pushButton_2.clicked.connect(self.toggleFullScreen)
        self.ui.pushButton_3.clicked.connect(self.toggleMinimize)

        self.auto_click_button()

        self.showFullScreen()

    def auto_click_button(self):
        self.ui.btn_maliyet.click()

    def toggleFullScreen(self):
        if self.isFullScreen():
            self.showNormal()  # Pencereyi normal boyuta getir
  
        else:
            self.showFullScreen()  # Pencereyi tam ekran yap
    def toggleMinimize(self):
       self.showMinimized()

    def menu_ac(self):
       self.ui.frame_6.show()
       self.ui.frame_207.hide()



    def menu_kapat(self):
       self.ui.frame_6.hide()
       self.ui.frame_207.show() 

    def open_save(self):

       self.kayit.show()
       self.kayit.ui.stackedWidget.setCurrentIndex(0)

    def error_close(self):
       self.kayit.hide()






    def change_page(self, index):
        # Seçilen ComboBox öğesine göre StackedWidget'ı değiştir
        self.ui.stackedWidget_2.setCurrentIndex(index)

    def kayit_id(self):
      cursor.execute("SELECT data_id FROM data_1 ORDER BY data_id DESC LIMIT 1")
      eklenen_tarih = self.ui.dateEdit.dateTime().toString()
      son_sayi_2 = cursor.fetchone()

        # Son sayıyı almak
      if son_sayi_2 is not None:
        son_sayi = son_sayi_2[0]
        data_id = son_sayi + 1
          
      else:
         data_id = 0               
       
      self.ui.label.setText(f"{data_id}")




    def veriEkle(self):
    # QLineEdit alanlarından verileri al,

      cursor.execute("SELECT calisan_id FROM calisan_bilgi ORDER BY calisan_id DESC LIMIT 1")
      son_sayi_2 = cursor.fetchone()

        # Son sayıyı almak
      if son_sayi_2 is not None:
        son_sayi = son_sayi_2[0]
        calisan_id = son_sayi + 1
          
      else:
         calisan_id = 0
      
      if self.ui.calisan_maasi.text() == "" or self.ui.calisan_maasi.text().replace('.', '', 1).isdigit() == False:
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         self.kayit.ui.label_2.setText("Maaş kısmında hatalı veya boş giriş yapıldı")
      else:
         calisan_gunlugu = float(self.ui.calisan_maasi.text())
         eklenen_tarih = self.ui.dateEdit.dateTime().toString()
         self.cursor.execute("INSERT INTO calisan_bilgi VALUES (?, ?, ?)", (eklenen_tarih, calisan_gunlugu, calisan_id))
         self.connection.commit()
      
      self.tabloyuYenile()



    def veriEkle_2(self):
    # QLineEdit alanlarından verileri al,

      cursor.execute("SELECT marka_id FROM marka_bilgi ORDER BY marka_id DESC LIMIT 1")
      son_sayix = cursor.fetchone()

        # Son sayıyı almak
      if son_sayix is not None:
        son_sayi = son_sayix[0]
        marka_id = son_sayi + 1
          
      else:
         marka_id = 0

      veri_kontrol = str()

      if self.ui.lineEdit_4.text() == "":
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         self.kayit.ui.label_2.setText("Marka adı kısmını boş geçemezsiniz")
         veri_kontrol = "1. veri girişi boş ya da hatalı"      
      else:
         marka_adi = self.ui.lineEdit_4.text()

      if self.ui.lineEdit_5.text() == "" or self.ui.lineEdit_5.text().replace('.', '', 1).isdigit() == False:
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         self.kayit.ui.label_2.setText("Marka fiyatı kısmında hatalı veya boş giriş yapıldı")
         veri_kontrol += "2. veri girişi boş ya da hatalı"      
      else:
         marka_fiyat = float(self.ui.lineEdit_5.text())

      if self.ui.lineEdit_6.text() == "" or self.ui.lineEdit_6.text().replace('.', '', 1).isdigit() == False:
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         self.kayit.ui.label_2.setText("Marka fiyatı kısmında hatalı veya boş giriş yapıldı")
         veri_kontrol += "3. veri girişi boş ya da hatalı"      
      else:
         marka_kutle = float(self.ui.lineEdit_6.text())
      
      if len(veri_kontrol) == 0:
         self.cursor.execute("INSERT INTO marka_bilgi VALUES (?, ?, ?, ?)", (marka_adi, marka_fiyat, marka_kutle, marka_id))
         self.connection.commit()



      self.tabloyuYenile_2()

    def veriEkle_3(self):
    # QLineEdit alanlarından verileri al
      cursor.execute("SELECT makine_kodu FROM makine_marka ORDER BY makine_kodu DESC LIMIT 1")
      son_sayix_2 = cursor.fetchone()

        # Son sayıyı almak
      if son_sayix_2 is not None:
        son_sayi_2 = son_sayix_2[0]
        makine_kodu = son_sayi_2 + 1
          
      else:
         makine_kodu = 0
      
      veri_kontrol = str()

      uretim_turu = self.ui.makine_kodu_2.currentText()

      if self.ui.lineEdit_8.text() == "":
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         self.kayit.ui.label_2.setText("Makine adı kısmını boş geçemezsiniz")
         veri_kontrol = "1. veri girişi boş ya da hatalı"      
      else:
         makine_adi = self.ui.lineEdit_8.text()

      if self.ui.lineEdit_9.text() == "" or self.ui.lineEdit_9.text().replace('.', '', 1).isdigit() == False:
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         self.kayit.ui.label_2.setText("Makine fiyatı kısmında hatalı veya boş giriş yapıldı")
         veri_kontrol += "2. veri girişi boş ya da hatalı"      
      else:
         makine_fiyati = float(self.ui.lineEdit_9.text())

      if self.ui.lineEdit_10.text() == "" or self.ui.lineEdit_10.text().replace('.', '', 1).isdigit() == False:
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         self.kayit.ui.label_2.setText("Kw fiyatı kısmında hatalı veya boş giriş yapıldı")
         veri_kontrol += "3. veri girişi boş ya da hatalı"      
      else:
         makine_kw = float(self.ui.lineEdit_10.text())

      if len(veri_kontrol) == 0:
         self.cursor.execute("INSERT INTO makine_marka VALUES (?, ?, ?, ?, ?)", (uretim_turu, makine_adi, makine_fiyati,makine_kw, makine_kodu))
         self.connection.commit()


      self.tabloyuYenile_3()

    def veriEkle_4(self):
    # QLineEdit alanlarından verileri al,

      cursor.execute("SELECT kw_id FROM kw_bilgi ORDER BY kw_id DESC LIMIT 1")
      son_sayi_4 = cursor.fetchone()

        # Son sayıyı almak
      if son_sayi_4 is not None:
        son_sayi_4 = son_sayi_4[0]
        kw_id = son_sayi_4 + 1
          
      else:
         kw_id = 0
      
      
      if self.ui.lineEdit_12.text() == "" or self.ui.lineEdit_12.text().replace('.', '', 1).isdigit() == False:
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         self.kayit.ui.label_2.setText("Kw bedel kısmında hatalı veya boş giriş yapıldı")
      else:
         kw_bedel = float(self.ui.lineEdit_12.text())
         eklenen_tarih = self.ui.dateEdit.dateTime().toString()
         self.cursor.execute("INSERT INTO kw_bilgi VALUES (?, ?, ?)", (eklenen_tarih, kw_bedel,kw_id))
         self.connection.commit()
      
      
      self.tabloyuYenile_4()


    def sil(self, tabloyuYenile):
       
      if self.ui.lineEdit_13.text() == "":
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         self.kayit.ui.label_2.setText("Tablodan seçim yapınız")     
      else:       
         calisan_id = self.ui.lineEdit_13.text()
         self.cursor.execute("DELETE FROM calisan_bilgi WHERE calisan_id = ?", (calisan_id,))
         self.connection.commit()
         self.ui.calisan_maasi.clear()
         self.ui.lineEdit_13.clear()
         self.tabloyuYenile()


    def sil_2(self, tabloyuYenile_2):
       
      if self.ui.lineEdit_3.text() == "":
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         self.kayit.ui.label_2.setText("Tablodan seçim yapınız")     
      else:
         marka_id = self.ui.lineEdit_3.text()
         self.cursor.execute("DELETE FROM marka_bilgi WHERE marka_id = ?", (marka_id,))
         self.connection.commit()
         self.ui.lineEdit_7.clear()
         self.tabloyuYenile_2()

    def sil_3(self, tabloyuYenile_3):
       
      if self.ui.lineEdit_7.text() == "":
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         self.kayit.ui.label_2.setText("Tablodan seçim yapınız")     
      else:       
         makine_kodu = self.ui.lineEdit_7.text()
         self.cursor.execute("DELETE FROM makine_marka WHERE makine_kodu = ?", (makine_kodu,))
         self.connection.commit()
         self.ui.lineEdit_7.clear()
         self.tabloyuYenile_3()
    
    def sil_4(self, tabloyuYenile_4):
       
      if self.ui.lineEdit_11.text() == "":
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         self.kayit.ui.label_2.setText("Tablodan seçim yapınız")     
      else:              
         kw_id = self.ui.lineEdit_11.text()
         self.cursor.execute("DELETE FROM kw_bilgi WHERE kw_id = ?", (kw_id,))
         self.connection.commit()
         self.ui.lineEdit_12.clear()
         self.ui.lineEdit_11.clear()
         self.tabloyuYenile_4()       
  

    def tabloyuYenile(self):    

    # Tüm verileri yeniden al
      self.cursor.execute("SELECT * FROM calisan_bilgi")
   
      veriler = self.cursor.fetchall()
     

    ## Tabloya verileri aktar ##
      self.ui.table_calisan_bilgi.setRowCount(len(veriler))
      self.ui.table_calisan_bilgi.setColumnCount(3)

      


      for satir, veri in enumerate(veriler):
         for sutun, deger in enumerate(veri):
            item = QTableWidgetItem(str(deger))
            self.ui.table_calisan_bilgi.setItem(satir, sutun, item)



    # QLineEdit alanlarını temizle
      self.ui.calisan_maasi.clear()
      self.ui.lineEdit_13.clear()





 
    def tabloyuYenile_2(self):    
      self.ui.marka_secim.clear() 
      self.kayit.ui.marka_secim.clear()
    # Tüm verileri yeniden al
      self.cursor.execute("SELECT * FROM marka_bilgi")
   
      veriler_2 = self.cursor.fetchall()
     

    # Tabloya verileri aktar
      self.ui.table_marka_bilgi.setRowCount(len(veriler_2))
      self.ui.table_marka_bilgi.setColumnCount(4)

      
      for row in veriler_2:
            self.ui.marka_secim.addItem(row[0])
            self.kayit.ui.marka_secim.addItem(row[0])

      for satir, veri in enumerate(veriler_2):
         for sutun, deger in enumerate(veri):
            item = QTableWidgetItem(str(deger))
            self.ui.table_marka_bilgi.setItem(satir, sutun, item)



    # QLineEdit alanlarını temizle
      self.ui.lineEdit_3.clear()
      self.ui.lineEdit_4.clear()
      self.ui.lineEdit_5.clear()
      self.ui.lineEdit_6.clear()

    def tabloyuYenile_3(self):  
      self.ui.makine_secim.clear() 
      self.ui.makine_secim_2.clear() 
      self.ui.makine_secim_3.clear() 
      self.ui.makine_secim_4.clear()
      self.ui.makine_secim_5.clear()
      self.ui.makine_secim_6.clear()
      self.ui.makine_secim_7.clear()
      self.ui.makine_secim_8.clear()

      self.kayit.ui.makine_secim.clear() 
      self.kayit.ui.makine_secim_2.clear() 
      self.kayit.ui.makine_secim_3.clear() 
      self.kayit.ui.makine_secim_9.clear()
      self.kayit.ui.makine_secim_5.clear()
      self.kayit.ui.makine_secim_6.clear()
      self.kayit.ui.makine_secim_7.clear()
      self.kayit.ui.makine_secim_8.clear()  
    # Tüm verileri yeniden al
      self.cursor.execute("SELECT * FROM makine_marka")
   
      veriler_3 = self.cursor.fetchall()
     

    # Tabloya verileri aktar
      self.ui.table_makine_bilgi.setRowCount(len(veriler_3))
      self.ui.table_makine_bilgi.setColumnCount(5)

      
      for row in veriler_3:
            self.ui.makine_secim.addItem(row[1])
            self.ui.makine_secim_2.addItem(row[1])
            self.ui.makine_secim_3.addItem(row[1])
            self.ui.makine_secim_4.addItem(row[1])
            self.ui.makine_secim_5.addItem(row[1])
            self.ui.makine_secim_6.addItem(row[1])
            self.ui.makine_secim_7.addItem(row[1])
            self.ui.makine_secim_8.addItem(row[1])

            self.kayit.ui.makine_secim.addItem(row[1])
            self.kayit.ui.makine_secim_2.addItem(row[1])
            self.kayit.ui.makine_secim_3.addItem(row[1])
            self.kayit.ui.makine_secim_9.addItem(row[1])
            self.kayit.ui.makine_secim_5.addItem(row[1])
            self.kayit.ui.makine_secim_6.addItem(row[1])
            self.kayit.ui.makine_secim_7.addItem(row[1])
            self.kayit.ui.makine_secim_8.addItem(row[1])
            

      for satir, veri in enumerate(veriler_3):
         for sutun, deger in enumerate(veri):
            item = QTableWidgetItem(str(deger))
            self.ui.table_makine_bilgi.setItem(satir, sutun, item)

      self.ui.lineEdit_7.clear()
      self.ui.lineEdit_8.clear()
      self.ui.lineEdit_9.clear()
      self.ui.lineEdit_10.clear()


    def tabloyuYenile_4(self):    

    # Tüm verileri yeniden al
      self.cursor.execute("SELECT * FROM kw_bilgi")
   
      veriler_4 = self.cursor.fetchall()
     

    # Tabloya verileri aktar
      self.ui.table_kw_bilgi.setRowCount(len(veriler_4))
      self.ui.table_kw_bilgi.setColumnCount(3)

      


      for satir, veri in enumerate(veriler_4):
         for sutun, deger in enumerate(veri):
            item = QTableWidgetItem(str(deger))
            self.ui.table_kw_bilgi.setItem(satir, sutun, item)



    # QLineEdit alanlarını temizle
      self.ui.lineEdit_12.clear()
      self.ui.lineEdit_11.clear()



    def guncelleme_sayfasi(self, row, column):
       
       
       selected_rows = self.ui.table_marka_bilgi.selectionModel().selectedRows()
       if len(selected_rows) > 0:
            row = selected_rows[0].row()
            data1 = self.ui.table_marka_bilgi.item(row, 0).text()
            data2 = self.ui.table_marka_bilgi.item(row, 1).text()
            data3 = self.ui.table_marka_bilgi.item(row, 2).text()
            
            data4 = self.ui.table_marka_bilgi.item(row, 3).text()

            self.ui.lineEdit_3.setText(f"{data4}")
            self.ui.lineEdit_4.setText(f"{data1}")
            self.ui.lineEdit_5.setText(f"{data2}")
            self.ui.lineEdit_6.setText(f"{data3}")
       else:
            self.ui.lineEdit_4.setText("")
            self.ui.lineEdit_5.setText("")
            self.ui.lineEdit_6.setText("")

    def guncelleme_sayfasi_2(self, row):
       
       


       selected_rows_2 = self.ui.table_makine_bilgi.selectionModel().selectedRows()
       if len(selected_rows_2) > 0:
            row = selected_rows_2[0].row()
            data1_2 = self.ui.table_makine_bilgi.item(row, 0).text()
            data2_2 = self.ui.table_makine_bilgi.item(row, 1).text()
            data3_2 = self.ui.table_makine_bilgi.item(row, 2).text()
            
            data4_2 = self.ui.table_makine_bilgi.item(row, 3).text()
            data5_2 = self.ui.table_makine_bilgi.item(row, 4).text()

            self.ui.lineEdit_7.setText(f"{data5_2}")
            
            if data1_2 in [self.ui.makine_kodu_2.itemText(i) for i in range(self.ui.makine_kodu_2.count())]:
                 index = self.ui.makine_kodu_2.findText(data1_2)
                 self.ui.makine_kodu_2.setCurrentIndex(index)
            self.ui.lineEdit_8.setText(f"{data2_2}")
            self.ui.lineEdit_9.setText(f"{data3_2}")
            self.ui.lineEdit_10.setText(f"{data4_2}")
       else:
            self.ui.lineEdit_7.setText("")
            self.ui.lineEdit_8.setText("")
            self.ui.lineEdit_9.setText("")
            self.ui.lineEdit_10.setText("")

    def guncelleme_sayfasi_3(self, row, column):
       
       
       selected_rows = self.ui.table_calisan_bilgi.selectionModel().selectedRows()
       if len(selected_rows) > 0:
            row = selected_rows[0].row()
            data1_3 = self.ui.table_calisan_bilgi.item(row, 0).text()
            data3_3 = self.ui.table_calisan_bilgi.item(row, 2).text()
            data2_3 = self.ui.table_calisan_bilgi.item(row, 1).text()

            


            self.ui.lineEdit_13.setText(f"{data3_3}")

            self.ui.calisan_maasi.setText(f"{data2_3}")

       else:
            self.ui.calisan_maasi.setText("")


    def guncelleme_sayfasi_4(self, row, column):
       
       
       selected_rows = self.ui.table_kw_bilgi.selectionModel().selectedRows()
       if len(selected_rows) > 0:
            row = selected_rows[0].row()
            data1_3 = self.ui.table_kw_bilgi.item(row, 0).text()
            data3_3 = self.ui.table_kw_bilgi.item(row, 2).text()
            data2_3 = self.ui.table_kw_bilgi.item(row, 1).text()

            


            self.ui.lineEdit_11.setText(f"{data3_3}")

            self.ui.lineEdit_12.setText(f"{data2_3}")

       else:
            self.ui.lineEdit_12.setText("")


    def guncelle(self, tabloyuYenile):
       
       
       veri_kontrol = str()
       
       if self.ui.calisan_maasi.text() == "" or self.ui.calisan_maasi.text().replace('.', '', 1).isdigit() == False:
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         
         self.kayit.ui.label_2.setText("Çalışan maaşı kısmında hatalı veya boş giriş yapıldı")
         veri_kontrol = "1. veri girişi boş ya da hatalı"    
       else:
         calisan_adi = float(self.ui.calisan_maasi.text())

       if self.ui.lineEdit_13.text() == "":
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         
         self.kayit.ui.label_2.setText("Tablodan seçim yapmalısınız")
         veri_kontrol += "1. veri girişi boş ya da hatalı"    
       else:
         calisan_id = self.ui.lineEdit_13.text()

       if len(veri_kontrol) == 0:
         self.cursor.execute("UPDATE calisan_bilgi SET calisan_gunlugu = ? WHERE calisan_id = ?", (calisan_adi,  calisan_id))
         self.connection.commit()  
         self.tabloyuYenile()
         self.ui.calisan_maasi.clear()
         self.ui.lineEdit_13.clear()





    def guncelle_2(self, tabloyuYenile_2):
       
       veri_kontrol = str()
       
       if self.ui.lineEdit_3.text() == "":
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         
         self.kayit.ui.label_2.setText("Tablodan seçim yapmalısınız")
         veri_kontrol = "1. veri girişi boş ya da hatalı"    
       else:
         marka_kodu = self.ui.lineEdit_3.text()

       if self.ui.lineEdit_4.text() == "":
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         
         self.kayit.ui.label_2.setText("Marka adı kısmında hatalı veya boş giriş yapıldı")
         veri_kontrol += "1. veri girişi boş ya da hatalı"    
       else:
         marka_adi = self.ui.lineEdit_4.text()

       if self.ui.lineEdit_5.text() == "" or self.ui.lineEdit_5.text().replace('.', '', 1).isdigit() == False:
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         
         self.kayit.ui.label_2.setText("Marka fiyatı kısmında hatalı veya boş giriş yapıldı")
         veri_kontrol += "1. veri girişi boş ya da hatalı"    
       else:
         marka_fiyati = float(self.ui.lineEdit_5.text())       

       if self.ui.lineEdit_6.text() == "" or ui.lineEdit_6.text().replace('.', '', 1).isdigit() == False:
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         
         self.kayit.ui.label_2.setText("Marka kütle kısmında hatalı veya boş giriş yapıldı")
         veri_kontrol += "1. veri girişi boş ya da hatalı"    
       else:
         marka_kutle = float(self.ui.lineEdit_6.text())
   
       if len(veri_kontrol) == 0:
         self.cursor.execute("UPDATE marka_bilgi SET  marka_adi = ?, marka_fiyat = ?, marka_kutle = ? WHERE marka_id = ?", (marka_adi, marka_fiyati, marka_kutle,  marka_kodu))
         self.connection.commit()
         self.tabloyuYenile_2()
         self.ui.lineEdit_3.clear()
         self.ui.lineEdit_4.clear()
         self.ui.lineEdit_5.clear()
         self.ui.lineEdit_6.clear()

       
       
    def guncelle_3(self, tabloyuYenile_3):

       veri_kontrol = str()
       
       if self.ui.lineEdit_7.text() == "":
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         
         self.kayit.ui.label_2.setText("Tablodan seçim yapmalısınız")
         veri_kontrol = "1. veri girişi boş ya da hatalı"    
       else:
         makine_kodu = self.ui.lineEdit_7.text()      

       if self.ui.lineEdit_8.text() == "":
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         
         self.kayit.ui.label_2.setText("Makine adı kısmında hatalı veya boş giriş yapıldı")
         veri_kontrol += "1. veri girişi boş ya da hatalı"    
       else:
         makine_adi = self.ui.lineEdit_8.text()
       
       if self.ui.lineEdit_9.text() == "" or self.ui.lineEdit_9.text().replace('.', '', 1).isdigit() == False:
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         
         self.kayit.ui.label_2.setText("Makine fiyatı kısmında hatalı veya boş giriş yapıldı")
         veri_kontrol += "1. veri girişi boş ya da hatalı"    
       else:
         makine_fiyati = float(self.ui.lineEdit_9.text()) 

       if self.ui.lineEdit_10.text() == "" or self.ui.lineEdit_10.text().replace('.', '', 1).isdigit() == False:
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         
         self.kayit.ui.label_2.setText("Makine kw kısmında hatalı veya boş giriş yapıldı")
         veri_kontrol += "1. veri girişi boş ya da hatalı"    
       else:
         makine_kw = float(self.ui.lineEdit_10.text()) 

       if len(veri_kontrol) == 0:

         uretim_turu = self.ui.makine_kodu_2.currentText()
       
         self.cursor.execute("UPDATE makine_marka SET uretim=?, makine_adi=?, makine_gunlugu=?, makine_kw=? WHERE makine_kodu=?", (uretim_turu, makine_adi, makine_fiyati,  makine_kw, makine_kodu))
         self.connection.commit()
         self.tabloyuYenile_3()

         self.ui.lineEdit_7.clear()   
         self.ui.lineEdit_8.clear()
         self.ui.lineEdit_9.clear()
         self.ui.lineEdit_10.clear()

    def guncelle_4(self, tabloyuYenile_4):
       
       veri_kontrol = str()
       
       if self.ui.lineEdit_11.text() == "":
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         
         self.kayit.ui.label_2.setText("Tablodan seçim yapmalısınız")
         veri_kontrol = "1. veri girişi boş ya da hatalı"    
       else:
         kw_id = self.ui.lineEdit_11.text()

       if self.ui.lineEdit_12.text() == ""or self.ui.lineEdit_12.text().replace('.', '', 1).isdigit() == False:
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         
         self.kayit.ui.label_2.setText("Kw bedeli kısmında hatalı veya boş giriş yapıldı")
         veri_kontrol += "1. veri girişi boş ya da hatalı"    
       else:
         kw_bedel = float(self.ui.lineEdit_12.text())
       
       if len(veri_kontrol) == 0:

         self.cursor.execute("UPDATE kw_bilgi SET kwh = ? WHERE kw_id = ?", (kw_bedel,  kw_id))
         self.connection.commit()  
         self.tabloyuYenile_4()
         self.ui.lineEdit_12.clear()
         self.ui.lineEdit_11.clear()



    def ham_hesap(self, index):
        number1 = 0
        number2 = 0
        number3 = 0
        number4 = 0
        number5 = 0
        number6 = 0
        number7 = 0
        number8 = 0
        number9 = 0
        number10 = 0
        number11 = 0
        number12 = 0
        number13 = 0
        number14 = 0
        kutle = 0
        saf_fiyat = 1

        global veri
        global veri_2
        global veri_3
        global operation
        global seçilen_marka
        global name
        global data_id
        global eklenen_tarih
        global vardiyaadeti
        global vardiyaadeti_2
        global vardiyaadeti_3
        global vardiyaadeti_4
        global vardiyaadeti_5
        global vardiyaadeti_6
        global vardiyaadeti_7
        global vardiyaadeti_8
        global karmarji
        global vadefarki
        global vadesuresi
        global son_kar
        global vadesuresi_2 


        seçilen_ürün = self.ui.marka_secim.currentText()

        
        
        self.cursor.execute("SELECT marka_kutle FROM marka_bilgi WHERE marka_adi=?", (seçilen_ürün,))
        result = self.cursor.fetchone()
        if result is not None:
          kutle = result[0]
        else:
            pass
        
        seçilen_marka = self.ui.marka_secim.currentText()
        self.cursor.execute("SELECT marka_fiyat FROM marka_bilgi WHERE marka_adi=?", (seçilen_marka,))
        result_10 = self.cursor.fetchone()
        if result_10 is not None:
          saf_fiyat = result_10[0]
        else:
            pass
        
        
        
        operation = self.ui.sekil.currentText()

        if operation == "Yuvarlak":
            dis_cap_str = self.ui.dis_cap.text()
            uzunluk_str = self.ui.uzunluk.text()
            veri = dis_cap_str
            veri_2 = uzunluk_str
            veri_3 = "veri_3"
            if dis_cap_str.replace('.', '', 1).isdigit():
                number1 = float(dis_cap_str)
                

            else:
                pass
            if uzunluk_str.replace('.', '', 1).isdigit():
                number2 = float(uzunluk_str)
            else:
                pass
            
            if number1 or number2 or kutle != 0:
               result = (((3.14 * number1 * number1 / 4) * number2) / 1000 ) * kutle

            else:
               result = 0
               
            
            
        
        elif operation == "Boru":
            dis_cap_3_str = self.ui.dis_cap_3.text()
            ic_cap_2_str = self.ui.ic_cap_2.text()
            uzunluk_3_str = self.ui.uzunluk_3.text()
            veri = dis_cap_3_str
            veri_2 = ic_cap_2_str
            veri_3 = uzunluk_3_str
            if dis_cap_3_str.replace('.', '', 1).isdigit():
                number3 = float(dis_cap_3_str)
            else:
               pass

            if uzunluk_3_str.replace('.', '', 1).isdigit():
                number4 = float(uzunluk_3_str)
            else:
                pass
            if ic_cap_2_str.replace('.', '', 1).isdigit():
                number5 = float(ic_cap_2_str)
            else:
                pass
            if number3 or number4 or number5 or kutle != 0:
               result = ((((3.14 * number3 * number3 / 2) * number4) / 1000 ) - (((3.14 * number5 * number5 / 2) * number4) / 1000 ) ) * kutle

            else:
               result = 0
            
            
        
        
        
        elif operation == "Kare":
            en_3_str = self.ui.en_3.text()
            uzunluk_4_str = self.ui.uzunluk_4.text()
            genislik_3_str = self.ui.genislik_3.text()
            veri = en_3_str
            veri_2 = genislik_3_str
            veri_3 = uzunluk_4_str
            if en_3_str.replace('.', '', 1).isdigit():
                number6 = float(en_3_str)
            else:
                pass
            if uzunluk_4_str.replace('.', '', 1).isdigit():
                number7 = float(uzunluk_4_str)
            else:
                pass
            if genislik_3_str.replace('.', '', 1).isdigit():
                number8 = float(genislik_3_str)
            else:
                pass
             
            
            if number6 or number7 or number8 or kutle != 0:
               result = ((number6 * number7 * number8) / 1000) * kutle

            else:
               result = 0
            
        elif operation == "Lama":
            en_4_str = self.ui.en_4.text()
            uzunluk_5_str = self.ui.uzunluk_5.text()
            genislik_4_str = self.ui.genislik_4.text()
            veri = en_4_str
            veri_2 = genislik_4_str
            veri_3 = uzunluk_5_str
            if en_4_str.replace('.', '', 1).isdigit():
                number9 = float(en_4_str)
            else:
                pass
            if uzunluk_5_str.replace('.', '', 1).isdigit():
                number10 = float(uzunluk_5_str)
            else:
                pass
            if genislik_4_str.replace('.', '', 1).isdigit():
                number11 = float(genislik_4_str)
            else:
                pass
            

            if number9 or number10 or number11 or kutle != 0:
               result = ((number9 * number10 * number11) / 1000) * kutle

            else:
               result = 0
            
            
        
        
        
        
        
        elif operation == "Altıgen":
            en_7_str = self.ui.en_7.text()
            uzunluk_10_str = self.ui.uzunluk_10.text()
            veri = en_7_str
            veri_2 = uzunluk_10_str
            veri_3 = "veri_3"
            if en_7_str.replace('.', '', 1).isdigit():
                number12 = float(en_7_str)
            else:
                pass
            if uzunluk_10_str.replace('.', '', 1).isdigit():
                number13 = float(uzunluk_10_str)
            else:
                pass
            
            

            if number12 or number13 or kutle != 0:
               result = ((((number12 * number12) * 0.866) * number13) / 1000) * kutle

            else:
               result = 0



            
        elif operation == "Ham":
            agirlik_6_str = self.ui.agirlik_6.text()
            veri = agirlik_6_str
            veri_2 = "veri_2"
            veri_3 = "veri_3"
            if agirlik_6_str.replace('.', '', 1).isdigit():
                number14 = float(agirlik_6_str)
            else:
                pass
            
            
            

            if number14 != 0:
               result = (number13 / 10) 

            else:
               result = 0
            
        xresult = round(result, 2)  
        self.ui.ham_madde_agirlik.setText(f"{xresult}")
            
        
        seçilen_makine = self.ui.makine_secim.currentText()
        seçilen_makine_2 = self.ui.makine_secim_2.currentText()
        seçilen_makine_3 = self.ui.makine_secim_3.currentText()
        seçilen_makine_4 = self.ui.makine_secim_4.currentText()
        seçilen_makine_5 = self.ui.makine_secim_5.currentText()
        seçilen_makine_6 = self.ui.makine_secim_6.currentText()
        seçilen_makine_7 = self.ui.makine_secim_7.currentText()
        seçilen_makine_8 = self.ui.makine_secim_8.currentText()
        
        seçilen_iscilik = self.ui.makine_secim.currentText()
        seçilen_iscilik_2 = self.ui.makine_secim_2.currentText()
        seçilen_iscilik_3 = self.ui.makine_secim_3.currentText()
        seçilen_iscilik_4 = self.ui.makine_secim_4.currentText()
        seçilen_iscilik_5 = self.ui.makine_secim_5.currentText()
        seçilen_iscilik_6 = self.ui.makine_secim_6.currentText()
        seçilen_iscilik_7 = self.ui.makine_secim_7.currentText()
        seçilen_iscilik_8 = self.ui.makine_secim_8.currentText()

        self.ui.makine_ismi.setText(f"{seçilen_makine}")
        self.ui.makine_ismi_2.setText(f"{seçilen_makine_2}")
        self.ui.makine_ismi_3.setText(f"{seçilen_makine_3}")
        self.ui.makine_ismi_4.setText(f"{seçilen_makine_4}")
        self.ui.makine_ismi_5.setText(f"{seçilen_makine_5}")
        self.ui.makine_ismi_6.setText(f"{seçilen_makine_6}")
        self.ui.makine_ismi_7.setText(f"{seçilen_makine_7}")
        self.ui.makine_ismi_8.setText(f"{seçilen_makine_8}")
        

        toplam_urun = 1

        vardiyaadeti = 0
        vardiyaadeti_2 = 0
        vardiyaadeti_3 = 0
        vardiyaadeti_4 = 0
        vardiyaadeti_5 = 0
        vardiyaadeti_6 = 0
        vardiyaadeti_7 = 0
        vardiyaadeti_8 = 0


        
        makine_gunluk = 1
        makine_gunluk_2 = 1
        makine_gunluk_3 = 1
        makine_gunluk_4 = 1
        makine_gunluk_5 = 1
        makine_gunluk_6 = 1
        makine_gunluk_7 = 1
        makine_gunluk_8 = 1

        iscilik_gunluk = 1
        iscilik_gunluk_2 = 1
        iscilik_gunluk_3 = 1
        iscilik_gunluk_4 = 1
        iscilik_gunluk_5 = 1
        iscilik_gunluk_6 = 1
        iscilik_gunluk_7 = 1
        iscilik_gunluk_8 = 1

        makine_gunluk__1 = 0
        makine_gunluk__2 = 0
        makine_gunluk__3 = 0
        makine_gunluk__4 = 0
        makine_gunluk__5 = 0
        makine_gunluk__6 = 0
        makine_gunluk__7 = 0
        makine_gunluk__8 = 0

        iscilik_gunluk__1 = 0
        iscilik_gunluk__2 = 0
        iscilik_gunluk__3 = 0
        iscilik_gunluk__4 = 0
        iscilik_gunluk__5 = 0
        iscilik_gunluk__6 = 0
        iscilik_gunluk__7 = 0
        iscilik_gunluk__8 = 0

        kw_gunluk__1 = 0
        kw_gunluk__2 = 0
        kw_gunluk__3 = 0
        kw_gunluk__4 = 0
        kw_gunluk__5 = 0
        kw_gunluk__6 = 0
        kw_gunluk__7 = 0
        kw_gunluk__8 = 0


        kw_gunluk = 0
        kw_gunluk_2 = 0
        kw_gunluk_3 = 0
        kw_gunluk_4 = 0
        kw_gunluk_5 = 0
        kw_gunluk_6 = 0
        kw_gunluk_7 = 0
        kw_gunluk_8 = 0

        gunluk__1 = 0
        gunluk__2 = 0
        gunluk__3 = 0
        gunluk__4 = 0
        gunluk__5 = 0
        gunluk__6 = 0
        gunluk__7 = 0
        gunluk__8 = 0

        karmarji = 1
        kdv = 1
        vadefarki = 1
        vadesuresi = 1
        vadesuresi_2 = 0
        cikantalas = 0
        talasfiyat = 0
        son_kar = 1
        son_kar_marjix = 1

        
        
        
        self.ui.madde_ozkutle.setText(f"{kutle}")
        self.ui.m.setText(f"{saf_fiyat}")
        
        
           

           

          

          

          


        cikan_talas_str = self.ui.cikan_talas.text()
        if cikan_talas_str.replace('.', '', 1).isdigit():
           cikantalas = float(cikan_talas_str)
        else:
            pass
        
        talas_fiyat_str = self.ui.talas_fiyat.text()
        if talas_fiyat_str.replace('.', '', 1).isdigit():
           talasfiyat = float(talas_fiyat_str)
        else:
            pass
        
        if cikantalas != 0:
           if talasfiyat != 0:
              talas_tutar = ((xresult - cikantalas) / 1000) * talasfiyat
           else:
              talas_tutar = 0
        else:
           talas_tutar = 0
              
              
        

        self.ui.talas_tutari.setText(f"{talas_tutar}")
        
        cursor.execute("SELECT calisan_gunlugu FROM calisan_bilgi ORDER BY calisan_gunlugu DESC LIMIT 1")
        son_sayi_2 = cursor.fetchone()

         # Son sayıyı almak
        if son_sayi_2 is not None:
         son_sayi = son_sayi_2[0]
         calisan_fiyati = son_sayi / 7
          
        else:
          calisan_fiyati = 0 

        cursor.execute("SELECT kwh FROM kw_bilgi ORDER BY kwh DESC LIMIT 1")
        son_sayi_3 = cursor.fetchone()

         # Son sayıyı almak
        if son_sayi_3 is not None:
         son_sayi_2 = son_sayi_3[0]
         kw_fiyati = son_sayi_2 * 12
          
        else:
          kw_fiyati = 0 


        vardiya_adeti_str = self.ui.vardiya_adeti.text()
        if vardiya_adeti_str.replace('.', '', 1).isdigit():
           vardiyaadeti = float(vardiya_adeti_str)
        else:
            pass
        
        vardiya_adeti_2_str = self.ui.vardiya_adeti_2.text()
        if vardiya_adeti_2_str.replace('.', '', 1).isdigit():
           vardiyaadeti_2 = float(vardiya_adeti_2_str)
        else:
            pass
        
        vardiya_adeti_3_str = self.ui.vardiya_adeti_3.text()
        if vardiya_adeti_3_str.replace('.', '', 1).isdigit():
           vardiyaadeti_3 = float(vardiya_adeti_3_str)
        else:
            pass
        
        vardiya_adeti_4_str = self.ui.vardiya_adeti_4.text()
        if vardiya_adeti_4_str.replace('.', '', 1).isdigit():
           vardiyaadeti_4 = float(vardiya_adeti_4_str)
        else:
            pass

        vardiya_adeti_5_str = self.ui.vardiya_adeti_5.text()
        if vardiya_adeti_5_str.replace('.', '', 1).isdigit():
           vardiyaadeti_5 = float(vardiya_adeti_5_str)
        else:
            pass

        vardiya_adeti_6_str = self.ui.vardiya_adeti_6.text()
        if vardiya_adeti_6_str.replace('.', '', 1).isdigit():
           vardiyaadeti_6 = float(vardiya_adeti_6_str)
        else:
            pass

        vardiya_adeti_7_str = self.ui.vardiya_adeti_7.text()
        if vardiya_adeti_7_str.replace('.', '', 1).isdigit():
           vardiyaadeti_7 = float(vardiya_adeti_7_str)
        else:
            pass

        vardiya_adeti_8_str = self.ui.vardiya_adeti_8.text()
        if vardiya_adeti_8_str.replace('.', '', 1).isdigit():
           vardiyaadeti_8 = float(vardiya_adeti_8_str)
        else:
            pass
        
        toplam_urun_str = self.ui.toplam_urun.text()
        if toplam_urun_str.replace('.', '', 1).isdigit():
           toplam_urun = float(toplam_urun_str)
        else:
            pass
        
        self.cursor.execute("SELECT uretim FROM makine_marka WHERE makine_adi=?", (seçilen_makine,))
        atama = self.cursor.fetchone()
        if atama and atama[0] != "Kendi":
           self.ui.label_42.setText("Tane fiyatı:")
           
           if vardiyaadeti != 0:
             makine_gunluk__1 = vardiyaadeti
             iscilik_gunluk__1 = 0
             kw_gunluk__1 = 0
             gunluk__1 = 0

           else:
               makine_gunluk__1 = 0
               iscilik_gunluk__1 = 0
               kw_gunluk__1 = 0
               gunluk__1 = 0
           
           
           
           
        else:   
           self.cursor.execute("SELECT makine_gunlugu, makine_kw FROM makine_marka WHERE makine_adi=?", (seçilen_makine,))
           result_2 = self.cursor.fetchone()
           self.ui.label_42.setText("Vardiye adeti:")
           if result_2 is not None:
              makine_gunluk = result_2[0]
              kw_gunluk = result_2[1]
           else:
             pass 
           
           if vardiyaadeti != 0:
            makine_gunluk__1 = makine_gunluk / vardiyaadeti
            iscilik_gunluk__1 = calisan_fiyati / vardiyaadeti
            kw_gunluk__1 = (kw_gunluk * kw_fiyati) / vardiyaadeti
            gunluk__1 = toplam_urun / vardiyaadeti

           else:
            makine_gunluk__1 = 0
            iscilik_gunluk__1 = 0
            kw_gunluk__1 = 0
            gunluk__1 = 0

        
         
        self.cursor.execute("SELECT uretim FROM makine_marka WHERE makine_adi=?", (seçilen_makine_2,))
        atama_2 = self.cursor.fetchone()
        if atama_2 and atama_2[0] != "Kendi":
           self.ui.label_43.setText("Tane fiyatı:")
           
           if vardiyaadeti_2 != 0:
            makine_gunluk__2 = vardiyaadeti_2
            iscilik_gunluk__2 = 0
            kw_gunluk__2 = 0
            gunluk__2 = 0

           else:
            makine_gunluk__2 = 0
            iscilik_gunluk__2 = 0
            kw_gunluk__2 = 0
            gunluk__2 = 0
           
           
           
           
        else:   
           self.ui.label_43.setText("Vardiye adeti:")
           self.cursor.execute("SELECT makine_gunlugu, makine_kw FROM makine_marka WHERE makine_adi=?", (seçilen_makine_2,))
           result_3 = self.cursor.fetchone()
           if result_3 is not None:
            makine_gunluk_2 = result_3[0]
            kw_gunluk_2 = result_3[1]
           else:
            pass 
           
           if vardiyaadeti_2 != 0:
             makine_gunluk__2 = makine_gunluk_2 / vardiyaadeti_2
             iscilik_gunluk__2 = calisan_fiyati / vardiyaadeti_2
             kw_gunluk__2 = (kw_gunluk_2 * kw_fiyati) / vardiyaadeti_2
             gunluk__2 = toplam_urun / vardiyaadeti_2

           else:
               makine_gunluk__2 = 0
               iscilik_gunluk__2 = 0
               kw_gunluk__2 = 0
               gunluk__2 = 0

        self.cursor.execute("SELECT uretim FROM makine_marka WHERE makine_adi=?", (seçilen_makine_3,))
        atama_3 = self.cursor.fetchone()
        if atama_3 and atama_3[0] != "Kendi":
           self.ui.label_44.setText("Tane fiyatı:")
           
           if vardiyaadeti_3 != 0:
            makine_gunluk__3 = vardiyaadeti_3
            iscilik_gunluk__3 = 0
            kw_gunluk__3 = 0
            gunluk__3 = 0

           else:
            makine_gunluk__3 = 0
            iscilik_gunluk__3 = 0
            kw_gunluk__3 = 0
            gunluk__3 = 0
           
           
           
           
        else:   
           self.ui.label_44.setText("Vardiye adeti:")
           self.cursor.execute("SELECT makine_gunlugu, makine_kw FROM makine_marka WHERE makine_adi=?", (seçilen_makine_3,))
           result_4 = self.cursor.fetchone()
           if result_4 is not None:
            makine_gunluk_3 = result_4[0]
            kw_gunluk_3 = result_4[1]
           else:
            pass 
           
           if vardiyaadeti_3 != 0:
            makine_gunluk__3 = makine_gunluk_3 / vardiyaadeti_3
            iscilik_gunluk__3 = calisan_fiyati / vardiyaadeti_3
            kw_gunluk__3 = (kw_gunluk_3 * kw_fiyati) / vardiyaadeti_3
            gunluk__3 = toplam_urun / vardiyaadeti_3

           else:
            makine_gunluk__3 = 0
            iscilik_gunluk__3 = 0
            kw_gunluk__3 = 0
            gunluk__3 = 0
        

        self.cursor.execute("SELECT uretim FROM makine_marka WHERE makine_adi=?", (seçilen_makine_4,))
        atama_4 = self.cursor.fetchone()
        if atama_4 and atama_4[0] != "Kendi":
           self.ui.label_45.setText("Tane fiyatı:")
           
           if vardiyaadeti_4 != 0:
            makine_gunluk__4 = vardiyaadeti_4
            iscilik_gunluk__4 = 0
            kw_gunluk__4 = 0
            gunluk__4 = 0

           else:
            makine_gunluk__4 = 0
            iscilik_gunluk__4 = 0
            kw_gunluk__4 = 0
            gunluk__4 = 0
           
           
           
           
        else:   
           self.ui.label_45.setText("Vardiye adeti:")
           self.cursor.execute("SELECT makine_gunlugu, makine_kw FROM makine_marka WHERE makine_adi=?", (seçilen_makine_4,))
           result_5 = self.cursor.fetchone()
           if result_5 is not None:
            makine_gunluk_4 = result_5[0]
            kw_gunluk_4 = result_5[1]
           else:
            pass 
           
           if vardiyaadeti_4 != 0:
            makine_gunluk__4 = makine_gunluk / vardiyaadeti_4
            iscilik_gunluk__4 = calisan_fiyati / vardiyaadeti_4
            kw_gunluk__4 = (kw_gunluk_4 * kw_fiyati) / vardiyaadeti_4
            gunluk__4 = toplam_urun / vardiyaadeti_4

           else:
            makine_gunluk__4 = 0
            iscilik_gunluk__4 = 0
            kw_gunluk__4 = 0
            gunluk__4 = 0

        self.cursor.execute("SELECT uretim FROM makine_marka WHERE makine_adi=?", (seçilen_makine_5,))
        atama_5 = self.cursor.fetchone()
        if atama_5 and atama_5[0] != "Kendi":
           self.ui.label_149.setText("Tane fiyatı:")
           
           if vardiyaadeti_5 != 0:
            makine_gunluk__5 = vardiyaadeti_5
            iscilik_gunluk__5 = 0
            kw_gunluk__5 = 0
            gunluk__5 = 0

           else:
            makine_gunluk__5 = 0
            iscilik_gunluk__5 = 0
            kw_gunluk__5 = 0
            gunluk__5 = 0
           
           
           
           
        else:   
           self.ui.label_149.setText("Vardiye adeti:")
           self.cursor.execute("SELECT makine_gunlugu, makine_kw FROM makine_marka WHERE makine_adi=?", (seçilen_makine_5,))
           result_11 = self.cursor.fetchone()
           if result_11 is not None:
            makine_gunluk_5 = result_11[0]
            kw_gunluk_5 = result_11[1]
           else:
            pass 
           
           if vardiyaadeti_5 != 0:
            makine_gunluk__5 = makine_gunluk_5 / vardiyaadeti_5
            iscilik_gunluk__5 = calisan_fiyati / vardiyaadeti_5
            kw_gunluk__5 = (kw_gunluk_5 * kw_fiyati) / vardiyaadeti_5
            gunluk__5 = toplam_urun / vardiyaadeti_5

           else:
            makine_gunluk__5 = 0
            iscilik_gunluk__5 = 0
            kw_gunluk__5 = 0
            gunluk__5 = 0

        self.cursor.execute("SELECT uretim FROM makine_marka WHERE makine_adi=?", (seçilen_makine_6,))
        atama_6 = self.cursor.fetchone()
        if atama_6 and atama_6[0] != "Kendi":
           self.ui.label_147.setText("Tane fiyatı:")
           
           if vardiyaadeti_6 != 0:
            makine_gunluk__6 = vardiyaadeti_6
            iscilik_gunluk__6 = 0
            kw_gunluk__6 = 0
            gunluk__6 = 0

           else:
            makine_gunluk__6 = 0
            iscilik_gunluk__6 = 0
            kw_gunluk__6 = 0
            gunluk__6 = 0
           
           
           
           
        else:   
           self.ui.label_147.setText("Vardiye adeti:")
           self.cursor.execute("SELECT makine_gunlugu, makine_kw FROM makine_marka WHERE makine_adi=?", (seçilen_makine_6,))
           result_12 = self.cursor.fetchone()
           if result_12 is not None:
            makine_gunluk_6 = result_12[0]
            kw_gunluk_6 = result_12[1]
           else:
            pass
           
           if vardiyaadeti_6 != 0:
            makine_gunluk__6 = makine_gunluk_6 / vardiyaadeti_6
            iscilik_gunluk__6 = calisan_fiyati / vardiyaadeti_6
            kw_gunluk__6 = (kw_gunluk_6 * kw_fiyati) / vardiyaadeti_6
            gunluk__6 = toplam_urun / vardiyaadeti_6

           else:
            makine_gunluk__6 = 0
            iscilik_gunluk__6 = 0
            kw_gunluk__6 = 0
            gunluk__6 = 0

        self.cursor.execute("SELECT uretim FROM makine_marka WHERE makine_adi=?", (seçilen_makine_7,))
        atama_7 = self.cursor.fetchone()
        if atama_7 and atama_7[0] != "Kendi":
           self.ui.label_150.setText("Tane fiyatı:")
           
           if vardiyaadeti_7 != 0:
            makine_gunluk__7 = vardiyaadeti_7
            iscilik_gunluk__7 = 0
            kw_gunluk__7 = 0
            gunluk__7 = 0

           else:
            makine_gunluk__7 = 0
            iscilik_gunluk__7 = 0
            kw_gunluk__7 = 0
            gunluk__7 = 0
           
           
           
           
        else:   
           self.ui.label_150.setText("Vardiye adeti:")
           self.cursor.execute("SELECT makine_gunlugu, makine_kw FROM makine_marka WHERE makine_adi=?", (seçilen_makine_7,))
           result_13 = self.cursor.fetchone()
           if result_13 is not None:
            makine_gunluk_7 = result_13[0]
            kw_gunluk_7 = result_13[1]
           else:
            pass
           
           if vardiyaadeti_7 != 0:
            makine_gunluk__7 = makine_gunluk_7 / vardiyaadeti_7
            iscilik_gunluk__7 = calisan_fiyati / vardiyaadeti_7
            kw_gunluk__7 = (kw_gunluk_7 * kw_fiyati) / vardiyaadeti_7
            gunluk__7 = toplam_urun / vardiyaadeti_7

           else:
            makine_gunluk__7 = 0
            iscilik_gunluk__7 = 0
            kw_gunluk__7 = 0
            gunluk__7 = 0

        self.cursor.execute("SELECT uretim FROM makine_marka WHERE makine_adi=?", (seçilen_makine_8,))
        atama_8 = self.cursor.fetchone()
        if atama_8 and atama_8[0] != "Kendi":
           self.ui.label_153.setText("Tane fiyatı:")
           
           if vardiyaadeti_8 != 0:
            makine_gunluk__8 = vardiyaadeti_8
            iscilik_gunluk__8 = 0
            kw_gunluk__8 = 0
            gunluk__8 = 0

           else:
            makine_gunluk__8 = 0
            iscilik_gunluk__8 = 0
            kw_gunluk__8 = 0
            gunluk__8 = 0
           
           
           
           
        else:   
           self.ui.label_153.setText("Vardiye adeti:")
           self.cursor.execute("SELECT makine_gunlugu, makine_kw FROM makine_marka WHERE makine_adi=?", (seçilen_makine_8,))
           result_14 = self.cursor.fetchone()
           if result_14 is not None:
             makine_gunluk_8 = result_14[0]
             kw_gunluk_8 = result_14[1]
           else:
             pass
           
           if vardiyaadeti_8 != 0:
            makine_gunluk__8 = makine_gunluk_8 / vardiyaadeti_8
            iscilik_gunluk__8 = calisan_fiyati / vardiyaadeti_8
            kw_gunluk__8 = (kw_gunluk_8 * kw_fiyati) / vardiyaadeti_8
            gunluk__8 = toplam_urun / vardiyaadeti_8

           else:
            makine_gunluk__8 = 0
            iscilik_gunluk__8 = 0
            kw_gunluk__8 = 0
            gunluk__8 = 0

        

           
           

        
        

        self.ui.makine_tutari.setText(f"{round(makine_gunluk__1, 2)}")
        self.ui.makine_tutari_2.setText(f"{round(makine_gunluk__2, 2)}")
        self.ui.makine_tutari_3.setText(f"{round(makine_gunluk__3, 2)}")
        self.ui.makine_tutari_4.setText(f"{round(makine_gunluk__4, 2)}")
        self.ui.makine_tutari_5.setText(f"{round(makine_gunluk__5, 2)}")
        self.ui.makine_tutari_6.setText(f"{round(makine_gunluk__6, 2)}")
        self.ui.makine_tutari_7.setText(f"{round(makine_gunluk__7, 2)}")
        self.ui.makine_tutari_8.setText(f"{round(makine_gunluk__8, 2)}")

        
        

        self.ui.calisan_tutari.setText(f"{round(iscilik_gunluk__1, 2)}")
        self.ui.calisan_tutari_2.setText(f"{round(iscilik_gunluk__2, 2)}")
        self.ui.calisan_tutari_3.setText(f"{round(iscilik_gunluk__3, 2)}")
        self.ui.calisan_tutari_4.setText(f"{round(iscilik_gunluk__4, 2)}")
        self.ui.calisan_tutari_5.setText(f"{round(iscilik_gunluk__5, 2)}")
        self.ui.calisan_tutari_6.setText(f"{round(iscilik_gunluk__6, 2)}")
        self.ui.calisan_tutari_7.setText(f"{round(iscilik_gunluk__7, 2)}")
        self.ui.calisan_tutari_8.setText(f"{round(iscilik_gunluk__8, 2)}")

        self.ui.elektrik_tutari.setText(f"{round(kw_gunluk__1, 2)}")
        self.ui.elektrik_tutari_2.setText(f"{round(kw_gunluk__2, 2)}")
        self.ui.elektrik_tutari_3.setText(f"{round(kw_gunluk__3, 2)}")
        self.ui.elektrik_tutari_4.setText(f"{round(kw_gunluk__4, 2)}")
        self.ui.elektrik_tutari_5.setText(f"{round(kw_gunluk__5, 2)}")
        self.ui.elektrik_tutari_6.setText(f"{round(kw_gunluk__6, 2)}")
        self.ui.elektrik_tutari_7.setText(f"{round(kw_gunluk__7, 2)}")
        self.ui.elektrik_tutari_8.setText(f"{round(kw_gunluk__8, 2)}")
        

        
        toplam_makine_tutarix = makine_gunluk__1 + makine_gunluk__2 + makine_gunluk__3 + makine_gunluk__4 + makine_gunluk__5 + makine_gunluk__6 + makine_gunluk__7 + makine_gunluk__8  
        
        toplam_makine_tutari = round(toplam_makine_tutarix, 2)

        self.ui.toplam_makine.setText(f"{toplam_makine_tutari}")



        toplam_iscilik_tutarix = iscilik_gunluk__1 + iscilik_gunluk__2 + iscilik_gunluk__3 + iscilik_gunluk__4 + iscilik_gunluk__5 + iscilik_gunluk__6 + iscilik_gunluk__7 + iscilik_gunluk__8  
        
        toplam_iscilik_tutari = round(toplam_iscilik_tutarix, 2)

        self.ui.toplam_iscilik.setText(f"{toplam_iscilik_tutari}")
        

        toplam_kw_tutarix = kw_gunluk__1 + kw_gunluk__2 + kw_gunluk__3 + kw_gunluk__4 + kw_gunluk__5 + kw_gunluk__6 + kw_gunluk__7 + kw_gunluk__8  
        
        toplam_kw_tutari = round(toplam_kw_tutarix, 2)

        self.ui.toplam_elektrik.setText(f"{toplam_kw_tutari}")


        toplam__urun =  gunluk__1 + gunluk__2 + gunluk__3 + gunluk__4 + gunluk__5 + gunluk__6 + gunluk__7 + gunluk__8  

        self.ui.talas_tutari_3.setText(f"{toplam__urun}") 

        kg_ham_madde = xresult / 1000
        ham_birim_fiyat = kg_ham_madde * saf_fiyat
        ham_gunluk_tutar = ham_birim_fiyat * vardiyaadeti


        self.ui.ham_birim_fiyat.setText(f"{round(ham_birim_fiyat, 2)}")

        maliyet = float(ham_birim_fiyat + toplam_makine_tutari + toplam_iscilik_tutari + toplam_kw_tutari) 



        self.ui.maliyet.setText(f"{round(maliyet, 2)}")

        

        kar_marji_str = self.ui.kar_marji.text()
        if kar_marji_str.replace('.', '', 1).isdigit():
           karmarji = float(kar_marji_str)
        else:
            pass
        
       
        
        vade_farki_str = self.ui.vade_farki.text()
        if vade_farki_str.replace('.', '', 1).isdigit():
           vadefarki = float(vade_farki_str)
        else:
            pass
        
        vade_suresi_str = self.ui.vade_suresi.text()
        if vade_suresi_str.replace('.', '', 1).isdigit():
           vadesuresi = float(vade_suresi_str)
        else:
            pass
        

        vade_farki_2_str = self.ui.vade_farki_2.text()
        if vade_farki_2_str.replace('.', '', 1).isdigit():
           son_kar = float(vade_farki_2_str)
        else:
            pass

        vade_suresi_2_str = self.ui.vade_suresi_2.text()
        if vade_suresi_2_str.replace('.', '', 1).isdigit():
           vadesuresi_2 = float(vade_suresi_2_str)
        else:
            pass
        
        
        if karmarji != 0:
           pesinx = (maliyet * karmarji / 100) + maliyet

        else:
           pesinx = maliyet
           
        
        pesin = round(pesinx, 2)

        

        


    
        self.ui.pesin.setText(f"{pesin}")

        vadeli_fiyatx = pesin * (1 + ((vadesuresi / 30 * vadefarki) / 100))

        vadeli_fiyat = round(vadeli_fiyatx, 2)

        self.ui.vadeli_fiyat.setText(f"{vadeli_fiyat}")

        if vadesuresi_2 != 0:
           if son_kar != 0:
              ara_islem = son_kar / ( 1 + (((vadesuresi_2 / 30) * vadefarki) / 100))
           else:
              ara_islem = 0
              
        else:
           if son_kar != 0:
              ara_islem = son_kar / 1

           else:
              ara_islem = 0
           
           


        if maliyet != 0:
           if ara_islem != 0:
              son_kar_marjix = (((ara_islem / maliyet) - 1) * 100)

           else:
              son_kar_marjix = 0
              
        else:
          son_kar_marjix = 0
           
        


        son_kar_marji = round(son_kar_marjix, 2)
        data_id = self.ui.label.text()
        self.ui.vadeli_fiyat_2.setText(f"{son_kar_marji}")
        eklenen_tarih = self.ui.dateEdit.dateTime().toString()
        
        
    def data_1_save(self):

        name = self.kayit.ui.save_name.text()

        seçilen_makine = self.ui.makine_secim.currentText()
        seçilen_makine_2 = self.ui.makine_secim_2.currentText()
        seçilen_makine_3 = self.ui.makine_secim_3.currentText()
        seçilen_makine_4 = self.ui.makine_secim_4.currentText()
        seçilen_makine_5 = self.ui.makine_secim_5.currentText()
        seçilen_makine_6 = self.ui.makine_secim_6.currentText()
        seçilen_makine_7 = self.ui.makine_secim_7.currentText()
        seçilen_makine_8 = self.ui.makine_secim_8.currentText()

        err_txt = str()
        
        if  veri == "" or veri.replace('.', '', 1).isdigit() == False:
           err_txt = "1. veri girişi boş ya da hatalı"
      
        if veri_2 == "veri_2":
           pass
        elif veri_2 == "" or veri_2.replace('.', '', 1).isdigit() == False:
           err_txt += " 2. veri girişi boş ya da hatalı"

        if veri_3 == "veri_3":
           pass
        elif veri_3 == "" or veri_3.replace('.', '', 1).isdigit() == False:
           err_txt += " 3. veri girişi boş ya da hatalı"
        
        if len(err_txt) == 0:
           self.cursor.execute("INSERT INTO data_1 VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (eklenen_tarih, data_id, name, seçilen_marka, operation, veri, veri_2, veri_3))
           self.cursor.execute("INSERT INTO data_2 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (data_id, seçilen_makine, seçilen_makine_2, seçilen_makine_3, seçilen_makine_4, seçilen_makine_5, seçilen_makine_6, seçilen_makine_7, seçilen_makine_8))
           self.cursor.execute("INSERT INTO data_3 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (data_id, vardiyaadeti, vardiyaadeti_2, vardiyaadeti_3, vardiyaadeti_4, vardiyaadeti_5, vardiyaadeti_6, vardiyaadeti_7, vardiyaadeti_8))
           self.cursor.execute("INSERT INTO data_4 VALUES (?, ?, ?, ?, ?, ?)", (data_id, karmarji, vadefarki, vadesuresi, son_kar, vadesuresi_2))

           self.connection.commit()
           self.kayit.ui.save_name.clear()
           self.kayit.hide()
           self.kayit_id()

    def data_refresh(self):    

    # Tüm verileri yeniden al
      self.cursor.execute("SELECT * FROM data_1")
   
      veriler = self.cursor.fetchall()
     

    ## Tabloya verileri aktar ##
      self.ui.data_bilgi.setRowCount(len(veriler))
      self.ui.data_bilgi.setColumnCount(8)

      


      for satir, veri in enumerate(veriler):
         for sutun, deger in enumerate(veri):
            item = QTableWidgetItem(str(deger))
            self.ui.data_bilgi.setItem(satir, sutun, item)



    # QLineEdit alanlarını temizle
      self.ui.calisan_maasi.clear()
      self.ui.lineEdit_13.clear()

    def data_update(self, row):
       
       
       selected_rows = self.ui.data_bilgi.selectionModel().selectedRows()
       if len(selected_rows) > 0:
            row = selected_rows[0].row()
            data1 = self.ui.data_bilgi.item(row, 1).text()



            self.ui.label_25.setText(f"{data1}")

       else:
            self.ui.label_25.setText("")


    def data_delete(self):
       data_id = self.ui.label_25.text()
       err_txt = str()
       if data_id == "":
          self.kayit.show()
          self.kayit.ui.stackedWidget.setCurrentIndex(1)
          self.kayit.ui.label_2.setText("Tablodan seçim yapınız")          
       else:
          self.cursor.execute("DELETE FROM data_1 WHERE data_id = ?", (data_id,))
          self.cursor.execute("DELETE FROM data_2 WHERE data_id = ?", (data_id,))
          self.cursor.execute("DELETE FROM data_3 WHERE data_id = ?", (data_id,))
          self.cursor.execute("DELETE FROM data_4 WHERE data_id = ?", (data_id,))          
          
          self.connection.commit()
          self.data_refresh()   

    def data_close(self):
          if self.kilitle == False:
              self.kilitle = False
          else:
              self.kilitle = False
          self.ui.frame_207.show()
          self.ui.stackedWidget.setCurrentIndex(5)
          self.ui.stackedWidget_12.setCurrentIndex(0)       

          self.ui.sekil.setDisabled(self.kilitle)

          self.ui.marka_secim.setDisabled(self.kilitle)

          self.ui.dis_cap.setReadOnly(self.kilitle)
          self.ui.uzunluk.setReadOnly(self.kilitle)
          self.ui.dis_cap_3.setReadOnly(self.kilitle)
          self.ui.uzunluk_3.setReadOnly(self.kilitle)
          self.ui.ic_cap_2.setReadOnly(self.kilitle)
          self.ui.en_3.setReadOnly(self.kilitle)
          self.ui.genislik_3.setReadOnly(self.kilitle)
          self.ui.uzunluk_4.setReadOnly(self.kilitle)
          self.ui.en_4.setReadOnly(self.kilitle)
          self.ui.genislik_4.setReadOnly(self.kilitle)
          self.ui.uzunluk_5.setReadOnly(self.kilitle)
          self.ui.en_7.setReadOnly(self.kilitle)
          self.ui.uzunluk_10.setReadOnly(self.kilitle)


          self.ui.makine_secim.setDisabled(self.kilitle)
          self.ui.makine_secim_2.setDisabled(self.kilitle)
          self.ui.makine_secim_3.setDisabled(self.kilitle)
          self.ui.makine_secim_4.setDisabled(self.kilitle)
          self.ui.makine_secim_5.setDisabled(self.kilitle)
          self.ui.makine_secim_6.setDisabled(self.kilitle)
          self.ui.makine_secim_7.setDisabled(self.kilitle)
          self.ui.makine_secim_8.setDisabled(self.kilitle)


          self.ui.vardiya_adeti.setReadOnly(self.kilitle)
          self.ui.vardiya_adeti_2.setReadOnly(self.kilitle)
          self.ui.vardiya_adeti_3.setReadOnly(self.kilitle)
          self.ui.vardiya_adeti_4.setReadOnly(self.kilitle)
          self.ui.vardiya_adeti_5.setReadOnly(self.kilitle)
          self.ui.vardiya_adeti_6.setReadOnly(self.kilitle)
          self.ui.vardiya_adeti_7.setReadOnly(self.kilitle)
          self.ui.vardiya_adeti_8.setReadOnly(self.kilitle)


          self.ui.kar_marji.setReadOnly(self.kilitle)
          self.ui.vade_suresi.setReadOnly(self.kilitle)
          self.ui.vade_farki.setReadOnly(self.kilitle)

          self.ui.sekil.setCurrentIndex(0)
          self.ui.marka_secim.setCurrentIndex(0)

          self.ui.makine_secim.setCurrentIndex(0)
          self.ui.makine_secim_2.setCurrentIndex(0)
          self.ui.makine_secim_3.setCurrentIndex(0)
          self.ui.makine_secim_4.setCurrentIndex(0)
          self.ui.makine_secim_5.setCurrentIndex(0)
          self.ui.makine_secim_6.setCurrentIndex(0)
          self.ui.makine_secim_7.setCurrentIndex(0)
          self.ui.makine_secim_8.setCurrentIndex(0)
          self.ui.dis_cap.setText("0")
          self.ui.uzunluk.setText("0")
          self.ui.dis_cap_3.setText("0")
          self.ui.ic_cap_2.setText("0")
          self.ui.uzunluk_3.setText("0")         
          self.ui.en_3.setText("0")
          self.ui.uzunluk_4.setText("0")
          self.ui.genislik_3.setText("0")
          self.ui.en_4.setText("0")
          self.ui.uzunluk_5.setText("0")
          self.ui.genislik_4.setText("0")
          self.ui.en_7.setText("0")
          self.ui.uzunluk_10.setText("0")
          self.ui.agirlik_6.setText("0")



          self.ui.vardiya_adeti.setText("0")
          self.ui.vardiya_adeti_2.setText("0")
          self.ui.vardiya_adeti_3.setText("0")
          self.ui.vardiya_adeti_4.setText("0")
          self.ui.vardiya_adeti_5.setText("0")
          self.ui.vardiya_adeti_6.setText("0")
          self.ui.vardiya_adeti_7.setText("0")
          self.ui.vardiya_adeti_8.setText("0")

          self.ui.kar_marji.setText("0")
          self.ui.vade_suresi.setText("0")
          self.ui.vade_farki.setText("0")
          self.ui.vade_suresi_2.setText("0")
          self.ui.vade_farki_2.setText("0")


       


    def data_marka_change(self, data_detay):
       data_id = self.ui.label_25.text()
       seçilen_marka = self.kayit.ui.marka_secim.currentText()
       self.cursor.execute("UPDATE data_1 SET malzeme = ? WHERE data_id = ?", (seçilen_marka, data_id))
       self.connection.commit()
       self.kayit.hide()
       self.data_detay()


    def data_detay(self):

       if self.ui.label_25.text() == "TextLabel":
         self.kayit.show()
         self.kayit.ui.stackedWidget.setCurrentIndex(1)
         self.kayit.ui.label_2.setText("Tablodan seçim yapınız")
         
       else:
          self.ui.frame_207.hide()
          self.ui.frame_6.hide()
          self.ui.stackedWidget.setCurrentIndex(0)
          self.ui.stackedWidget_12.setCurrentIndex(1)
          if self.kilitle == True:
             self.kilitle = True
          else:
             self.kilitle = True

          self.cursor.execute("SELECT * FROM data_1 WHERE data_id = ?", (self.ui.label_25.text(),))
          data_1 = self.cursor.fetchall()

          self.cursor.execute("SELECT * FROM data_2 WHERE data_id = ?", (self.ui.label_25.text(),))
          data_2 = self.cursor.fetchall()

          self.cursor.execute("SELECT * FROM data_3 WHERE data_id = ?", (self.ui.label_25.text(),))
          data_3 = self.cursor.fetchall()

          self.cursor.execute("SELECT * FROM data_4 WHERE data_id = ?", (self.ui.label_25.text(),))
          data_4 = self.cursor.fetchall()

          self.ui.sekil.setDisabled(self.kilitle)

          self.ui.marka_secim.setDisabled(self.kilitle)

          self.ui.dis_cap.setReadOnly(self.kilitle)
          self.ui.uzunluk.setReadOnly(self.kilitle)
          self.ui.dis_cap_3.setReadOnly(self.kilitle)
          self.ui.uzunluk_3.setReadOnly(self.kilitle)
          self.ui.ic_cap_2.setReadOnly(self.kilitle)
          self.ui.en_3.setReadOnly(self.kilitle)
          self.ui.genislik_3.setReadOnly(self.kilitle)
          self.ui.uzunluk_4.setReadOnly(self.kilitle)
          self.ui.en_4.setReadOnly(self.kilitle)
          self.ui.genislik_4.setReadOnly(self.kilitle)
          self.ui.uzunluk_5.setReadOnly(self.kilitle)
          self.ui.en_7.setReadOnly(self.kilitle)
          self.ui.uzunluk_10.setReadOnly(self.kilitle)


          self.ui.makine_secim.setDisabled(self.kilitle)
          self.ui.makine_secim_2.setDisabled(self.kilitle)
          self.ui.makine_secim_3.setDisabled(self.kilitle)
          self.ui.makine_secim_4.setDisabled(self.kilitle)
          self.ui.makine_secim_5.setDisabled(self.kilitle)
          self.ui.makine_secim_6.setDisabled(self.kilitle)
          self.ui.makine_secim_7.setDisabled(self.kilitle)
          self.ui.makine_secim_8.setDisabled(self.kilitle)


          self.ui.vardiya_adeti.setReadOnly(self.kilitle)
          self.ui.vardiya_adeti_2.setReadOnly(self.kilitle)
          self.ui.vardiya_adeti_3.setReadOnly(self.kilitle)
          self.ui.vardiya_adeti_4.setReadOnly(self.kilitle)
          self.ui.vardiya_adeti_5.setReadOnly(self.kilitle)
          self.ui.vardiya_adeti_6.setReadOnly(self.kilitle)
          self.ui.vardiya_adeti_7.setReadOnly(self.kilitle)
          self.ui.vardiya_adeti_8.setReadOnly(self.kilitle)


          self.ui.kar_marji.setReadOnly(self.kilitle)
          self.ui.vade_suresi.setReadOnly(self.kilitle)
          self.ui.vade_farki.setReadOnly(self.kilitle)



          if data_1 is not None:
              operation_2 = data_1[0][4]
              self.ui.sekil.setCurrentText(f"{data_1[0][4]}")

              if data_1[0][3] in [self.ui.marka_secim.itemText(index) for index in range(self.ui.marka_secim.count())]:
                 self.ui.marka_secim.setCurrentText(f"{data_1[0][3]}")
              else:
                 self.kayit.show()
                 self.kayit.ui.label_4.setText(data_1[0][3])
                 self.kayit.ui.stackedWidget.setCurrentIndex(2)

              if data_2[0][1] in [self.ui.makine_secim.itemText(index) for index in range(self.ui.makine_secim.count())]:
                 self.ui.makine_secim.setCurrentText(f"{data_2[0][1]}")
              else:
                 self.kayit.show()
                 self.kayit.ui.label_4.setText(data_2[0][1])
                 self.kayit.ui.label_7.setText("seçilen_makine")
                 self.kayit.ui.stackedWidget.setCurrentIndex(3)
                 self.kayit.ui.stackedWidget_3.setCurrentIndex(8)                                  
              
              if data_2[0][2] in [self.ui.makine_secim_2.itemText(index) for index in range(self.ui.makine_secim_2.count())]:
                 self.ui.makine_secim_2.setCurrentText(f"{data_2[0][2]}")
              else:
                 self.kayit.show()
                 self.kayit.ui.label_4.setText(data_2[0][2])
                 self.kayit.ui.label_7.setText("seçilen_makine_2")
                 self.kayit.ui.stackedWidget.setCurrentIndex(3)
                 self.kayit.ui.stackedWidget_3.setCurrentIndex(1)

              if data_2[0][3] in [self.ui.makine_secim_3.itemText(index) for index in range(self.ui.makine_secim_3.count())]:
                 self.ui.makine_secim_3.setCurrentText(f"{data_2[0][3]}")
              else:
                 self.kayit.show()
                 self.kayit.ui.label_4.setText(data_2[0][3])
                 self.kayit.ui.label_7.setText("seçilen_makine_3")
                 self.kayit.ui.stackedWidget.setCurrentIndex(3)
                 self.kayit.ui.stackedWidget_3.setCurrentIndex(2)              

              if data_2[0][4] in [self.ui.makine_secim_4.itemText(index) for index in range(self.ui.makine_secim_4.count())]:
                 self.ui.makine_secim_4.setCurrentText(f"{data_2[0][4]}")
              else:
                 self.kayit.show()
                 self.kayit.ui.label_4.setText(data_2[0][4])
                 self.kayit.ui.label_7.setText("seçilen_makine_4")
                 self.kayit.ui.stackedWidget.setCurrentIndex(3)
                 self.kayit.ui.stackedWidget_3.setCurrentIndex(3)  

              if data_2[0][5] in [self.ui.makine_secim_5.itemText(index) for index in range(self.ui.makine_secim_5.count())]:
                 self.ui.makine_secim_5.setCurrentText(f"{data_2[0][5]}")
              else:
                 self.kayit.show()
                 self.kayit.ui.label_4.setText(data_2[0][5])
                 self.kayit.ui.label_7.setText("seçilen_makine_5")
                 self.kayit.ui.stackedWidget.setCurrentIndex(3)
                 self.kayit.ui.stackedWidget_3.setCurrentIndex(4)  

              if data_2[0][6] in [self.ui.makine_secim_6.itemText(index) for index in range(self.ui.makine_secim_6.count())]:
                 self.ui.makine_secim_6.setCurrentText(f"{data_2[0][6]}")
              else:
                 self.kayit.show()
                 self.kayit.ui.label_4.setText(data_2[0][6])
                 self.kayit.ui.label_7.setText("seçilen_makine_6")
                 self.kayit.ui.stackedWidget.setCurrentIndex(3)
                 self.kayit.ui.stackedWidget_3.setCurrentIndex(5) 

              if data_2[0][7] in [self.ui.makine_secim_7.itemText(index) for index in range(self.ui.makine_secim_7.count())]:
                 self.ui.makine_secim_7.setCurrentText(f"{data_2[0][7]}")
              else:
                 self.kayit.show()
                 self.kayit.ui.label_4.setText(data_2[0][7])
                 self.kayit.ui.label_7.setText("seçilen_makine_7")
                 self.kayit.ui.stackedWidget.setCurrentIndex(3)
                 self.kayit.ui.stackedWidget_3.setCurrentIndex(6)
               
              if data_2[0][8] in [self.ui.makine_secim_8.itemText(index) for index in range(self.ui.makine_secim_8.count())]:
                 self.ui.makine_secim_8.setCurrentText(f"{data_2[0][8]}")
              else:
                 self.kayit.show()
                 self.kayit.ui.label_4.setText(data_2[0][8])
                 self.kayit.ui.label_7.setText("seçilen_makine_8")
                 self.kayit.ui.stackedWidget.setCurrentIndex(3)
                 self.kayit.ui.stackedWidget_3.setCurrentIndex(7)



              if operation_2 == "Yuvarlak":
                 self.ui.dis_cap.setText(f"{data_1[0][5]}")
                 self.ui.uzunluk.setText(f"{data_1[0][6]}")

              elif operation_2 == "Boru":
                 self.ui.dis_cap_3.setText(f"{data_1[0][5]}")
                 self.ui.ic_cap_2.setText(f"{data_1[0][6]}")
                 self.ui.uzunluk_3.setText(f"{data_1[0][7]}")

              elif operation_2 == "Kare":
                 self.ui.en_3.setText(f"{data_1[0][5]}")
                 self.ui.uzunluk_4.setText(f"{data_1[0][6]}")
                 self.ui.genislik_3.setText(f"{data_1[0][7]}")

              elif operation_2 == "Lama":
                 self.ui.en_4.setText(f"{data_1[0][5]}")
                 self.ui.uzunluk_5.setText(f"{data_1[0][6]}")
                 self.ui.genislik_4.setText(f"{data_1[0][7]}")

              elif operation_2 == "Altıgen":
                 self.ui.en_7.setText(f"{data_1[0][5]}")
                 self.ui.uzunluk_10.setText(f"{data_1[0][6]}")

              elif operation_2 == "Ham":
                 self.ui.agirlik_6.setText(f"{data_1[0][5]}")
              
              self.ui.vardiya_adeti.setText(f"{data_3[0][1]}")
              self.ui.vardiya_adeti_2.setText(f"{data_3[0][2]}")
              self.ui.vardiya_adeti_3.setText(f"{data_3[0][3]}")
              self.ui.vardiya_adeti_4.setText(f"{data_3[0][4]}")
              self.ui.vardiya_adeti_5.setText(f"{data_3[0][5]}")
              self.ui.vardiya_adeti_6.setText(f"{data_3[0][6]}")
              self.ui.vardiya_adeti_7.setText(f"{data_3[0][7]}")
              self.ui.vardiya_adeti_8.setText(f"{data_3[0][8]}")

              self.ui.kar_marji.setText(f"{data_4[0][1]}")
              self.ui.vade_suresi.setText(f"{data_4[0][2]}")
              self.ui.vade_farki.setText(f"{data_4[0][3]}")
              self.ui.vade_suresi_2.setText(f"{data_4[0][4]}")
              self.ui.vade_farki_2.setText(f"{data_4[0][5]}")

          else:
             pass

    def data_makine_change(self):
       data_id = self.ui.label_25.text()
       makine_hangisi = self.kayit.ui.label_7.text()
       if makine_hangisi == "seçilen_makine":
          new_makine = self.kayit.ui.makine_secim.currentText()
          self.cursor.execute("UPDATE data_2 SET makine_name = ? WHERE data_id = ?", (new_makine, data_id))
          self.connection.commit()
          self.kayit.hide()
          self.data_detay()
                      
       elif makine_hangisi == "seçilen_makine_2":
          new_makine = self.kayit.ui.makine_secim_2.currentText()
          self.cursor.execute("UPDATE data_2 SET makine_name_2 = ? WHERE data_id = ?", (new_makine, data_id))
          self.connection.commit()
          self.kayit.hide()
          self.data_detay()
             
       elif makine_hangisi == "seçilen_makine_3":
          new_makine = self.kayit.ui.makine_secim_3.currentText()
          self.cursor.execute("UPDATE data_2 SET makine_name_3 = ? WHERE data_id = ?", (new_makine, data_id))
          self.connection.commit()
          self.kayit.hide()
          self.data_detay()           

       elif makine_hangisi == "seçilen_makine_4":
          new_makine = self.kayit.ui.makine_secim_5.currentText()
          self.cursor.execute("UPDATE data_2 SET makine_name_4 = ? WHERE data_id = ?", (new_makine, data_id))
          self.connection.commit()
          self.kayit.hide()
          self.data_detay()

       elif makine_hangisi == "seçilen_makine_5":
          new_makine = self.kayit.ui.makine_secim_6.currentText()
          self.cursor.execute("UPDATE data_2 SET makine_name_5 = ? WHERE data_id = ?", (new_makine, data_id))
          self.connection.commit()
          self.kayit.hide()
          self.data_detay()

       elif makine_hangisi == "seçilen_makine_6":
          new_makine = self.kayit.ui.makine_secim_7.currentText()
          self.cursor.execute("UPDATE data_2 SET makine_name_6 = ? WHERE data_id = ?", (new_makine, data_id))
          self.connection.commit()
          self.kayit.hide()
          self.data_detay()

       elif makine_hangisi == "seçilen_makine_7":
          new_makine = self.kayit.ui.makine_secim_8.currentText()
          self.cursor.execute("UPDATE data_2 SET makine_name_7 = ? WHERE data_id = ?", (new_makine, data_id))
          self.connection.commit()
          self.kayit.hide()
          self.data_detay()        
        
       elif makine_hangisi == "seçilen_makine_8":
          new_makine = self.kayit.ui.makine_secim_9.currentText()
          self.cursor.execute("UPDATE data_2 SET makine_name_8 = ? WHERE data_id = ?", (new_makine, data_id))
          self.connection.commit()
          self.kayit.hide()
          self.data_detay()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            if self.offset is not None:
                # Pencereyi yeni konuma taşı
                self.move(self.pos() + event.pos() - self.offset)
                self.offset = event.pos()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = False
            self.offset = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())