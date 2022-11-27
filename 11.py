slowo = input("Podaj słowo: ")
nslowo = ""
for i in slowo:
    nslowo = i+nslowo
if nslowo==slowo:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")