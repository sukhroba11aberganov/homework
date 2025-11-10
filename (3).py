# append() Roʻyxat oxiriga element qoʻshadi

cars = []
cars.append('BMW')
cars.append('Lomborgini')
cars.append('Bugatti')
cars.append('Tahoe')
print(cars)

fruits = []
fruits.append('olma')
fruits.append('banan')
fruits.append('apelsin')
fruits.append('anor')
print(fruits)

# clear() Ro‘yxatdagi barcha elementlarni o‘chiradi

shaxarlar = ['Toshkent', 'Urganch', 'Samarqand', 'Xiva']
shaxarlar.clear()
print(shaxarlar)

numbers = [1, 20, 8000, 51132, 2623]
numbers.clear()
print(numbers)

# copy() Ro‘yxatning nusxasini qaytaradi

kampaniyalar = ['HP', 'Lenova', 'Acer', 'Apple']
salom =  kampaniyalar.copy()
print(salom)

viloyatlar = ['Xorazm', 'Toshkent', 'Buxoro', 'Samarqand']
volt =  viloyatlar.copy()
print(volt)

# count() Belgilanmagan qiymatga ega elementlar sonini qaytaradi

jamoalar = ['REAL MADRID', 'PSG', 'barcelona', 'Liverpol', 'Milan']
jma =  jamoalar.count('REAL MADRID')
print(jma)

ismlar = ['Asror', 'Abror', 'Ali', 'Vali']
imyi = ismlar.count('Ali')
print(imyi)

# extend() Joriy ro‘yxat oxiriga ro‘yxatning (yoki har qanday takrorlanadigan obyektning) elementlarini qo‘shing

ismlar_1 = ['Samir', 'Amir', 'Ali', 'Vali']
ismlar_2 = ['Rasul', 'Mansur', 'Xolmurod', 'Dilmurod']
ismlar_1.extend(ismlar_2)
print(ismlar_1)

moshinalar = ['matiz', 'nexia 2', 'damas']
moshinalar_2 = ['malibu', 'onix', 'cobalt']
moshinalar.extend(moshinalar_2)
print(moshinalar)

# index() Belgilanadigan qiymatga ega birinchi elementning indeksini qaytaradi

mevalar = ['olma', 'anor', 'apelsin']
a = mevalar.index('anor')
print(a)

kampyuterlar = ['HP', 'acer', 'lenova']
b = kampyuterlar.index('HP')
print(b)

# insert() Belgilar berilgan pozitsiyaga element qo‘shadi

kurslar = ['foundation', 'frontend', 'grafik dizayn']
kurslar.insert(0, 'backend')
print(kurslar)

oylar = ['yanvar', 'fevral', 'aprel']
oylar.insert(2, 'mart')
print(oylar)

# pop() Ko‘rsatilgan pozitsiyadagi elementni o‘chiradi

appliances = ['muzlatkich', 'kir moshinasi', 'qozon']
appliances.pop(2)
print(appliances)

programming_languages = ['Python', 'JavaScript', 'telefon', 'CSS']
programming_languages.pop(2)
print(programming_languages)

# remove() Ko‘rsatilgan qiymatga ega bo‘lgan elementni o‘chiradi

davlatlar = ['UZB', 'RUS', 'ENG', 'xorazm']
davlatlar.remove('xorazm')
print(davlatlar)

viloyatlar_2 = ['Xoraz', 'ENG', 'Toshkent', 'Samarqand']
viloyatlar_2.remove('ENG')
print(viloyatlar_2)

# reverse() Ro‘yxat tartibini teskari aylantiradi

cars_2 = ['malibu', 'bmw', 'lomborgini']
cars_2.reverse()
print(cars_2)

saytlar = ['uzum', 'kun.uz', 'tiktok']
saytlar.reverse()
print(saytlar)

# sort() Roʻyxatni tartiblaydi

harflar = ['c', 'e', 'a', 'b', 'd']
harflar.sort()
print(harflar)

avtomabil = ['tahoe', 'captiva', 'tico', 'damas', ]
avtomabil.sort()
print(avtomabil)