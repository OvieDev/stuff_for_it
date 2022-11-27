import random
lista = random.sample(range(1,1000), 100)
parzyste = []
nieparzyste = []
for i in lista:
    if i % 2 == 0:
        parzyste.append(i)
    else:
        nieparzyste.append(i)

print(f"Parzyste: {len(parzyste)}")
print(f"Nieparzyste: {len(nieparzyste)}")