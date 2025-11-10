##1-topshiriq
# salom = input("Elektron pochta kiriting, (@)< shu belgi bo'lsin: ")
# emaillar = salom.split(",")  # split() berilgan belgi bo‘yicha matnni bo‘lib, ro‘yxat (list) qaytaradi
# for email in emaillar:
#     print(email)
#     if "@" in email:
#         print("Qabul qilindi:", email)
#     else:
#         print("'@' belgisi yo'q:", email)

##2-topshiriq
# qwe = input("8ta belgidan ko'proq parol kiriting: ")
# parol = qwe.split(",")
# for qwe in parol:
#     if len(qwe) < 8:
#         print(parol, "-> Juda qisqa")
#     else:
#         print(parol, "-> Kuchli parol")
#
##3-topshiriq
# temperature = []
# for i in range(7):
#     temp = float(input(f"{i+1}- haroratni kiriting>>>:"))
#     temperature.append(temp)
# for h, temp in enumerate(temperature, start=1):   #enumerate() - bu sikl (for) ichida elementning tartib raqami (indeksi) bilan o‘sha elementning o‘zini birgalikda olish uchun ishlatiladi.
#     if temp > 22:
#         print(f"{h}: {temp} ILIQ KUN!")
#     else:
#         print(f"{h}: {temp} SALQIN KUN!")
##4-topshiriq
# mavjudlar = ["Manti", "Somsa", "Chuchvara", "Lag'mon", "Norin", "Hotdog", "Osh"]
# print("mavjud bo'lgan taomlar: ", mavjudlar)
# qwert = input("Qanday taom buyurtma bermoqchisiz? ")
# for qwe in mavjudlar:
#     if qwert.lower() == qwe.lower():
#         print("Buyurtmangi 5 daqiqada tayor bo'ladi!")
#         break
# else:
#     print("mavjud emas")
#
##5-topshiriq
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh>=18:
#     print('Xush kelibsiz!')
# else: # ask holda
#     print('Yosh chegarasiga yetmagan')

##6-topshiriq
# xabarlar = ["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
# for xabar in xabarlar:
#     if xabar == "Batareya past":
#         print("Telefoningizni quvvatlang")
# for qwerty in xabarlar:
#     if qwerty == "Yangi xabar":
#         print("Xabarangizni aytishiningiz mumkin!")
# for ewq in xabarlar:
#     if ewq == "Yangilanish mavjud":
#         print("Ajoyib!")

##7-topshiriq
# fayllar = ["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
# mp3 = []
# jpg = []
# for top in fayllar:
#     if top.find(".mp3") != -1:
#         mp3.append(top)
#     elif top.find(".jpg") != -1:
#         jpg.append(top)
# print("mp3 lar:", mp3)
# print("jpg:", jpg)
