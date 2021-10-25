a = 1 #szorzótábla
b = 1 #-ik elem
c=0
szorzotabla=[1,2,3,4,5,6,7,8,9,10]
kiiras=[]

while b <= 10:
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        c = i*b
        kiiras.append(c)
    print(kiiras)
    b+=1
    kiiras=[]





