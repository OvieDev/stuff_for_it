import random
lista = random.sample(range(1, 1000), 100)

for i in lista:
    if str(i).find("21")!=-1:
        print(i)