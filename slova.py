import random

suglasnici = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","w","x","y","z","1","3","5","7","9"]

def vrati(n):
    lista = []
    for i in range(n):
        x = ""
        for i in range(5):
            x = x + random.choice(suglasnici)

        lista.append(x)
    return lista

n = int(input())
list1 = vrati(n)
list2 = vrati(n)
print(list1)
print(list2)


nema = ""
for x in list1:
    for i in x:
        if list2.__contains__(i):
            continue
        else:
            nema = nema + i

print("riječ:" + nema)