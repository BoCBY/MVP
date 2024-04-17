my_list = ['element1', 'element2', 'element3']
my_list[1:3] = ['-'.join(my_list[1:3])]
print(my_list)

my_list = ['element1', 'element2', 'element3']
my_list[1:3] = '-'.join(my_list[1:3])
print(my_list)