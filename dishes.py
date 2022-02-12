from pprint import pprint

def create_cook_book(dishes_text):
    cook_book = {}

    with open(dishes_text, encoding='utf-8') as f:
        lst = [line.strip() for line in f]


        for i, c in enumerate(lst):
            if c.isdigit():
                cook_book[lst[i - 1]] = []

                for slice in lst[i+1:i+int(c)+1]:
                    ingredient_name = slice.split('| ' )[0]
                    quantity = int(slice.split('| ')[1])
                    measure = slice.split('| ')[2]

                    cook_book[lst[i - 1]].append({'ingredient_name':ingredient_name, 'quantity':quantity, 'measure':measure})
    return cook_book

def get_shop_list_by_dishes(dishes, cooking_book, person_count):
    cook_book = cooking_book
    for key in dishes:
        try:
            for value in cook_book[key]:
                value['quantity'] *= person_count
                print(value)
        except:
            pass

print('Задача №1:\n')
pprint(create_cook_book('dishes_text.txt'))

print('Задача №2:\n')
get_shop_list_by_dishes(['Омлет', 'Запеченный картофель','Фахитос'],\
                        create_cook_book('dishes_text.txt'), 15) 