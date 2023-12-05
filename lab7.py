import random

# Глобальний список відповідей
answers = ["Так", "Ні", "Можливо", "Не розраховуй на це", "Спробуй знову пізніше"]

def charivna_kulka(question):
    """
    Функція charivna_kulka моделює чарівну кульку передбачень.

    :param question: Рядок - питання для чарівної кульки.
    :return: Рядок - випадкова відповідь зі списку answers.
    """
    if not isinstance(question, str) or not question.strip():
        return "Неправильне питання"
    
    return random.choice(answers)

def configure_magic_ball(new_answers: list, probability=None):
    """
    Функція configure_magic_ball додає нові відповіді та налаштовує шанси їх випадання.

    :param new_answers: Список рядків - нові відповіді для чарівної кульки.
    :param probability: Словник, де ключ - відповідь, значення - ймовірність випадання від 0 до 1.
    """
    global answers
    answers.extend(new_answers)

    if probability:
        for answer, chance in probability.items():
            if answer in answers and 0 <= chance <= 1:
                index = answers.index(answer)
                answers = answers[:index] * int((1 - chance) * 100) + [answer] + answers[index:] * int(chance * 100)

# Тести
def test_charivna_kulka():
    # Тест 1: Функція повертає одне з очікуваних значень
    result = charivna_kulka("Чи буде завтра сонячно?")
    assert result in answers, f"Отримана відповідь {result}, а очікувалася одна з {answers}"

    # Тест 2: Функція повертає значення типу str
    result = charivna_kulka("Питання")
    assert isinstance(result, str), f"Отримане значення {result}, а очікувалася str"

    # Тест 3: Реакція на пусте питання або на введення, яке не є рядком
    result = charivna_kulka("")
    assert result == "Неправильне питання", f"Отримана відповідь {result}, а очікувалася 'Неправильне питання'"

    result = charivna_kulka(123)
    assert result == "Неправильне питання", f"Отримана відповідь {result}, а очікувалася 'Неправильне питання'"

def test_configure_magic_ball():
    # Тест 1: Додавання нових відповідей та налаштування їх ймовірностей
    configure_magic_ball(["Це впевнено"], {"Так": 0.8, "Ні": 0.2})
    result = charivna_kulka("Чи вам подобається цей варіант?")
    assert result == "Так", f"Отримана відповідь {result}, а очікувалася 'Так' з ймовірністю 80%"

    # Тест 2: Перевірка налаштування шансу випадання неіснуючої відповіді
    configure_magic_ball([], {"Не існує": 0.5})
    result = charivna_kulka("Питання")
    assert result in answers, f"Отримана відповідь {result}, а очікувалася одна з {answers}"


def main():
    print("Тестуємо функцію charivna_kulka:")
    test_charivna_kulka()

    print("\nТестуємо функцію configure_magic_ball:")
    test_configure_magic_ball()

    print("\nТестування завершено!")

if __name__ == "__main__":
    main()
