immutable_var=(10,15,'Tuple','c')
print(immutable_var)
#immutable_var[0]=4
#print(immutable_var) # кортеж относится к неизменяемым типам данных и не поддерживает обращение по элементам
mutable_list=[10,15,'Tuple','c']
mutable_list.append(False)
print(mutable_list)