import random
print("Unesi granice")
x = int(input())
y = int(input())
if(x>y):
    x,y=y,x
r = random.randint(x,y)
guess = y+1
pokusaji = 0
while guess != r:
    pokusaji += 1
    guess = int(input("Pogodi "))
    if guess>r:
        print("Prevelik broj")
    if guess < r:
        print("Premalen broj")
    if guess == r:
        print("Točno,pogodio/la si u",pokusaji,"pokusaja")
        break