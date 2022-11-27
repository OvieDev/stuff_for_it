import random
lista = random.sample(range(1,1000), 100)
minimum = int(input("Podaj początek przedziału: "))
maximum = int(input("Podaj koniec przedziału: "))
wynik = []
for i in lista:
    if i>minimum and i<maximum:
        wynik.append(i)

print(wynik)