"""
Запросить трижды ввод наименования товаров и их цену через пробел.
"пример:
>>>яблоко 10"
>>>груша 15
>>>малина 20

    - создать из введенных данных словарь где ключ это наименование, а цена значение
    - запросить имя товара, найти его в словаре, и вывести его цену, увеличенную на 15%.
    - вывести сумму всех товаров

"""

from pprint import pprint


def validation_input_name(word: str):
    if not word:
        return False

    return all(elem.isalpha() or elem == "-" or elem == " " for elem in word)


def get_products(count):
    while True:
        user_input = input(f"Товар {count}: ").strip().capitalize()

        if not user_input:
            print("Вы забыли ввести данные!")
            continue

        input_parts = user_input.split()

        if len(input_parts) < 2:
            try:
                float(user_input)
                print("Вы забыли ввести название товара!")
                continue
            except ValueError:
                # Значит, это название без цены
                print(f"Забыли ввести цену для '{user_input}'!")
                continue

        name_product = " ".join(input_parts[:-1])
        price_product = input_parts[-1]

        if not validation_input_name(name_product):
            print(
                f"""❌ Ошибка! Название товара может содержать только буквы, ' ', '-'.
Попробуйте снова👌"""
            )
            continue

        try:
            price = float(price_product)
            if price <= 0:
                print("Товар должен стоить больше чем 0!")
                continue
        except ValueError or TypeError:
            print(f"❌ Ошибка: цена должна быть числом! \nПопробуйте снова👌")
            continue

        name = name_product
        return name, price


products_list = {}

print(f"Введите название товара и его цену через пробел.")
for i in range(3):
    name, price = get_products(i + 1)
    products_list[name] = price

print("Каталог товаров успешно создан🥳")
pprint(products_list, width=1)

# Поиск товара
while True:
    search_product = " ".join(
        input(
            f"""{'-'*40}
Введите название товара для поиска: """
        ).split()
    ).capitalize()

    if not search_product:
        print("Вы забыли ввести название!")
        continue

    if not validation_input_name(search_product):
        print(
            f"""❌ Ошибка! Название товара может содержать только буквы, ' ', '-'.
Попробуйте снова👌"""
        )
        continue

    if search_product in products_list:
        print(
            f"Стоимость {search_product} составляет {products_list[search_product] * 1.15}"
        )
        break
    else:
        pprint(products_list, width=1)
        print(
            f"""❌ Товар {search_product} в каталоге не найден!
Попробуйте снова!""",
        )

        continue


print(f"Стоимость всех товаров составляет: {sum(products_list.values())}")
