# №1
def summa(*qwe):
    """Sonlarni ko'paytmasini hisoblaydigan funksiya"""
    qwerty = 1
    for asd in qwe:
        qwerty *= asd
    return qwerty
print(summa(1, 30))

# №2
def talabalar(ism,familiya,**boshqa_malumotlar):
    boshqa_malumotlar["ism"]=ism
    boshqa_malumotlar["familiya"]=familiya
    return boshqa_malumotlar
talaba_1=talabalar("Rajabboy","Adilbekov",yil=2010,yashash_manzil="urganch")
talaba_2=talabalar("Akrom","Sodikov",yil=2010,yashash_manzil="urganch")
print(talaba_1,talaba_2)

