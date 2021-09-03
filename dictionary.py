my_dict = {'account name': 'Jack', 'branch': 'Pune'}

# Output: Jack
print("the account name is",my_dict['account name'])

# Output: pune
print("the brach in which account exist",my_dict.get('branch'))


my_dict.keys()
print(my_dict.keys())

my_dict.values()
print(my_dict.values())

new=my_dict.copy()
print(my_dict.copy())

my_dict.items()
print(my_dict.items())

my_dict.get('account name')
my_dict.get('branch')
print(my_dict.get('account name'))
print(my_dict.get('branch'))

new2={'state':'maharashtra'}
my_dict.update(new2)
print(my_dict)

new=my_dict.pop('account name')
print('the poped element is ',new)
print('the my_dict is',my_dict)

my_dict.clear()
print(my_dict.clear())












