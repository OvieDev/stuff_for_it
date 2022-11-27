import random
lista = random.sample(range(1,1000), 100)
wynik = 0
for i in lista:
    if i>800:
        wynik+=1

print(wynik)