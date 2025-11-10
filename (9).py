# add() -- To'plamga element qo'shadi
moshinalar = {"BMW", "mers", "Damas", "Matiz", "Locetty"}
moshinalar.add("cobalt")
print(moshinalar)

tel_lar = {'iphone', 'redmi', 'honor', 'samsung'}
tel_lar.add("infinix")
print(tel_lar)

# clear() hammasini o'chiradi
shaharlar = {'Urganch', 'Toshkent', 'Xiva'}
shaharlar.clear()
print(shaharlar)

mevalar = {'olma', 'anor', 'olcha', 'banan'}
mevalar.clear()
print(mevalar)

# copy() To'plamning nusxasini qaytaradi
ismlar = {'Ali', 'Ravshan', 'Vali', 'og\'abek'}
ismlar.copy()
print(ismlar)

sonlar = {12, 77, 00, 1}
sonlar.copy()
print(sonlar)

# difference() Ikki yoki undan ortiq to'plam orasidagi farqni o'z ichiga olgan to'plamni qaytaradi
vil = {"Xorazm", "Samarqand", "Surxondaryo", "Toshkent"}
shah = {"Samarqand", "Toshkent", "Urganch", "Nukus"}
qwe = vil.difference(shah)
print(qwe)

son_1 = {1, 23, 45, 77, 7}
son_2 = {23, 7, 45, 777, 0}
son_3 = son_1.difference(son_2)
print(son_3)

# discard() ko'rstailgan narsani o'chiradi
kampanyialar = {"Limon", "Uzinfocom", "HP"}
kampanyialar.discard("HP")
print(kampanyialar)

kamandalar = {"REAL MADRID", "Liverpool", "barcelona", "Man city"}
kamandalar.discard("barcelona")
print(kamandalar)

# intersection() Ikkita boshqa to'plamning kesishmasi bo'lgan to'plamni qaytaradi
mevalar = {"olma", "kivi", "nok", "apelsin"}
mevalar_2 = {"kivi", "mandarin", "apelsin", "uzum"}
mevalar_3 = mevalar.intersection(mevalar_2)
print(mevalar_3)

number = {32, 7, 0, 94, 78}
number_2 = {7, 90, 78, 0, 777}
number_3 = number.intersection(number_2)
print(number_3)

#intersection_update() Ushbu to'plamdagi boshqa,
# ko'rsatilgan to'plam(lar)da mavjud bo'lmagan elementlarni olib tashlaydi
darslar = {"matematika", "adabiyot", "ingliz tili", "informatika"}
darslar_2 = {"ona tili", "ingliz tili", "rus tili"}
darslar.intersection_update(darslar_2)
print(darslar)

a = {"kampyuter", "stol", "stul"}
b = {"gilam", "soat", "stol"}
a.intersection_update(b)
print(a)

#isdisjoint() Ikki to'plamning kesishishi bor yoki yo'qligini qaytaradi
saytlar = {"google", "youtube", "facebook", "twitter"}
saytlar_2 = {"Wikipedia", "yandex", "yahoo"}
saytlar_3 = saytlar.isdisjoint(saytlar_2)
print(saytlar_3) #True

kurslar = {"backend", "frontend", "foundation"}
kurslar_2 = {"mobilagrafiya", "frontend", "kampyuter s"}
kurslar_3 = kurslar.isdisjoint(kurslar_2)
print(kurslar_3) #Falce

#issubset() Agar bu to‘plamdagi barcha elementlar boshqa to‘plamda mavjud bo‘lsa, True qaytaradi
oylar = {"yanvar", "mart", "may"}
oylar_2 = {"yanvar", "fevral", "mart", "aprel", "may"}
oylar_3 = oylar.issubset(oylar_2)
print(oylar_3) #True

n = {23, 1, 4, 3, 2, 6}
n_2 = {1, 2, 3, 4, 5, 6}
n_3 = n.issubset(n_2)
print(n_3) #Falce

#pop() To'plamdan elementni olib tashlaydi
colors = {"red", "green", "blue", "orange"}
colors.pop()
print(colors)

davlatlar = {"O'zbekiston", "Rossia", "Ispania"}
davlatlar.pop()
print(davlatlar)

#remove() Ko'rsatilgan elementni olib tashlaydi

fruits = {"apple", "orange", "peach"}
fruits.remove("orange")
print(fruits)

nomer = {21, 7, 0, 00}
nomer.remove(00)
print(nomer)

#symmetric_difference() Ikkita to'plamning simmetrik farqlari bilan to'plam qaytaradi
a = {"iphone", "samsung", "olma"}
f = {"infinix", "poco", "olma"}
t = a.symmetric_difference(f)
print(t)

cars = {"bmw", "ferrari", "mers",}
cars_2 = {"malibu", "damas", "cobalt", "mers"}
cars_3 = cars.symmetric_difference(cars_2)
print(cars_3)

#symmetric_difference_update() Ushbu to'plam va boshqa to'plamdan simmetrik farqlarni kiritadi
kunlar = {"dushanba", "chorshanba", "payshanba"}
kunlar_2 = {"dushanba", "seshanba", "juma", "shanba"}
kunlar.symmetric_difference_update(kunlar_2)
print(kunlar)

qwe = {"soat", "meva", "shim", "klaviatura"}
qwe2 = {"meva", "mishka", "ekran", "monitor"}
qwe.symmetric_difference_update(qwe2)
print(qwe)

#union() To'plamlar birlashmasini o'z ichiga olgan to'plamni qaytaradi
o = {"osh", "ochiq", "olma"}
o2 = {"osh", "somsa", "shokolad"}
o3 =  o.union(o2)
print(o)

asd = {"ismlar", "rashid", "ali", "vali"}
asd_2 = {"ismlar", "abu", "baxti", "shoxjaxon"}
qwer =  asd.union(asd_2)
print(qwer)

#update() Bu to'plamni ushbu to'plam va boshqalar yig'indisi bilan yangilang
qw = {"apple", "banana", "cherry"}
fg = {"google", "microsoft", "apple"}
qw.update(fg)
print(qw)

harflar = {"a", "b", "c"}
harflar_2  = {"d", "e", "c", "f"}
harflar.update(harflar_2)
print(harflar)
