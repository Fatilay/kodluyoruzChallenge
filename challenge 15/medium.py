# Kullanıcıdan bir metin almanızı istiyorum. Bu metnin içindeki en çok tekrar eden harfi bulmalı ve kaç kere tekrar ettiğini göstermeli.
def enCokTekrarEdenHarf(metin):
    harfSayisi = {} #metindeki harfleri tutmak için kullanılan sözlük

    for harf in metin : 
        #hepsini küçük harfe dönüştür
        harf=harf.lower()
        #sadece harfleri say
        if harf.isalpha():
            harfSayisi[harf] = harfSayisi.get(harf,0)+1
     # En çok tekrar eden harfi ve tekrar sayısını buluyoruz
    enCokTekrarEdenHarf = None
    enCokTekrar = 0

    for harf, tekrar in harfSayisi.items():
        if tekrar > enCokTekrar:
            enCokTekrarEdenHarf = harf 
            enCokTekrar = tekrar
    return enCokTekrarEdenHarf,enCokTekrar
#kullanıcıdan bir metin alıyoruz
metin = input('lutfen bir metin girin: ')

#en çok tekrar eden harf ve tekrar sayisi
enCokTekrarEdenHarf, enCokTekrar = enCokTekrarEdenHarf(metin)

print('en cok tekrar eden harf: ',enCokTekrarEdenHarf , 'tekrar sayisi: ', enCokTekrar)


    