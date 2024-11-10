my_dict = {'Nikolay': 1990, 'Artur': 1985, 'Sasha': 1995, 'Zina': 1977}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Nikolay'))
print('Not existing value:', my_dict.get('Semen'))
my_dict.update({'Vasya': 2000,
                'Egor': 2001})
a = my_dict.pop('Artur')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)


my_set = {1, 2.3, 'Vasya', (1, 2, 3), 1, 2.3, 'Vasya', (1, 2, 3)}
print(my_set)
my_set.add(8)
my_set.add('mouse')
my_set.discard(2.3)
print(my_set)