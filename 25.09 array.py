#определение массива
a = []

import random
import array

#функция
def func(arr = "",i = 1,elem = 1):
    print("YOOOUUUO")
    status = 0
    for k in range(i):
        if arr[k] == elem:
            status = 1
            break
    return status

#генерация массива рандомными числами без повторения
for i in range(15):
    rnd = random.randrange(0,100)
    if i>0:
        while func(a,i,rnd) == 1:
            rnd = random.randrange(0,100)
        a.append(rnd)
    else:
        a.append(rnd)
print(a)

#сортировка пузырьком
for k in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            t = a[i+1]
            a[i+1] = a[i]
            a[i] = t
print(a)
