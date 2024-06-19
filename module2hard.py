a = int(input('Ввести число : '))

list_1 = [1, 2, 3 ,4 ,5 ,6 ,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_2 = [1, 2, 3 ,4 ,5 ,6 ,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
password = []

for i in range(len(list_1)):
    if list_1 == list_1[i]:
        continue
    for j in range(list_1[i], len(list_2)):
        if list_1[i] == list_2[j]:
            continue
        if list_1 == list_2[j]:
            continue
        if a % (list_1[i] + list_2[j]) == 0:
            password.append(list_1[i])
            password.append(list_2[j])
        else:
            continue
print(f'Пароль: {password}')