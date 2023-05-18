#ÖĞRENCİ AD SOYAD----> SENANUR İNCEKARA


def yolcukayit():
    yolcu=int(input("Kaç yolcu kayıt edeceksiniz-->"))
    
    for i in range(1,yolcu+1):
        ad =input("Yolcu adı nedir->")
        soyad=input("Yolcu Soyadı nedir-> ")
        durum=True
        while durum:
            tcno=input("Yolcu TC kimlik numarasi->")
            if len(tcno)!=11:   #TC no 11 rakamdan oluşma kontrolü sağlandı
                print("\n\tTC kimlik numarası 11 rakamdan oluşmaktadır . Lütfen 11 rakam olacak şekilde giriniz\n")
            else:
                durum=False
       
        durum=True
        while durum:
            cinsiyet=input("Yolcunun cinsiyeti nedir (kadın / erkek olarak giriniz)->")
            if cinsiyet!="kadın" and cinsiyet!="erkek":
                print(f"Cinsiyet bilgisi yanlış girildi")
            else:
                durum=False
        durum=True
        while durum:
            telno=input("Yolcunun telefon numarasi nedir->")
            if len(telno)!=11:
                print("\n\tTelefon numarasını 11 rakamdan oluşacak şekilde giriniz\n")
            else:
                durum=False
        yas=input("Yolcunun yasi nedir->")
        
       
        for j in range(0,1):
            bavulkg=input(f"{i}. Yolcunun bavulu kaç kg (her yolcunun 12 kg hakki vardir (12kg+ bavula sahip olan yolculardan kg basina 50 TL alinacaktir)\n-->")
            
        with open("21100011027.txt","a",encoding="utf-8")as file:  #dosya açıldı ve kaldığımız satırdan bilgiler içine yazıldı
            file.write(tcno+" ,"+ad+" ,"+soyad+" ,"+cinsiyet+" ,"+telno+" ,"+yas+" ,"+bavulkg+"\n")
           

def yolculistele():
    tcdic={} #sırayla kulanacağım sözlükleri tanımladık
    addic={}
    soyaddic={}
    cinsdic={}
    teldic={}
    yasdic={}
    bavuldic={} 
    with open("21100011027.txt","r",encoding="utf-8")as file:  #dosya read (okuma) olarak açıldı
        sayac=0 #key bilgisi için sayac tanımladık
        for j in file:
            j=j.strip() #dosya içerisinden satırları ayırdık
            if len(j)>=1:
                lists=j.split(',') #satırları liste içine aldık ve "," e göre index numarasını ayırdık
                
                tcdic[sayac]=lists[0] #sözlük içine hepsinin key nosu aynı olacak şekilde ekledik
                addic[sayac]=lists[1]
                soyaddic[sayac]=lists[2]
                cinsdic[sayac]=lists[3]
                teldic[sayac]=lists[4]
                yasdic[sayac]=lists[5]
                bavuldic[sayac]=lists[6]  
        
            sayac+=1   #key nosu 0,1,2.. şeklinde artması için sayac döngü sonunda 1 artırıldı
        i=1    
        for key in tcdic:  #sözlük içine girdik ve print ile listeleme işlemini yaptık
            print(f"{i}. yolcunun bilgileri:\nADI->{addic[key]}\nSOYAD->{soyaddic[key]}\nTC NO-> {tcdic[key]}\nCİNSİYET->{cinsdic[key]}\nYAŞ->{yasdic[key]}\nTELEFON NO->{teldic[key]}\nBAVUL KG MİKTARI->{bavuldic[key]} Kg\n---------------\n")   
            i+=1 
             
def ozelyolcuara():
    tcdic={} #sırayla kulanacağım sözlükleri tanımladık
    addic={}
    soyaddic={}
    cinsdic={}
    teldic={}
    yasdic={}
    bavuldic={} 
    with open("21100011027.txt","r",encoding="utf-8")as file:  #dosya read (okuma) olarak açıldı
        sayac=0 #key bilgisi için sayac tanımladık
        for j in file:
            j=j.strip() #dosya içerisinden satırları ayırdık
            if len(j)>=1:
                lists=j.split(',') #satırları liste içine aldık ve "," e göre index numarasını ayırdık
                
                tcdic[sayac]=lists[0] #sözlük içine hepsinin key nosu aynı olacak şekilde ekledik
                addic[sayac]=lists[1]
                soyaddic[sayac]=lists[2]
                cinsdic[sayac]=lists[3]
                teldic[sayac]=lists[4]
                yasdic[sayac]=lists[5]
                bavuldic[sayac]=lists[6]  
        
            sayac+=1   #key nosu 0,1,2.. şeklinde artması için sayac döngü sonunda 1 artırıldı
        
        bul=input("Hangi yolcunun bilgisine ulaşmak istiyorsanız lütfen TC numarasını giriniz->")    
        bulundu=0
        for key in tcdic:
            tcdic[key]=tcdic[key].strip()
            if tcdic[key]==bul:
                print(f"ADI->{addic[key]}\nSOYAD->{soyaddic[key]}\nTC NO-> {tcdic[key]}\nYAŞ->{yasdic[key]}\nBAVUL KG->{bavuldic[key]} Kg")
                bulundu=1
        if bulundu==0:
            print(f"{bul} Tc'li Yolcu bulunamadı")
        

def yolcubilgiguncelle():
    
    tcdic={}
    addic={}
    soyaddic={}
    cinsdic={}
    teldic={}
    yasdic={}
    bavuldic={} 
    with open("21100011027.txt","r+",encoding="utf-8")as file: #dosya okuma ve yazma olarak açıldı
        
        sayac=0
        for j in file:
            j=j.strip()  #dosya içerisindeki satırları ayırdık
               
            if len(j)>=1:
                lists=j.split(',')      #satırları liste içine aldık ve "," e göre index numarasını ayırdık      
                tcdic[sayac]=lists[0]
                addic[sayac]=lists[1]
                soyaddic[sayac]=lists[2]
                cinsdic[sayac]=lists[3]
                teldic[sayac]=lists[4]
                yasdic[sayac]=lists[5]
                bavuldic[sayac]=lists[6]
        
            sayac+=1   

        
        new=input("değiştirmek istediğin yolcunun TC nosu nedir? ")
        okey=0
        for key,value in tcdic.items():   
            value=value.strip() #boşluk value değerlerden ayrıldı
            if str(new)==str(value):
                okey=1
                durum=True
                while durum:
                    newtc=input("YENİ TC->")
                    if len(newtc)!=11:
                        print("\n\tTC kimlik numarası 11 rakamdan oluşmaktadır . Lütfen 11 rakam olacak şekilde giriniz\n")
                    else:
                        
                        durum=False
                    
                tcdic[key]=newtc  #yeni tc nosu sözlüğün içine atandı

                newad=input("yolcunun adı->")
                addic[key]=newad   #yeni ad bilgisi addic sözlüğünün içine atandı
                newsoyad=input("yolcunun soyadı nedir-> ")
                soyaddic[key]=newsoyad
                durum=True

                while durum:
                    newcinsiyet=input("Yolcunun cinsiyeti nedir (kadın / erkek olarak giriniz)->")
                    if newcinsiyet!="kadın" and newcinsiyet!="erkek":
                        print(f"Cinsiyet bilgisi yanlış girildi")
                    else:
                        durum=False

                cinsdic[key]=newcinsiyet

                durum=True
                while durum:
                    newtel=input("Yolcunun telefon numarasi nedir->")
                    if len(newtel)!=11:
                       print("\n\tTelefon numarasını 11 rakamdan oluşacak şekilde giriniz\n")
                    else:
                       durum=False

                teldic[key]=newtel
                newyas=input("yolcunun yaşı->")
                yasdic[key]=newyas
                newbavul=input("yolcunun bavul kg bilgisi->")
                bavuldic[key]=newbavul
        if okey==0:
            print(f"{new} TC nosuna sahip yolcu bulunamadı")    

         
        file.seek(0,0) #başlangıç yerine seek metotu ile gittik
        file.truncate()  #dosyanın bütün içeriği silindi

        for key in tcdic:  #dosya içerisine sözlük bilgileri sırasıyla yazıldı
            file.write(f"{tcdic[key]}, {addic[key]}, {soyaddic[key]}, {cinsdic[key]}, {teldic[key]}, {yasdic[key]}, {bavuldic[key]}\n")
        
        
adliste=[]
soyadliste=[]
tcnolist=[]
cinsiyetlist=[]
telnolist=[]
yaslist=[]
bavullist=[]
                       
def yolcusil():
    global tcnolist #silince yolcunun tcsine kolay ulaşabilmek için global olarak tanımladık
    tcnolist=[]
    with open("21100011027.txt","r+",encoding="utf-8")as file: #dosyayı okuma ve yazma olarak açtık
        for j in file: #dosyanın içine girdik
            j=j.strip() #dosya içeriğindeki satırları aldık
            
            if len(j)>=1:
                lists=j.split(',') #satırları liste içine aldık ve "," e göre index numarasını ayırdık
                tcnolist.append(lists[0].strip()) #listenin 0. eleamnını tcnolistesine gönderdik
                adliste.append(lists[1].strip())
                soyadliste.append(lists[2].strip())
                cinsiyetlist.append(lists[3].strip())
                telnolist.append(lists[4].strip())
                yaslist.append(lists[5].strip())
                bavullist.append(lists[6].strip())  
             
        silincek=input("kaydını silmek istediğiniz yolcunun TC kimlik numarası nedir -> ")
        try:
           index=tcnolist.index(silincek) #silinecek tc nin indexi metot yardımı ile bulundu
           tcnolist.pop(index) #silme işlemi pop metotu ile sağlandı
           adliste.pop(index)
           soyadliste.pop(index)
           cinsiyetlist.pop(index)
           yaslist.pop(index)
           bavullist.pop(index)
        
        
           file.seek(0,0) #dosya içerisinde en baş konuma gittik
           file.truncate() #dosyanın bütün içeriği silindi
        
        
           for index in range(len(tcnolist)): #liste içerisine yazdığımız bilgiler sayesinde dosyaya tekrar yazım işlemini yaptık
                file.write(f"{tcnolist[index]}, {adliste[index]}, {soyadliste[index]}, {cinsiyetlist[index]}, {telnolist[index]}, {yaslist[index]}, {bavullist[index]}\n")
           print("\nYolcu başarılı bir şekilde silindi")    
        except ValueError: #TC numarası liste içinde bulunamaz ise value error hatası direkt exceptte yazdırılacak
            print("\nBöyle bir yolcu bulunamadı")   
         
        
#İÇİÇE FONKSİYON BİLET HESAPLAMADA KULLANILDI

def yolcubiletfiyatlistesi():
    print("\n\t\tYOLCULARIN ÖDEYECEĞİ ÜCRET BİLGİLENDİRMESİ\n")
    print("-"*100)
    biletdic={} #ilk fiyat hesaplanması için sözlük oluşturuldu
    with open("21100011027.txt","r+",encoding="utf-8")as file: #dosya içindeki bilgilerin okunması için 
        
        for j in file:
            j=j.strip() #satır olarak ayırdık 
            
            if len(j)>=1:
                lists=j.split(',') #her bir satır "," işaretinden ayrıldı liste içinde indexlendi
                j=int(lists[5])  #str değer olduğu için int a çevirdik. Yaş bilgisini veriyor
                k=int(lists[6]) #Bavul bilgisini veriyor . int a çevirdik
                if j>25: 
                    bavulfiyat=(k-12)*50  #Bavul fiyatı standart 12 kg limit üstünde kg başına 50 tl
                    bilet=bavulfiyat+300   #yaş 25 ten büyük ise +300
                if j<=25 and j>18:
                    bavulfiyat=(k-12)*50
                    bilet=bavulfiyat+175  #yaş 25-18 arası ise +175
                if j<=18 and j>6:
                    bavulfiyat=(k-12)*50
                    bilet=bavulfiyat+150  #yaş 18-6 arası ise +150
                if j<=6:
                    bavulfiyat=(k-12)*50
                    bilet=bavulfiyat+100  #yaş 6 dan küçük ise +100
                biletdic[lists[0]]=bilet  #bilet fiyatı key tc olacak şekilde biletdic sözlüğüne atıldı
                print(f"{lists[0]} TC li yolcunun yaşı {lists[5]} ve bavul kg miktarı {lists[6]} olduğu için ödemesi gereken miktar --> {bilet}")
        print("-"*100)        
                      
  
        
    def indirim():  #İÇ İÇE FONKSİYON  EKSTRA İNDİRİM HESAPLAMASI 
      indirim={}    #indirim sözlüğü oluşturuldu
      print("\n")
      print("*"*80)
      print("\n\t\tEKSTRA İNDİRİM KAMPANYALARI\n\tEngelli yolcularımız için %40 indirim\n\tŞehit ve gazi yakınlarımız için %50 indirim\n\n")
      print("*"*80)
      print("\n")

      for key,value in biletdic.items():  #BİLETDİC sözlüğünün içine girdik
          engel=input(f"{key} TC nolu yolcunun Herhangi bir engeli var mı ?(evet için e hayır için h giriniz) ")  #key->tc no bilgisini veriyor
          if engel=='e'or engel== 'E':
              print("%40 indirim\n") 
          if engel=='h'or engel=='H':
              print()

          sgyakin=input(f"{key} TC nolu yolcu Şehit veya gazi yakını mı ?(evet için e hayır için h giriniz) ")
          if sgyakin=='e'or sgyakin=='E':
              print("%50 indirim\n")
          if sgyakin=='h'or sgyakin=='H':
              print()
          indirim[key]=engel+sgyakin  #indirimin uygulanması için sözlüğün içine girilen cevapları ekledik
        
         
      global sonbiletdic #dışardada kullanabilmek amacıyla global olarak tanımladık
      sonbiletdic={} 

      for i in indirim:  #indirim hesaplanması yapılıyor
                
              if indirim[i]=='ee'or indirim[i]=='EE' or indirim[i]=='Ee' or indirim[i]== 'eE':
                  in1=biletdic[i] -(biletdic[i]*40)/100
                  sonBilet=in1-(in1*50)/100
              if indirim[i]=='eh' or indirim[i]== 'EH' or indirim[i]== 'Eh' or indirim[i]== 'eH':
                  in1=biletdic[i] -(biletdic[i]*40)/100
                  sonBilet=in1
              if indirim[i]=='he' or indirim[i]=='HE' or indirim[i]=='hE' or indirim[i]=='He':
                  in1=biletdic[i] -(biletdic[i]*50)/100
                  sonBilet=in1
              if indirim[i]=='hh' or indirim[i]=='HH' or indirim[i]=='Hh' or indirim[i]=='hH':
                  sonBilet=biletdic[i]

              sonbiletdic[i]=sonBilet   #hesaplamalar sobiletdic sözlüğüne atandı
       
      print("\n")
      print("*"*80)
      for k in sonbiletdic:
              print(f"{k} TC li yolcunun ödemesi gereken bilet ---> {sonbiletdic[k]}")
              
      print("*"*80)         
     
                
    return indirim()      


def maxbilet():
    max=0
    min=0
    for key,value in sonbiletdic.items():  #sözlüğün içine girdik
        if max<value:
            max=value
            maxtc=key
    print(f"{maxtc } TC kimlik numarasına sahip kisi {max} TL ile en yüksek ücreti ödemektedir  ")    

def cikis():
    exit()       

while True:
    print("\n\tKONYA-KENYA SEFERLERİ UÇUŞ MENÜSÜ")
    islem=input("\n\t1-YOLCU KAYIT\n\t2-YOLCULARI LISTELE\n\t3-ÖZEL YOLCU ARA\n\t4-YOLCU BILGILERINI GUNCELLE\n\t5-YOLCU SIL\n\t6-YOLCUNUN ODEYECEGI BILET FIYAT BILGISI\n\t7-EN YUKSEK BILET FIYATI\n\t8-CIKIS\n\n\tISLEMINIZI GIRIIZ-->")
    if islem=='1':
        yolcukayit()
    
    if islem=='2':
        yolculistele()
    if islem=='3':
        ozelyolcuara()    
    if islem=='4':
        yolcubilgiguncelle()
        
    if islem=='5':
        yolcusil()
        
    if islem=='6':
        yolcubiletfiyatlistesi()
        
    if islem=='7':
        maxbilet()
        
    if islem=='8':
        cikis()
        