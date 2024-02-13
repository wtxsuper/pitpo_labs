# Задаем константы для мастей и значений карт
SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


# Функция для получения имени карты по ее номеру
def get_card_name(card_number):
    suit = SUITS[(card_number - 1) // 13]  # Определяем масть по целочисленному делению
    value = VALUES[(card_number - 1) % 13]  # Определяем значение по остатку от деления
    return f"{value} of {suit}"  # Возвращаем имя карты в формате <значение> of <масть>


# Функция для применения трюка к колоде карт
def apply_trick(deck, trick):
    new_deck = [0] * 52  # Создаем новую пустую колоду
    for i in range(52):
        new_deck[trick[i] - 1] = deck[i]  # Переставляем карты в соответствии с трюком
    return new_deck  # Возвращаем новую колоду


# блоки
blocks = int(input())
for _ in range(blocks):
    input()
    t_num = int(input())
    tricks = []
    for _ in range(t_num):  # Для каждого трюка
        trick = list(map(int, input().split()))  # Читаем 52 целых числа и преобразуем их в список
        tricks.append(trick)  # Добавляем трюк в список
    deck = list(range(1, 53))  # Создаем колоду карт в исходном порядке
    while True:  # Пока вводятся номера трюков
        t = input()
        if t.strip() == "":
            break
        #  Применяем трюк к колоде
        deck = apply_trick(deck, tricks[int(t) - 1])
    # Выводим результат
    for card in deck:
        print(get_card_name(card))
    print()  # Выводим пустую строку-разделитель
