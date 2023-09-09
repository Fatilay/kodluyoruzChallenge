import time
import datetime
import locale
locale.setlocale(locale.LC_ALL,'turkish')

dogumTarihi = input('dogum tarihinizi giriniz(gun ay yil): ')
suan = datetime.datetime.now()

tarih = datetime.datetime.strptime(dogumTarihi, '%d %m %Y')
yas = (suan.year - tarih.year)
#dogum günü henüz gecmediyse yas 1 azalt
if tarih.month>suan.month or (tarih.month==suan.month and tarih.day>suan.day):
    yas-=1

print('yasiniz: ', yas)


