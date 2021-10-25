a1 = int(input("Add meg a mértani sorozat első elemét: "))
a2 = int(input("Add meg a mértani sorozat második elemét: "))
n = int(input("Hányadik elemet szeretnéd megkapni?: "))

q = a2 / a1
an = a1*(q**(n-1))
print(an)
