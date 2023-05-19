#girdi txt sinden alınan metin okunuyor 
#lzw.txt ye sıkıştırılmadan önceki ve sonraki boyut yazılıyor

import time
def lzw_alghorithm(cumle):
    baslangic_zamani_lzw = time.time()
    uzunluk=len(cumle) 
    index_sozluk={}
    a=0
    for i in cumle:
        if i in index_sozluk:
            pass
        else:
            index_sozluk[i]=a
            a+=1
        
    print(index_sozluk)
    boyut=0
    for k in index_sozluk:
        boyut=boyut+1

    bit_number=1
    durum=0
    while(durum==0):
        if(2**bit_number<=boyut):
            bit_number=bit_number+1
        else:
            durum=1

    bit_number_first=uzunluk*bit_number
    son_string=["ilkeleman"]
    output=[]
    sc=str
    outputstring=str
    index_sozluk_eleman=len(index_sozluk)
    baslangıc_index=0
    for i in cumle:
        for j in son_string:
            if baslangıc_index==0:
                sc=i
                son_string[0]=i
                baslangıc_index=1
            
            else:
                sc=son_string[-1]+i
                string_mevcut=son_string[-1]
                for x in index_sozluk :
                    if string_mevcut== x and sc not in index_sozluk:
                        output.append(index_sozluk[x])
                
                if sc not in index_sozluk:
                    index_sozluk[sc]=index_sozluk_eleman
                    index_sozluk_eleman=index_sozluk_eleman+1
                    son_string.append(i)
                    # output.append()
                else:
                     son_string.append(sc)
                break
    # print(index_sozluk[sc]) 
    # print(output)       
    output.append(index_sozluk[sc])          
    # print(output)
    # print(index_sozluk)

    bitis_zamani_lzw = time.time()

    calisma_suresi_lzw = bitis_zamani_lzw - baslangic_zamani_lzw
    boyut=0
    for k in index_sozluk:
        boyut=boyut+1

    bit_number=1
    durum=0
    while(durum==0):
        if(2**bit_number<=boyut):
            bit_number=bit_number+1
        else:
            durum=1

    bit_number_son=len(output)*bit_number
    # print(calisma_suresi_lzw)
    with open("lzw.txt", 'r') as dosya:
        for satir in dosya:
            uzunluk += len(satir)

    with open("lzw.txt", 'a',encoding="utf-8") as dosya:
        dosya.write("LZW kodunun çalışma zamanı: " + str(calisma_suresi_lzw) + "\n"
                    + "LZW sıkıştırılmadan önceki boyut: " + str(bit_number_first) + "\n"
                    + "LZW sıkıştırıldıktan sonraki boyut: " + str(bit_number_son)+"\n")


dosya = open("girdi.txt", "r",encoding="utf-8") 
cumle= dosya.read() 

lzw_alghorithm(cumle)

