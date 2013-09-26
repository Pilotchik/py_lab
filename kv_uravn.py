# -*- coding: cp1251 -*-
#Python 3.3

import math

#Функция нахождения корня
def kv_ur(a,b,d,znak):
    if znak>0:
        x = (-b+math.sqrt(d))/(2*a)
    else:
        x = (-b-math.sqrt(d))/(2*a)
    return x

cmd = 1
while cmd<>0:
    a = float(input("Введите параметр а: "))
    b = float(input("Введите параметр b: "))
    c = float(input("Введите параметр c: "))
    d = b*b - 4*a*c
    if d<0:
        print("Решений нет")
    else:
        x1 = kv_ur(a,b,d,1) 
        x2 = kv_ur(a,b,d,0)
        x1 = str(x1)
        x2 = str(x2)
        print("Решение 1: "+x1+" Решение 2: "+x2)
    cmd = input("Введите 0, чтобы завершить: 1 - чтобы продолжить")
    cmd = int(cmd)
