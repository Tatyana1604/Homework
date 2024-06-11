my_dict = {'Tanya': 1986, 'Kate': 1982, 'Kira': 2017}
print(my_dict)
Existing_value = my_dict['Tanya']
print(Existing_value)
Deleted_value = my_dict.get('Mary')
print(Deleted_value)
my_dict.update({'Luda': 1961, 'Viktor': 1985})
print(my_dict)
a = my_dict.pop('Kate')
print(a)
print(my_dict)

my_set = {1, 8, 'Kate', 15.6, 8, 'Kate'}
print(my_set)
print(my_set.add('Tanya'))
print(my_set.add(10))
print(my_set)
print(my_set.discard(8))
print(my_set)
