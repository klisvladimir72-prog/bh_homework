import re
from datetime import datetime, timedelta
from typing import Optional
import random
import string
import logging


class User:
    def __init__(self, name: str, login: str, password: Optional[str] = None):
        """
        Создает объект User с валидацией данных.

        Args:
            name: Имя пользователя (только русские буквы)
            login: Логин (латинские буквы, цифры, подчеркивание, >= 6 символов)
            password: Пароль (если не указан, генерируется автоматически)
        """
        self.logger = logging.getLogger(self.__class__.__name__)

        self._name = self._validate_name(name)
        self._login = self._validate_login(login)

        if password is None:
            self._password = self._generate_password()
            self.logger.info(
                f"Сгенерирован пароль для пользователя {self._login}: {self._password}"
            )
        else:
            self._validate_password(password)
            self._password = password
            self.logger.debug(f"Установлен пароль для пользователя {self._login}")

        self._is_blocked = False
        self._subscription_mode = "free"
        # Пробная подписка на 30 дней
        self._subscription_date = datetime.now() + timedelta(days=30)
        self.logger.info(
            f"Создан пользователь {self._login} с пробной подпиской до {self._subscription_date.strftime('%Y-%m-%d')}"
        )

    @staticmethod
    def _validate_name(name: str) -> str:
        """Проверяет имя на соответствие требованиям (только русские буквы)."""
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")

        pattern = r"^[А-ЯЁа-яё]+$"
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

        pattern = r"^[a-zA-Z0-9_]{6,}$"
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

        if not re.match(r"^[a-zA-Z0-9]+$", password):
            raise ValueError("Пароль может содержать только латинские буквы и цифры")

        if not re.search(r"[a-z]", password):
            raise ValueError("Пароль должен содержать хотя бы одну строчную букву")

        if not re.search(r"[A-Z]", password):
            raise ValueError("Пароль должен содержать хотя бы одну заглавную букву")

        if not re.search(r"\d", password):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")

        return True

    @staticmethod
    def _generate_password(length: int = 8) -> str:
        """Генерирует случайный пароль по заданным правилам."""
        while True:
            # Генерируем случайный пароль
            chars = string.ascii_letters + string.digits
            password = "".join(random.choice(chars) for _ in range(length))

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

        old_status = self._is_blocked
        self._is_blocked = value

        action = "заблокирован" if value else "разблокирован"
        self.logger.info(f"Пользователь {self._login} {action}")

        if old_status != value:
            self.logger.debug(
                f"Статус блокировки изменен для пользователя {self._login}: {old_status} -> {value}"
            )

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

        # Проверяем, что дата подписки не истекла
        active = self._subscription_date > date
        days_left = max(0, (self._subscription_date - date).days)

        self.logger.debug(
            f"Проверка подписки для {self._login} на дату {date.strftime('%Y-%m-%d')}: "
            f"активна={active}, режим={self._subscription_mode}, дней_осталось={days_left}"
        )

        return {
            "active": active,
            "mode": self._subscription_mode,
            "days_left": days_left,
        }

    def change_pass(self, new_password: Optional[str] = None) -> None:
        """
        Изменяет пароль пользователя.

        Args:
            new_password: Новый пароль (если не указан, генерируется автоматически)
        """
        if new_password is None:
            old_password = self._password
            self._password = self._generate_password()
            self.logger.info(
                f"Сгенерирован новый пароль для пользователя {self._login}"
            )
            self.logger.debug(f"Пароль изменен: {old_password} -> {self._password}")
        else:
            old_password = self._password
            self._validate_password(new_password)
            self._password = new_password
            self.logger.info(f"Пароль изменен для пользователя {self._login}")
            self.logger.debug(f"Пароль изменен: {old_password} -> {new_password}")

    def extend_subscription(self, new_date: datetime, mode: str = "paid") -> None:
        """
        Продлевает подписку до указанной даты и устанавливает режим подписки.

        Args:
            new_date: Новая дата окончания подписки
            mode: Режим подписки ("free" или "paid")
        """
        if mode not in ["free", "paid"]:
            raise ValueError("Режим подписки должен быть 'free' или 'paid'")

        old_date = self._subscription_date
        old_mode = self._subscription_mode

        self._subscription_date = new_date
        self._subscription_mode = mode

        self.logger.info(
            f"Подписка пользователя {self._login} продлена до {new_date.strftime('%Y-%m-%d')}, режим: {mode}"
        )
        self.logger.debug(
            f"Подписка изменена: дата {old_date} -> {new_date}, режим {old_mode} -> {mode}"
        )

    def get_info(self) -> str:
        """
        Возвращает информацию о пользователе в виде строки.

        Returns:
            Строковое представление информации о пользователе
        """
        info_parts = []

        if self._is_blocked:
            info_parts.append(
                f"Пользователь '{self._name}' ({self._login}) заблокирован."
            )
            result = "\n".join(info_parts)
            self.logger.info(
                f"Получена информация о заблокированном пользователе: {self._login}"
            )
            return result

        subscr_info = self.check_subscr()
        info_parts.extend(
            [
                f"Имя: {self._name}",
                f"Логин: {self._login}",
                f"Статус подписки: {subscr_info['mode']}",
                f"Подписка действует до: {self._subscription_date.strftime('%Y-%m-%d')}",
                f"Осталось дней подписки: {subscr_info['days_left']}",
                f"Статус блокировки: {'Заблокирован' if self._is_blocked else 'Активен'}",
            ]
        )

        result = "\n".join(info_parts)
        self.logger.debug(f"Получена информация о пользователе: {self._login}")
        return result

    # Свойства для доступа к данным
    @property
    def name(self) -> str:
        return self._name

    @property
    def login(self) -> str:
        return self._login

    @property
    def password(self) -> str:
        # В реальных приложениях не рекомендуется предоставлять доступ к паролю
        # Это сделано для демонстрации, в продакшене пароль должен быть защищен
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


# Настройка логирования (для примера)
if __name__ == "__main__":
    # Настройка базового логирования
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Создание пользователя с автоматической генерацией пароля
    user1 = User("Иван", "ivan_user")
    print("--- Информация о пользователе ---")
    print(user1.get_info())

    print("\n--- Проверка подписки ---")
    subscr_result = user1.check_subscr()
    print(f"Подписка активна: {subscr_result['active']}")
    print(f"Режим подписки: {subscr_result['mode']}")
    print(f"Дней осталось: {subscr_result['days_left']}")

    print("\n--- Смена пароля ---")
    user1.change_pass("NewPass123")

    print("\n--- Блокировка пользователя ---")
    user1.block(True)
    print(user1.get_info())

    print("\n--- Разблокировка пользователя ---")
    user1.block(False)
    print(user1.get_info())

    print("\n--- Продление подписки ---")
    new_date = datetime.now() + timedelta(days=90)
    user1.extend_subscription(new_date, "paid")
    print(user1.get_info())
