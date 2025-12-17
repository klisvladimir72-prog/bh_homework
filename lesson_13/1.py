"""
Создать класс User с атрибутами:

Свойства:
	- name - имя - содержит только буквы русского алфавита 
	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
                содержит менее шести символов
                содержит строчную букву
                содержит заглавную букву
                содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)


Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным 
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
						Если дата не передана значит на дату проверки. 
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего. 
						Пароль должен пройти валидацию. 
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. 
Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
Валидацию данных сделать через регулярные выражения
"""


import re
from datetime import datetime, timedelta
from typing import Optional
import random
import string


class User:
    def __init__(self, name: str, login: str, password: Optional[str] = None):
        """
        Создает объект User с валидацией данных.

        Args:
            name: Имя пользователя (только русские буквы)
            login: Логин (латинские буквы, цифры, подчеркивание, >= 6 символов)
            password: Пароль (если не указан, генерируется автоматически)
        """
        self._name = self._validate_name(name)
        self._login = self._validate_login(login)

        if password is None:
            self._password = self._generate_password()
            print(f"Сгенерированный пароль: {self._password}")
        else:
            self._validate_password(password)
            self._password = password

        self._is_blocked = False
        self._subscription_mode = "free"
        # Пробная подписка на 30 дней
        self._subscription_date = datetime.now() + timedelta(days=30)

    @staticmethod
    def _validate_name(name: str) -> str:
        """Проверяет имя на соответствие требованиям (только русские буквы)."""
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")

        pattern = r'^[А-ЯЁа-яё]+$'
        if not re.match(pattern, name):
            raise ValueError(
                "Имя должно содержать только буквы русского алфавита (А-Я, а-я, ё/Ё)"
            )

        return name

    @staticmethod
    def _validate_login(login: str) -> str:
        """Проверяет логин на соответствие требованиям."""
        if not isinstance(login, str) or not login:
            raise ValueError("Логин должен быть непустой строкой")

        pattern = r'^[a-zA-Z0-9_]{6,}$'
        if not re.match(pattern, login):
            raise ValueError(
                "Логин должен содержать только латинские буквы, цифры и "
                "подчеркивание, а также быть не менее 6 символов длиной"
            )

        return login

    @staticmethod
    def _validate_password(password: str) -> bool:
        """Проверяет пароль на соответствие требованиям."""
        if not isinstance(password, str) or len(password) < 6:
            raise ValueError("Пароль должен содержать не менее 6 символов")

        if not re.match(r'^[a-zA-Z0-9]+$', password):
            raise ValueError(
                "Пароль может содержать только латинские буквы и цифры"
            )

        if not re.search(r'[a-z]', password):
            raise ValueError(
                "Пароль должен содержать хотя бы одну строчную букву")

        if not re.search(r'[A-Z]', password):
            raise ValueError(
                "Пароль должен содержать хотя бы одну заглавную букву")

        if not re.search(r'\d', password):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")

        return True

    @staticmethod
    def _generate_password(length: int = 8) -> str:
        """Генерирует случайный пароль по заданным правилам."""
        while True:
            chars = string.ascii_letters + string.digits
            password = ''.join(random.choice(chars) for _ in range(length))

            # Проверяем, соответствует ли сгенерированный пароль требованиям
            try:
                User._validate_password(password)
                return password
            except ValueError:
                # Если пароль не проходит валидацию, генерируем снова
                continue

    def block(self, value: bool) -> None:
        """
        Блокирует или разблокирует пользователя.

        Args:
            value: True для блокировки, False для разблокировки
        """
        if not isinstance(value, bool):
            raise TypeError("Значение должно быть булевым")

        self._is_blocked = value

    def check_subscr(self, date: Optional[datetime] = None) -> dict:
        """
        Проверяет действительность подписки на указанную дату.

        Args:
            date: Дата для проверки (по умолчанию - текущая дата)

        Returns:
            Словарь с информацией о подписке:
            {
                'active': bool,
                'mode': str,
                'days_left': int
            }
        """
        if date is None:
            date = datetime.now()

        active = self._subscription_date > date
        days_left = max(0, (self._subscription_date - date).days)

        return {
            'active': active,
            'mode': self._subscription_mode,
            'days_left': days_left
        }

    def change_pass(self, new_password: Optional[str] = None) -> None:
        """
        Изменяет пароль пользователя.

        Args:
            new_password: Новый пароль (если не указан, генерируется автоматически)
        """
        if new_password is None:
            self._password = self._generate_password()
            print(f"Сгенерированный новый пароль: {self._password}")
        else:
            self._validate_password(new_password)
            self._password = new_password

    def extend_subscription(self, new_date: datetime, mode: str = "paid") -> None:
        """
        Продлевает подписку до указанной даты и устанавливает режим подписки.

        Args:
            new_date: Новая дата окончания подписки
            mode: Режим подписки ("free" или "paid")
        """
        if mode not in ["free", "paid"]:
            raise ValueError("Режим подписки должен быть 'free' или 'paid'")

        self._subscription_date = new_date
        self._subscription_mode = mode

    def get_info(self) -> None:
        """Выводит информацию о пользователе."""
        if self._is_blocked:
            print(f"Пользователь '{self._name}' ({self._login}) заблокирован.")
            return

        subscr_info = self.check_subscr()
        print(f"Имя: {self._name}")
        print(f"Логин: {self._login}")
        print(f"Статус подписки: {subscr_info['mode']}")
        print(
            f"Подписка действует до: {self._subscription_date.strftime('%Y-%m-%d')}")
        print(f"Осталось дней подписки: {subscr_info['days_left']}")
        print(
            f"Статус блокировки: {'Заблокирован' if self._is_blocked else 'Активен'}")

    # Свойства для доступа к данным
    @property
    def name(self) -> str:
        return self._name

    @property
    def login(self) -> str:
        return self._login

    @property
    def password(self) -> str:
        return self._password

    @property
    def is_blocked(self) -> bool:
        return self._is_blocked

    @property
    def subscription_date(self) -> datetime:
        return self._subscription_date

    @property
    def subscription_mode(self) -> str:
        return self._subscription_mode


if __name__ == "__main__":
    user1 = User("Иван", "ivan_user")
    print("--- Информация о пользователе ---")
    user1.get_info()

    print("\n--- Проверка подписки ---")
    subscr_result = user1.check_subscr()
    print(f"Подписка активна: {subscr_result['active']}")
    print(f"Режим подписки: {subscr_result['mode']}")
    print(f"Дней осталось: {subscr_result['days_left']}")

    print("\n--- Смена пароля ---")
    user1.change_pass("NewPass123")

    print("\n--- Блокировка пользователя ---")
    user1.block(True)
    user1.get_info()

    print("\n--- Разблокировка пользователя ---")
    user1.block(False)
    user1.get_info()

    print("\n--- Продление подписки ---")
    new_date = datetime.now() + timedelta(days=90)
    user1.extend_subscription(new_date, "paid")
    user1.get_info()
