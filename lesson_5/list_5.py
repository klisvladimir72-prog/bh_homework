"""
Дан список
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

"""

test_list = ["samsung", "lg", "xerox", "bosch"]

delete_item = "xerox"

if delete_item in test_list:
    test_list.remove(delete_item)
else:
    print(f"Элемент {delete_item} не найден!")

test_list.insert(1, "indesit")

print(test_list)