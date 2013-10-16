#1. Поиск позиции элемента в двумерном массиве
def find_pos(arr,elem):
    p = -1
    for i in range(len(arr)):
        if arr[i][0] == elem:
            p = i
    return p

#2. Сформировать алфавит строки
#3. Сортировка двумерного массива по частоте
def sort_freq(arr):
    for i in arr:
        for j in range(len(arr)-1):
            if arr[j][1]<arr[j+1][1]:
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t
    return arr

#4. Преобразование в bin из dec
def to_bin(dec,l):
    s = ""
    while dec>0:
        p = int(dec % 2)
        dec = int(dec/2)
        s = str(p)+s
    while len(s)<l:
        s = "0"+s
    return(s)

st = input("Введите строку: ")
#преобразование в строчные
st=st.lower()

mas = [[st[0],0]]
for i in st:
    t = find_pos(mas,i)
    if t<0:
        mas.append([i,1])
    else:
        #если позиция была найдена, то увеличить частоту
        mas[t][1] += 1

print(mas)
mas = sort_freq(mas)

k = [0,0,0,0,0,0]
for i in range(len(mas)):
    if i<2:
        mas[i].append(to_bin(k[0],1))
        k[0] +=1
    if i>=2 and i<6:
        mas[i].append(to_bin(k[1],2))
        k[1] +=1
    if i>=6 and i<14:
        mas[i].append(to_bin(k[2],3))
        k[2] +=1
    if i>=14 and i<30:
        mas[i].append(to_bin(k[3],4))
        k[3] +=1
    if i>=30 and i<62:
        mas[i].append(to_bin(k[4],5))
        k[4] +=1

for i in range(len(mas)):
    print(mas[i][0]+" "+str(mas[i][1])+" "+str(mas[i][2]))

#st_h - строка результата
#l_st - длина результатной строки без пробелов
st_h = ""
l_st = 0
for i in st:
    t = find_pos(mas,i)
    l_st += len(mas[t][2])
    st_h = st_h + str(mas[t][2])+" "

#расчёт коэффициента
koef = (8*len(st))/l_st
print(st_h+" "+str(koef))
