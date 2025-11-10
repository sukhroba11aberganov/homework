# capitalize()	gapning birinchi harifini katta harfga aylantiradi

print(f"men lenova kampaniyasidan noutbuk sotib oldim".capitalize())
print(f"я купил ноутбук у компании 'Lenovo' ".capitalize())
print(f"I bought a laptop from the 'Lenovo' company".capitalize())

# casefold()  qatorni kichik harfga aylantiradi

print(f"PYTHON BU KATTA DASTURLASH TILI".casefold())
print(f"PYTHON — ЭТО ЯЗЫК ПРОГРАММИРОВАНИЯ".casefold())
print(f"PYTHON IS A GREAT PROGRAMMING LANGUAGE".casefold())

# count()   Belgilangan qiymat satrda necha marta sodir bo'lishini aytadi

print(f"IT park xorazm, xorazmda joylashgan".count("xorazm"))
print(f"hozirda ko'p odamlar IT sohasini tanlamoqda, chunki IT hozir kuchli rivojlanmoqda".count("IT"))
print(f"real madrid erkaklar jamoasi, qisqasi 'hala madrid😎'".count("madrid"))

# encode()   Satrdan shifrlangan versiyasini qaytaradi

print(f"Salom mening ismim 'Suhrob'".encode())
print(f"Hello world".encode())
print(f"Satrdan shifrlangan versiyasini qaytaradi".encode())

# endswith() Agar satr belgilangan qiymat bilan tugasa, true qaytaradi

print(f"men 26-oktyabr kuni shu jamoaga muhlislik qilaman bu jamoa: (REAL MADRID)".endswith('REAL MADRID'))
# print(f"")
# print(f"")

# expandtabs() Satrdagi tab o'lchamini belgilaydi

print(f"assalomu alaykum, yaxshimisiz".expandtabs())
print(f"siz     yoshdamisiz?".expandtabs())
print(f"Satrdagi    tab     o'lchamini belgilaydi".expandtabs())

# find() Satrdan ma'lum qiymatni qidiradi va topilgan joyini qaytaradi

print(f"Assalomu alaykum kuningiz 'xayrli' o'tsin".find('xayrli'))
print(f"katta dasturlash tillaridan biri bu python".find('python'))
print(f"moshinangizni nomi nima".find('moshinangizni'))

# format()  Qator ichidagi qiymatlarni belgilangan formatda chiqaradi

volt = "For only {price:.2f} uzs!"
print(volt.format(price = 100_000))
salom = "bu kampyuterimiz {price:.2f} uzs!"
print(salom.format(price = 6_000_000))
_3_ = "siz {price:.2f} uzs yutib oldingiz!"
print(_3_.format(price = 150_000))

# index() Satrdan ma'lum qiymatni qidiradi va topilgan joyini qaytaradi

print(f"salom mening ismim 'Suhrob'".index('Suhrob'))
print(f"sizning ismingiz kim".index('ismingiz'))
print(f"Satrdan ma'lum qiymatni qidiradi".index('qiymatni'))

# isalnum() Agar matndagi barcha belgilar alfanumerik bo'lsa, True qaytaradi

text = "Temur530"
text2 = text.isalnum()
print(text2) #true

text3 = "IT park xoram"
text4 = text3.isalnum()
print(text4)  #false

# isalpha() Agar satrdagi barcha belgilar alifboda bo'lsa, True qaytaradi

salom = "ITparkXoram"
qwer = salom.isalpha()
print(qwer)
print("Salom".isalpha())
print("Salom qalaysan".isalpha()) #false

# isascii() Agar matndagi barcha belgilar ASCII (Amerika axborot almashinuvi uchun standart kod)
# belgilar bo'lsa, True qiymatini qaytaradi

print("ushbu telefonni paroli 'salom123'".isascii())
print("bugun maktabga borasanmi?".isascii())
print(" _ ".isascii())

# isdecimal() Agar satrdagi barcha belgilar o'nlik raqam bo'lsa, True qaytaradi

print("salom123".isdecimal()) #so'z qatnashgani uchun false
print('123'.isdecimal()) #qatnashmagani uchun true

# isdigit() Agar satrdagi barcha belgilar raqam bo'lsa True qaytaradi

print("2011-yil".isdigit()) #falce
print("2011".isdigit())
print("0".isdigit())

# islower() Agar matndagi barcha belgilar kichik harf bo'lsa, True qaytaradi

print("assalomu alaykum o'zbekiston ahli".islower()) #t
print("Assalomu alaykum O'zbekiston ahli".islower()) #f
print("Asssalomu alaykum".islower(), "assalomu alaykum".islower())

# isnumeric() Agar stringdagi barcha belgilar raqam bo'lsa, True qaytaradi

print("1234567".isnumeric())
print("a123456".isnumeric())
print("123456765432".isnumeric())

# isprintable() Agar satrdagi barcha belgilar chop etilishi mumkin bo'lsa, True qiymatini qaytaradi

print("abcd, !@#$%^&, 1234567".isprintable())
print("bu telning narxi 300$".isprintable())
print("salom@gmail.com".isprintable())

# isspace() Agar matndagi barcha belgilar bo'sh joy bo'lsa, True qaytaradi

print("         ".isspace()) #t
print("salom".isspace()) #f
print("s a l o m".isspace()) #f

# istitle() Agar matn sarlavha qoidalariga amal qilsa, True qaytaradi

print("Salom mening Youtube kanalimga xush kelipsiz!".istitle()) #f
print("Salom Mening Youtube Kanalimgha Xush Kelipsiz!".istitle()) #t
print("Salom @ $".istitle()) #t

# isupper() Agar matndagi barcha belgilar katta harf bo'lsa, True qiymatini qaytaradi

print("HELLO WORLD".isupper()) #t
print("Hello World".isupper()) #f
print("ASSALOMU ALAYKUM".isupper()) #t

 # join() Takrorlanadigan elementlarni stringning oxiriga qo'shadi

ismlar = ("ali", "vali", "dali")
a = "@".join(ismlar)
print(a)

# ljust() Qatorning chapga tekislangan versiyasini qaytaradi

print("python".ljust(20), "katta dasturlash tili")
print("olma".ljust(30), "shirin meva")
print("bahodir".ljust(40), "qalaysan")

# lower() Matnni kichik harflarga o'zgartiradi

print("HELLO WORLD".lower())
print("Hello World".lower())
print("SALOM DUNYO".lower())

# lstrip() Qatorning chap tomondan kesilgan versiyasini qaytaradi

print("   salom   dunyo".lstrip())
print("                      salom      xorazm".lstrip())
print("   hello world".lstrip())

# maketrans() Tarjima qilishda ishlatiladigan tarjima jadvalini qaytaradi

sal = "pythmn!"
salo = str.maketrans("m", "o")
print(sal.translate(salo))

# partition() Matnni uch qismga bo‘ladigan tuple qaytaradi

print("men olmani yaxshi koraman".partition('yaxshi'))
print("HP kampaniasi lenova kampaniyasi acer kampaniyasi".partition('lenova kampaniyasi'))
print("olma anor anjir".partition('anor'))

# replace() Belgilanadigan qiymatni boshqa belgilanadigan qiymat bilan almashtiradigan satrni qaytaradi

print("mening kampyuterimni kampaniyasini nomi 'acer'".replace('acer', 'HP'))



# rfind() Belgilangan qiymatni matnda qidiradi va topilgan oxirgi joyini qaytaradi

print("men 'HP' kampaniyasidan kampyuter sotib oldim". rfind('HP'))
print("salom ")











