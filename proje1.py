BIR_KUTUDA_OLABILECEK_EN_AZ_BILYE = 10
absurt_deger = 1234567890 # en kucuk farki bulurken ilk seferde bloga kesinlikle girmesini saglamak icin kullanılan deger
MIN_BILYE_AGIRLIK = 0

uretim_hatasi_olan_kutular = 0
tum_kutular = 0
tum_bilyeler = 0
iade_edilen_bilye_sayisi = 0
tum_bilyeler_esit_agirlik = 0
hafif_bilyeli_kutu = 0
agır_bilyeli_kutu = 0
agır_olanlar_icin_agırlık_farkı = 0 # farkli bilye agir oldugu durumda kullanilan fark degiskeni
agır_olanlar_icin_agırlık_farkı_yuzde = 0 # farkli bilye agir oldugu durumda kullanilan fark orani degiskeni
hafif_olanlar_icin_agırlık_farkı = 0 # farkli bilye hafif oldugu durumda kullanilan fark degiskeni
hafif_olanlar_icin_agırlık_farkı_yuzde = 0 # farkli bilye hafif oldugu durumda kullanilan fark orani degiskeni
en_cok_bilyeli_kutu_butun_bilyeler_esitse_bilye_sayisi = 0
en_agir_bilye_agirlik = 0
en_agir_bilyeler_kutu_bilye_sayisi = 0
farkli_bilyenin_farki_en_buyuk = 0
fark_en_buyuk_olunca_oran = 0
farkli_bilyenin_farki_en_kucuk = 0
fark_en_kucuk_olunca_oran = 0

# kullanicidan baska kutu olup olmadıgının bilgisi evet veya hayir olarak kontrol ediliyor
secim = "e"
# secim == "e" veya secim == "E" oldugu sürece tum kutulara 1 ekleniyor ve bilye sayisi aliniyor
while (secim == "e" or secim == "E"):
    tum_kutular += 1
    kutudaki_bilye_sayisi = int(input("lutfen kutudaki bilye sayisini giriniz bilye sayisi en az 10 olmali"))

    # kutudaki bilye sayisi kesinlikle en az 10 olmali burada bunun kontrolu yapiliyor eger girilen degerde hata yoksa
    # alinan bilye sayisi tum bilyeler degiskenine toplaniyor
    while (kutudaki_bilye_sayisi < BIR_KUTUDA_OLABILECEK_EN_AZ_BILYE):
        kutudaki_bilye_sayisi = int(input("hatali bilye sayisi girdiniz lutfen en az 10 degerini girin"))
    tum_bilyeler += kutudaki_bilye_sayisi

    # ilk 3 bilye agirligi manuel olarak dongusuz aliniyor ve her birinin 0 mg dan daha fazka agirlikta oldugu kontrol ediliyor
    bilye_agirlik_1 = int(input("lutfen 1. bilyenin miligram cinsinden agirligini giriniz"))
    while bilye_agirlik_1 <= MIN_BILYE_AGIRLIK:
        bilye_agirlik_1 = int(input("bilye agirligi 0 dan kucuk veya esit olamaz lutfen 1. bilyenin miligram cinsinden agirligini tekrar giriniz"))
    bilye_agirlik_2 = int(input("lutfen 2. bilyenin miligram cinsinden agirligini giriniz"))
    while bilye_agirlik_2 <= MIN_BILYE_AGIRLIK:
        bilye_agirlik_2 = int(input("bilye agirligi 0 dan kucuk veya esit olamaz lutfen 2. bilyenin miligram cinsinden agirligini tekrar giriniz"))
    bilye_agirlik_3 = int(input("lutfen 3. bilyenin miligram cinsinden agirligini giriniz"))
    while bilye_agirlik_3 <= MIN_BILYE_AGIRLIK:
        bilye_agirlik_3 = int(input("bilye agirligi 0 dan kucuk veya esit olamaz lutfen 3. bilyenin miligram cinsinden agirligini tekrar giriniz"))

    # manuel alinan 3 bilyenin agirlikleri birbirlerinden farkli ise kalan degerlere bakilmadan hatali kutu olarak ayriliyor
    # uretim hatasi olan kutularin sayisi ise 1 artırılıp iade edilen bilye sayisi ise o kutudaki bilye sayisi kadar artiyor
    if bilye_agirlik_1 != bilye_agirlik_2 and bilye_agirlik_1 != bilye_agirlik_3 and bilye_agirlik_2 != bilye_agirlik_3:
        uretim_hatasi_olan_kutular += 1
        iade_edilen_bilye_sayisi += kutudaki_bilye_sayisi
        print("kutuda uretim hatasi var")

    # eger boyle bir durum yoksa diger bilyelerin agirliklari alinmaya basliyor
    else:
        hatali_bilye_sayisi = 0 # 2 adet farkli bilye tespit deildiginde hatali kutu olacak, degisken basta 0
        for x in range(4,kutudaki_bilye_sayisi+1):
            bilye_agirlik = int(input(f"lutfen {x}. bilyenin miligram cinsinden agirligini giriniz"))

            # bilye agirliginin 0 veya 0 dan kucuk oldugu bir durumda verş tekrar aliniyor
            while bilye_agirlik <= MIN_BILYE_AGIRLIK:
                bilye_agirlik = int(input(f"bilye agirligi 0 dan kucuk veya esit olamaz lutfen {x}. bilyenin miligram cinsinden agirligini tekrar giriniz"))

            # manuel alinan 3 bilyenin de agirligi esitse cogunluk olan bilye sayisi bu agirlik ataniyor
            if bilye_agirlik_1 == bilye_agirlik_2 and bilye_agirlik_2 == bilye_agirlik_3:
                cogunluk_bilye_agirlik = bilye_agirlik_1

                # eger yeni gelen bilye agirligi 1. bilyenin agirligi yani cogunluk bilye agirligindan farkli gelirse
                # bu agirlik digerlerinden farkli olan agirlik olarak ataniyor
                if bilye_agirlik != bilye_agirlik_1:
                    farkli_bilye_agirlik = bilye_agirlik

            # 1. ve 2. birbirine esit fakat 3. onlara esit degilse 1. ve 2. bilyenin agirlik degeri cogunluk bilye
            # agirligi olarak ataniyor, 3. bilyenin agirligi ise farkli olan bilye agirligi olarak ataniyor, bir adet
            # farkli bilye oldugu icin de hatali bilye sayisi 1 e esitleniyor
            elif bilye_agirlik_1 == bilye_agirlik_2:
                cogunluk_bilye_agirlik = bilye_agirlik_1
                hatali_bilye_sayisi = 1
                farkli_bilye_agirlik = bilye_agirlik_3

            # 1. ve 3. birbirine esit fakat 2. onlara esit degilse 1. ve 3. bilyenin agirlik degeri cogunluk bilye
            # agirligi olarak ataniyor, 2. bilyenin agirligi ise farkli olan bilye agirligi olarak ataniyor, bir adet
            # farkli bilye oldugu icin de hatali bilye sayisi 1 e esitleniyor
            elif bilye_agirlik_1 == bilye_agirlik_3:
                cogunluk_bilye_agirlik = bilye_agirlik_1
                hatali_bilye_sayisi = 1
                farkli_bilye_agirlik = bilye_agirlik_2

            # 2. ve 3. birbirine esit fakat 1. onlara esit degilse 2. ve 3. bilyenin agirlik degeri cogunluk bilye
            # agirligi olarak ataniyor, 1. bilyenin agirligi ise farkli olan bilye agirligi olarak ataniyor, bir adet
            # farkli bilye oldugu icin de hatali bilye sayisi 1 e esitleniyor
            elif bilye_agirlik_2 == bilye_agirlik_3:
                cogunluk_bilye_agirlik = bilye_agirlik_2
                hatali_bilye_sayisi = 1
                farkli_bilye_agirlik = bilye_agirlik_1

            # manuel olarak alinan bilyelerle cogunluk bilye agirlgi ve her durum icin hatali bilye sayisi atandiktan
            # sonra diger gelen bilye agirliklari cogunluk bilye agirligina esit gelmedikce hatali bilye sayisi 1 artiyor
            if cogunluk_bilye_agirlik != bilye_agirlik:
                hatali_bilye_sayisi += 1

            # hatali bilye sayisi 2 ye ulastiginda uretim hatasi olan kutu sayisi 1 artiriliyor, iade edilen bilye sayisi
            # kutudaki bilye sayisi kadar artiriliyor, kutuuretiminde hata oldugu bildirilip donguden cikililiyor
            if hatali_bilye_sayisi == 2:
                uretim_hatasi_olan_kutular += 1
                iade_edilen_bilye_sayisi += kutudaki_bilye_sayisi
                print("kutu uretiminde hata var")
                break

        # eger kutuda uretim hatasi yoksa breakle çıkılmıyor ve else blogune giriyor eger break ile cıkılırsa bu bloga
        # girilmeyip devam ediliyor
        else:
            print("kutunun uretiminde hata yok")

            # bu blogta 1 adet farkli olan bilye bulunan kutular kontrol ediliyor ve bildirilyor
            if hatali_bilye_sayisi == 1:
                print("kutuda bir adet farkli agirlikta bilye var")

                # eger farkli bilyenin agirligi cogunluk bilye agirligindan fazlaysa agirlik farki negatif durum
                # olusmamasi icin buyuk kucukten cikarilarak gerceklestiriliyor, bulunan farka göre ise farkin orani bulunuyor
                if farkli_bilye_agirlik > cogunluk_bilye_agirlik:
                    agir_agirlik_farki = farkli_bilye_agirlik - cogunluk_bilye_agirlik
                    fazla_agirlik_orani = agir_agirlik_farki / cogunluk_bilye_agirlik * 100

                    # agirlik farki, farkli bilyenin agirlik farki degerinden daha buyuk geldikce bu deger en buyuk agirlik
                    # farki icin ataniyor, bu agirlik farki orani ise fark en buyuk oldugunda olan oran icin ataniyor
                    # bu blokta farkli bilye cogunluk bilye agirligindan fazla olmak zorunda oldugu icin isaret agir olarak ataniyor
                    if agir_agirlik_farki > farkli_bilyenin_farki_en_buyuk:
                        farkli_bilyenin_farki_en_buyuk = agir_agirlik_farki
                        fark_en_buyuk_olunca_oran = fazla_agirlik_orani
                        isaret = "agir"

                    # agirlik farki toplam agirlik farkina agirlik farki orani ise toplam agirlik farki oranina ataniyor
                    agır_olanlar_icin_agırlık_farkı_yuzde += fazla_agirlik_orani
                    agır_olanlar_icin_agırlık_farkı += agir_agirlik_farki

                    # eger agirlik farki orani atadigim absurt deger degerinden kucuk ise bu orani absurt deger yerine,
                    # en kucuk farka o agirlik degerini, en kucuk fark oranina ise o oran ataniyor, bu blokta farkli
                    # bilyenin agirligi cogunluk bilyeden fazla oldugu icin isaret_2 degeri agir olarak ataniyor
                    if fazla_agirlik_orani <= absurt_deger:
                        absurt_deger = fazla_agirlik_orani
                        farkli_bilyenin_farki_en_kucuk = agir_agirlik_farki
                        fark_en_kucuk_olunca_oran = fazla_agirlik_orani
                        isaret_2 = "agir"

                    # bu bloktaki farkli bilye agirligi cogunluk bilye agirligindan kesinlikle fazla oldugu icin agir
                    # bilyeli kutu sayisi 1 artiriliyor
                    agır_bilyeli_kutu += 1
                    print("farkli olan bilyenin agirligi diger bilyelerden fazla")
                    print(f"agirlik farki: {agir_agirlik_farki}")
                    print(f"agirlik farkinin yuzdesi: {fazla_agirlik_orani:.2f}%")

                # eger cogunluk bilye agirligi farkli bilyenin agirligindan fazlaysa agirlik farki negatif durum
                # olusmamasi icin buyuk kucukten cikarilarak gerceklestiriliyor, bulunan farka göre ise farkin orani bulunuyor
                elif farkli_bilye_agirlik < cogunluk_bilye_agirlik:
                    hafif_agirlik_farki = cogunluk_bilye_agirlik - farkli_bilye_agirlik
                    az_agirlik_orani = hafif_agirlik_farki / cogunluk_bilye_agirlik * 100

                    # agirlik farki, farkli bilyenin agirlik farki degerinden daha buyuk geldikce bu deger en buyuk agirlik
                    # farki icin ataniyor, bu agirlik farki orani ise fark en buyuk oldugunda olan oran icin ataniyor
                    # bu blokta farkli bilye cogunluk bilye agirligindan az olmak zorunda oldugu icin isaret hafif olarak ataniyor
                    if hafif_agirlik_farki > farkli_bilyenin_farki_en_buyuk:
                        farkli_bilyenin_farki_en_buyuk = hafif_agirlik_farki
                        fark_en_buyuk_olunca_oran = az_agirlik_orani
                        isaret = "hafif"

                    # agirlik farki toplam agirlik farkina agirlik farki orani ise toplam agirlik farki oranina ataniyor
                    hafif_olanlar_icin_agırlık_farkı_yuzde += az_agirlik_orani
                    hafif_olanlar_icin_agırlık_farkı += hafif_agirlik_farki

                    # eger agirlik farki orani atadigim absurt deger degerinden kucuk ise bu orani absurt deger yerine,
                    # en kucuk farka o agirlik degerini, en kucuk fark oranina ise o oran ataniyor, bu blokta farkli
                    # bilyenin agirligi cogunluk bilyeden az oldugu icin isaret_2 degeri hafif olarak ataniyor
                    if az_agirlik_orani <= absurt_deger:
                        absurt_deger = az_agirlik_orani
                        farkli_bilyenin_farki_en_kucuk = hafif_agirlik_farki
                        fark_en_kucuk_olunca_oran = az_agirlik_orani
                        isaret_2 = "hafif"

                    # bu bloktaki farkli bilye agirligi cogunluk bilye agirligindan kesinlikle az oldugu icin hafif
                    # bilyeli kutu sayisi 1 artiriliyor
                    hafif_bilyeli_kutu += 1
                    print("farkli olan bilyenin agirligi diger bilyelerden az")
                    print(f"agirlik farki: {hafif_agirlik_farki}")
                    print(f"agirlik farkinin yuzdesi: {az_agirlik_orani:.2f}%")

            # bu blokta hatali bilye sayisi 0 olan yani butun bilyelerin esit agirlikta oldugu kutular kontrol ediliyor
            elif hatali_bilye_sayisi == 0:

                # eger tum bilyeler esit oldugu durumda olan kutulardaki bilye sayisi en cok bilyeli kutu olarak atanan
                # degerden daha fazla gelirse bu fazla gelen deger en cok bilyeli kutufaki bilye sayisi olarak ataniyor
                # o kutudaki bir bilyenin agirligi ise en cok bilye bulunan kutudaki bir bir bilyenin agirligi olarak ataniyor
                if kutudaki_bilye_sayisi > en_cok_bilyeli_kutu_butun_bilyeler_esitse_bilye_sayisi:
                    en_cok_bilyeli_kutu_butun_bilyeler_esitse_bilye_sayisi = kutudaki_bilye_sayisi
                    bir_bilyenin_agirligi = bilye_agirlik

                # tum bilyelerin esit agirlikta oldugu kutularda bir bilyenin agirligi, tum bilyelerin esit oldugu bir
                # kutudaki daha önce atanan en agir bilye agirligindan buyukse, bu kutudaki bilye sayisi en agir bilyelerin
                # bulundugu kutudaki bilye sayisi olarak, o kutudaki bilyenin agirligi ise en agir bilye olarak ataniyor
                if cogunluk_bilye_agirlik > en_agir_bilye_agirlik:
                    en_agir_bilyeler_kutu_bilye_sayisi = kutudaki_bilye_sayisi
                    en_agir_bilye_agirlik = cogunluk_bilye_agirlik

                # bu blokta tum bilyelerin agirligi esit oldugu icin tum bilyelerin esit oldugu kutu sayisi 1 artirilyor
                tum_bilyeler_esit_agirlik += 1
                print("kutudaki butun bilyelerin agirliklari eşittir")

    # kutu icin agirlik bilgileri bittikten sonra baska kutu olup olmadigi kullaniciya soruluyor
    secim = input("baska kutu var mi evet için e/E ,hayır için h/H tuslayiniz")

    # kullanicinin e,E veya h,H tuslari disinda veri girmesi durumında ayni soru tekrar soruluyor
    while secim != "e" and secim != "E" and secim != "h" and secim != "H":
        secim = input("hatali bir veri girdiniz lutfen evet icin e/E, hayir icin h/H tuslarini tuslayiniz")

# genel istatistik bilgileri icin yapılan matematiksel islemler
uretim_hatali_kutu_orani = uretim_hatasi_olan_kutular / tum_kutular * 100
kabul_edilen_bilyeler = tum_bilyeler - iade_edilen_bilye_sayisi
uretim_hatasi_olmayan_kutular = tum_kutular - uretim_hatasi_olan_kutular
esit_agirlikli_bilye_kutu_orani = tum_bilyeler_esit_agirlik / uretim_hatasi_olmayan_kutular * 100
hafif_agirlikli_bilye_kutu_orani = hafif_bilyeli_kutu / uretim_hatasi_olmayan_kutular * 100
agir_agirlikli_bilye_kutu_orani = agır_bilyeli_kutu / uretim_hatasi_olmayan_kutular * 100
agir_olanlar_icin_fark_ort = agır_olanlar_icin_agırlık_farkı / agır_bilyeli_kutu
agir_olanlar_icin_fark_yuzde_ort = agır_olanlar_icin_agırlık_farkı_yuzde / agır_bilyeli_kutu
hafif_olanlar_icin_fark_ort = hafif_olanlar_icin_agırlık_farkı / hafif_bilyeli_kutu
hafif_olanlar_icin_fark_yuzde_ort = hafif_olanlar_icin_agırlık_farkı_yuzde / hafif_bilyeli_kutu

print(f"üretim hatasi olan kutu sayisi: {uretim_hatasi_olan_kutular}   uretim hatasi olan kutularin tum kutulardaki yuzdesi: {uretim_hatali_kutu_orani:.2f}%")
print(f"kabul edilen bilyes sayisi: {kabul_edilen_bilyeler}   iade edilen bilye sayisi: {iade_edilen_bilye_sayisi}")
print(f"tum bilyelerin esit agirlikta oldugu kutu sayisi: {tum_bilyeler_esit_agirlik}")
print(f"tum bilyelerin esit agirlikta oldugu kutu sayisinin uretim hatasi olmayan kutulardaki yuzdesi: {esit_agirlikli_bilye_kutu_orani:.2f}%")
print(f"bir bilyenin diger bilyelerden daha agir oldugu kutu sayisi: {agır_bilyeli_kutu}")
print(f"bir bilyenin agir oldugu kutularin uretim hatasi olmayan kutulardaki orani {agir_agirlikli_bilye_kutu_orani:.2f}%")
print(f"bir bilyenin digerlerinden daha hafif oldugu kutu sayisi: {hafif_bilyeli_kutu}")
print(f"bir bilyenin hafif oldugu kutularin uretim hatasi olmayan kutulara orani: {hafif_agirlikli_bilye_kutu_orani:.2f}%")
print(f"bir bilyenin digerlerinden daha agir oldugu kutulardaki agır olan bilyenin agırlık farkı ortalaması: {agir_olanlar_icin_fark_ort:.2f} mg")
print(f"bir bilyenin digerlerinden daha agir oldugu kutulardaki agir olan bilyelerin agirlik farki yuzdesi ortalamasi: {agir_olanlar_icin_fark_yuzde_ort:.2f}%")
print(f"bir bilyenin digerlerinden daha hafif oldugu kutulardaki hafif olan bilyenin agırlık farkı ortalaması: {hafif_olanlar_icin_fark_ort:.2f} mg")
print(f"bir bilyenin digerlerinden daha hafif oldugu kutulardaki hafif olan bilyelerin agirlik farki yuzdesi ortalamasi: {hafif_olanlar_icin_fark_yuzde_ort:.2f}%")
print(f"tum bilyelerin esit agirlikta oldugu kutular arasinda icinde en cok bilye bulunan kutudaki bilye sayisi: {en_cok_bilyeli_kutu_butun_bilyeler_esitse_bilye_sayisi}")
print(f"tum bilyelerin esit agirlikta oldugu kutular arasinda icinde en cok bilye bulunan kutudaki bir bilyenin agirligi: {bir_bilyenin_agirligi} mg")
print(f"tum bilyelerin esit agirlikta oldugu kutular arasinda icinde en agir bilyeler olan kutudaki bilye sayisi: {en_agir_bilyeler_kutu_bilye_sayisi}")
print(f"tum bilyelerin esit agirlikta oldugu kutular arasinda icinde en agir bilyeler olan kutudaki bir bilyenin agirligi: {en_agir_bilye_agirlik} mg")
print(f"farkli olan bilyenin agirliginin kutudaki diger bilyelerle arasindaki agirlik farki en buyukken agirlik farki: {farkli_bilyenin_farki_en_buyuk} mg {isaret}")
print(f"farkli olan bilyenin agirliginin kutudaki diger bilyelerle arasindaki agirlik farki en buyukken agirlik farki orani: {fark_en_buyuk_olunca_oran:.2f}%")
print(f"farkli olan bilyenin agirliginin kutudaki diger bilyelerle arasindaki agirlik farki en kucukken agirlik farki: {farkli_bilyenin_farki_en_kucuk} mg {isaret_2}")
print(f"farkli olan bilyenin agirliginin kutudaki diger bilyelerle arasindaki agirlik farki en kucukken agirlik farki orani: {fark_en_kucuk_olunca_oran:.2f}%")