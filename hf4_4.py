bekert_szöveg = input("Írjon be egy szöveget: ")
i = 0
j = 1
lista=[]
a = 'False'

while i < (len(bekert_szöveg)//2):
    if bekert_szöveg[i] == bekert_szöveg[len(bekert_szöveg)-j]:
        lista.append('True')
        i+=1
        j+=1
    else:
        lista.append('False')
        i+=1
        j+=1
if a in lista:
    print("Ez nem palindrom. ")
if a not in lista:
    print("Ez palindrom. ")