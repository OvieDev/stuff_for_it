import random
lista = random.sample(range(1,1000), 100)
lista.sort()
for i in range(20):
    print(lista[i])