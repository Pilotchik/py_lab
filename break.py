#операция выхода из итерации
#break

#символы с a до z [97-122]

s = input("Введи строку: ")

end = 0
i = 0
for a in range(97,123):
    for b in range(97,123):
        s_new = chr(a) + chr(b)
        print(s_new)
        if s_new == s:
            print(i)
            end = 1
            break
        i+=1
    if end == 1:
        break
print(i)
