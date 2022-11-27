import random
liczba = random.randint(0, 10)

while True:
    odpowiedz = input("Zgadnij liczbe: ")
    if int(odpowiedz)==liczba:
        print("Poprawny wynik!")
        break
    else:
        print("Spróbuj jeszcze raz")
#

#
# # for i in range(10,99):
# #     s = ""
# #     for j in range(i + 1):
# #         s += str(i + 1)
# #     print(s)
#
# # import random
# # lista = random.sample(range(1, 1000), 100)
# #
# # for i in lista:
# #     if str(i).find("21")!=-1:
# #         print(i)
#
# # trzycyfrowe = 0
# #
# # for i in lista:
# #     if len(str(i))==3:
# #         trzycyfrowe+=1
# #
# # print(trzycyfrowe)
#
# #
#
# import random
# lista = random.sample(range(1,1000), 100)
#
# def klucz(wartosc):
#   return -wartosc
#
# parzyste = []
# nieparzyste = []
# for i in lista:
#     if i % 2 == 0:
#         parzyste.append(i)
#     else:
#         nieparzyste.append(i)
#
# parzyste.sort()
# nieparzyste.sort(key=klucz)
# parzyste.extend(nieparzyste)
# print(parzyste)
# # lista.sort()
# # for i in range(20):
# #     print(lista[i])
#
#
# # nieparzyste = 0
# # for i in lista:
# #     if i % 2 != 0:
# #         nieparzyste+=1
# # print(nieparzyste)
#
# # minimum = int(input("Podaj początek przedziału: "))
# # maximum = int(input("Podaj koniec przedziału: "))
# # wynik = []
# # for i in lista:
# #     if i>minimum and i<maximum:
# #         wynik.append(i)
# #
# # print(wynik)
#
# # parzyste = []
# # nieparzyste = []
# # for i in lista:
# #     if i % 2 == 0:
# #         parzyste.append(i)
# #     else:
# #         nieparzyste.append(i)
# #
# # parzyste.sort()
# # nieparzyste.sort(key=lambda x: -x)
# # parzyste.extend(nieparzyste)
# # print(parzyste)
# #
# # def funkcja(argument):
# #     print(argument)
# import requests
# r = requests.get("http://165.227.106.113/header.php", headers={"User-Agent": "Sup3rS3cr3tAg3nt", "Referer": "awesomesauce.com"})
# print(r.status_code)
# print(r.headers)
# print(r.content)

a = int(input("podaj liczbe: "))
print("Liczba ta, sklada sie z: "+str(len(str(a)))+" cyfr")
suma = 0
for i in str(a):
    suma+=int(i)

print("Suma cyfr wynosi: " + str(suma))

c = float(input("podaj stopnie celsjusza: "))
if c>0:
    print(str(c+273)+" w stopniach kelwina")

for i in range(1,100):
  if i%2==0 and i%3==0:
    print(i)

imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")

litery_z_imienia = imie[0:2]
litery_z_nazwiska = nazwisko[0:2]

a = input("podaj miesiąc: ").lower()

if a=="grudzien" or a=="styczen" or a=="luty":
    print("Mamy zimę!")
elif a=="marzec" or a=="kwiecen" or a=="maj":
    print("Mamy wiosnę!")
elif a=="czerwiec" or a=="lipiec" or a=="sierpien":
    print("Mamy lato!")
elif a=="wrzesien" or a=="pazdziernik" or a=="listopad":
    print("Mamy jesień")