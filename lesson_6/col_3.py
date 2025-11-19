"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""

d = {'one': 11, 'two': 22, 'hello': 'python', True: False}

print("Исходный словарь:")
print(d)


items = list(d.items())

print(f"\nЭлементы словаря:")
for i, (key, value) in enumerate(items):
    print(f"{i}: {key} ⇛ {value}")


while True:
    try:
        index = int(input(f"\nВведите номер элемента (0-{len(items)-1}): "))
        if 0 <= index < len(items):
            key_to_delete = items[index][0]
            del d[key_to_delete]
            print(f"\n✔ Элемент с ключом '{key_to_delete}' удалён.")
            break
        else:
            print(f"Номер должен быть от 0 до {len(items)-1}.")
    except ValueError:
        print("❌ Ошибка: введите целое число.")
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")


print("\nСловарь после удаления:")
print(d)
