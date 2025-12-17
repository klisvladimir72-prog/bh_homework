import random
from abc import ABC, abstractmethod
from typing import List, Optional


# ===========================================
# ПАТТЕРН "СОСТОЯНИЕ": АТАКА, ЗАЩИТА, ОТДЫХ
# ===========================================


class State(ABC):
    @abstractmethod
    def execute(self, hero):
        pass

    @abstractmethod
    def change_state(self, hero):
        pass


class AttackState(State):
    def execute(self, hero):
        print(f"  🗡️ {hero.name} выбирает атаковать!")

    def change_state(self, hero):
        hero.state = DefenseState()


class DefenseState(State):
    def execute(self, hero):
        print(f"  🛡️ {hero.name} выбирает защищаться!")
        hero.defending = True

    def change_state(self, hero):
        hero.state = RestState()


class RestState(State):
    def execute(self, hero):
        print(f"  😴 {hero.name} выбирает отдыхать!")
        hero.heal(10)

    def change_state(self, hero):
        hero.state = AttackState()


# ===========================================
# ЭФФЕКТЫ СТАТУСОВ
# ===========================================


class StatusEffect:
    def __init__(self, name: str, duration: int):
        self.name = name
        self.duration = duration

    def apply(self, hero):
        pass

    def tick(self):
        self.duration -= 1
        return self.duration <= 0


class Poison(StatusEffect):
    def __init__(self, damage: int = 5, duration: int = 3):
        super().__init__("Яд", duration)
        self.damage = damage

    def apply(self, hero):
        hero.health -= self.damage
        if hero.health < 0:
            hero.health = 0
        print(f"   🧨 {hero.name} получает {self.damage} урона от яда!")


class Slow(StatusEffect):
    def __init__(self, reduction: int = 5, duration: int = 2):
        super().__init__("Замедление", duration)
        self.reduction = reduction

    def apply(self, hero):
        print(f"   🐌 {hero.name} замедлен! Атака снижена на {self.reduction}.")


class Shield(StatusEffect):
    def __init__(self, shield: int = 10, duration: int = 2):
        super().__init__("Щит", duration)
        self.shield = shield

    def apply(self, hero):
        print(f"   🛡️ {hero.name} защищён щитом на {self.shield} ед.!")


# ===========================================
# БАЗОВЫЙ КЛАСС ГЕРОЯ
# ===========================================


class Hero:
    def __init__(self, name: str, health: int = 100, attack_power: int = 20):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.status_effects: List[StatusEffect] = []
        self.defending = False
        self.state: State = AttackState()

    def is_alive(self) -> bool:
        return self.health > 0

    def heal(self, amount: int):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def take_damage(self, damage: int):
        if self.defending:
            damage //= 2
            self.defending = False
            print(f"   🛡️ {self.name} защищается! Урон уменьшен до {damage}")
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def apply_status_effect(self, effect: StatusEffect):
        self.status_effects.append(effect)

    def update_status_effects(self):
        expired = []
        for effect in self.status_effects:
            effect.apply(self)
            if effect.tick():
                expired.append(effect)
        for e in expired:
            self.status_effects.remove(e)

    def get_resource_info(self) -> str:
        # Переопределяется в наследниках
        return ""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', health={self.health})"


class Warrior(Hero):
    def __init__(self, name: str):
        super().__init__(name, health=120, attack_power=25)
        self.rage = 5
        self.special_damage = 40

    def get_resource_info(self) -> str:
        return f"Ярость: {self.rage}"

    def special_attack(self, other):
        if self.rage > 0:
            other.take_damage(self.special_damage)
            self.rage -= 1
            print(
                f"   ⚡ {self.name} использует яростную атаку! Урон: {self.special_damage}"
            )
        else:
            print(
                f"   ❌ {self.name} не может использовать спец.атаку: ярость закончилась."
            )

    def attack(self, other):
        if self.rage > 0 and random.random() < 0.25:
            self.special_attack(other)
        else:
            other.take_damage(self.attack_power)
            print(f"   ⚔️ {self.name} наносит обычную атаку! Урон: {self.attack_power}")


class Mage(Hero):
    def __init__(self, name: str):
        super().__init__(name, health=90, attack_power=15)
        self.mana = 10
        self.spell_damage = 50

    def get_resource_info(self) -> str:
        return f"Мана: {self.mana}"

    def special_attack(self, other):
        if self.mana >= 2:
            other.take_damage(self.spell_damage)
            self.mana -= 2
            print(f"   🔮 {self.name} колдует! Урон: {self.spell_damage}")
            if random.random() < 0.5:
                other.apply_status_effect(Poison(damage=8, duration=2))
        else:
            print(
                f"   ❌ {self.name} не может использовать заклинание: не хватает маны."
            )

    def attack(self, other):
        if self.mana >= 2 and random.random() < 0.25:
            self.special_attack(other)
        else:
            other.take_damage(self.attack_power)
            print(f"   ⚔️ {self.name} наносит обычную атаку! Урон: {self.attack_power}")


class Archer(Hero):
    def __init__(self, name: str):
        super().__init__(name, health=100, attack_power=20)
        self.focus = 3
        self.piercing_shot = 35

    def get_resource_info(self) -> str:
        return f"Фокус: {self.focus}"

    def special_attack(self, other):
        if self.focus > 0:
            other.take_damage(self.piercing_shot)
            self.focus -= 1
            print(
                f"   🏹 {self.name} делает пронзающий выстрел! Урон: {self.piercing_shot}"
            )
        else:
            print(
                f"   ❌ {self.name} не может использовать пронзающий выстрел: фокус закончился."
            )

    def attack(self, other):
        if self.focus > 0 and random.random() < 0.25:
            self.special_attack(other)
        else:
            other.take_damage(self.attack_power)
            print(f"   ⚔️ {self.name} наносит обычную атаку! Урон: {self.attack_power}")


# ===========================================
# АРЕНА
# ===========================================


class Arena:
    def __init__(self, warriors: Optional[List[Hero]] = None):
        self.warriors = warriors if warriors is not None else []

    def add_warrior(self, warrior: Hero):
        if warrior in self.warriors:
            raise ValueError("Воин уже на арене")
        self.warriors.append(warrior)
        print(f"⚔️ {warrior.name} участвует в битве!")

    def choose_warrior(self) -> Hero:
        return random.choice(self.warriors)

    def show_battlefield_status(self):
        """
        Выводит таблицу с текущим статусом всех героев на арене.
        """
        print("\n" + "=" * 60)
        print("📊 ТЕКУЩЕЕ СОСТОЯНИЕ ВСЕХ ГЕРОЕВ:")
        print("=" * 60)
        print(f"{'Имя':<15} {'Здоровье':<10} {'Ресурсы':<15} {'Статусы':<20}")
        print("-" * 60)

        for w in self.warriors:
            health_bar = "❤️ " * (w.health // 10) + ("🖤 " if w.health == 0 else "")
            resource_info = w.get_resource_info()
            status_names = [e.name for e in w.status_effects]
            statuses = ", ".join(status_names) if status_names else "нет"
            print(
                f"{w.name:<15} {w.health:>3}/{w.max_health:<3}     {resource_info:<15} {statuses:<20} [{health_bar}]"
            )

        print("=" * 60)

    def battle(self) -> Hero:
        if len(self.warriors) < 2:
            raise ValueError("Количество воинов на арене должно быть больше 1")

        print("⚔️ БИТВА НАЧИНАЕТСЯ!\n")

        round_num = 1
        while len(self.warriors) > 1:
            print(f"--- Раунд {round_num} ---")

            attacker = self.choose_warrior()
            target = self.choose_warrior()
            while target == attacker and len(self.warriors) > 1:
                target = self.choose_warrior()

            # Применяем эффекты
            attacker.update_status_effects()

            # Выбор действия (состояние)
            attacker.state.execute(attacker)
            attacker.state.change_state(attacker)

            print(f"\n{attacker.name} атакует {target.name}!")
            attacker.attack(target)

            # Показываем статусы после атаки
            self.show_battlefield_status()

            if not target.is_alive():
                print(f"💀 {target.name} пал в битве!")
                self.warriors.remove(target)
            print("-" * 30)

            round_num += 1

        winner = self.warriors[0]
        print(f"\n🏆 Победил воин: {winner.name}!")
        return winner


# ===========================================
# ЗАПУСК ИГРЫ
# ===========================================

if __name__ == "__main__":
    # Создаём воинов
    warrior1 = Warrior("Конан")
    mage1 = Mage("Гендальф")
    archer1 = Archer("Леголас")
    warrior2 = Warrior("Тиранд")

    # Создаём арену и добавляем воинов
    arena = Arena()
    arena.add_warrior(warrior1)
    arena.add_warrior(mage1)
    arena.add_warrior(archer1)
    arena.add_warrior(warrior2)

    # Запускаем битву
    arena.battle()
