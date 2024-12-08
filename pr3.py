my_list = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт',  'Hello']

def duplicate_destroyer (lst):
    return list(set(lst))

new_list = duplicate_destroyer(my_list)
print (new_list)