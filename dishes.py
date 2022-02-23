from pprint import pprint


def create_cook_book(input_file):
    cook_book = {}

    with open(input_file, encoding='utf-8') as f:
        lst = [line.strip() for line in f]

    for i, c in enumerate(lst):
        
        if c.isdigit():
            # если элемент - цифра, то берем предыдущий элемент
            cook_book[lst[i-1]] = []
            
            for slice in lst[i+1:i+int(c)+1]:
                ingredient_name = slice.split('|')[0]
                quantity = int(slice.split('|')[1])
                measure = slice.split('|')[2]

                cook_book[lst[i-1]].append({'ingredient_name':ingredient_name, 'quantity':quantity, 'measure':measure})
    
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cooking_book):
    ing_dict = {}

    for key in cooking_book.keys ():
        for dish in dishes:
            if key == dish:
                for dictionary in cooking_book[key]:
                    ing_name = dictionary['ingredient_name']

                    try:
                        ing_dict[ing_name]['quantity'] += (dictionary['quantity'] * person_count)
                    except:
                        ing_dict[ing_name] = {'measure': dictionary['measure'], 'quantity': dictionary['quantity'] * person_count}

    return ing_dict

print('Задание №1:\n')
pprint(create_cook_book('dishes_text.txt'))
print('\n' * 3)
print('Задание №2:\n')
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 15, create_cook_book('dishes_text.txt')))
