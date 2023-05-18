import os

eskifile_dizin = r'C:\eski file path'  
yenifile_dizin = r'C:\kaydedilmek istenen file path'  

if not os.path.exists(yenifile_dizin):
    os.makedirs(yenifile_dizin)

for dosya in os.listdir(eskifile_dizin):
    if dosya.endswith('.jpg'):  
        eski_yol = os.path.join(eskifile_dizin, dosya)
        yeni_dosya = dosya.split('_BSRGAN')[0] + '.jpg'  # Dosya adı _BSRGAN a kadar kısım ile değiştirildi
        yeni_yol = os.path.join(yenifile_dizin, yeni_dosya)
        os.rename(eski_yol, yeni_yol)

