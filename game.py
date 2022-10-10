import random
n = random.randint(4,30)
print("Chsilo kamney =", n)
flag = 0
while n > 1:
    if flag % 2 == 0:
        print('Введите количество камней, которое вы возьмёте:')
        p = int(input())
        if p == 1: n -= 1
        elif p == 2: n -= 2
        else: n -= 3
    else:
        c = random.randint(1,3)
        print('Робот возьмет камней = ', c)
        n -= c
    flag += 1
    print('Количество оставшихся камней = ', n)
if flag%2 == 1: print('Победа пользователя')
else: print('Победа робота')

