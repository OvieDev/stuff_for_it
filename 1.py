promien = float(input("Podaj promien: "))
if promien>=0:
    pole = 3.14*promien**2
    obwod = 2 * 3.14 * promien
    print(f"pole: {pole}")
    print(f"obwod: {obwod}")
else:
    print("Liczba jest ujemna!")

