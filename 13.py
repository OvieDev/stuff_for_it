import random
lista = random.sample(range(1,1000), 100)
wynik = 1
for i in lista:
  wynik *= i
print(wynik)