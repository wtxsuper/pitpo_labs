def flip(stack, position):
    # Переворачивает стопку оладий от верхней до указанной позиции
    return stack[:position][::-1] + stack[position:]


def main():
    while True:
        try:
            # Чтение входных данных
            stack = list(map(int, input().split()))
            if not stack:
                break
            print(*stack, end=' ')
            flips = []
            # Итерация начинается с самой большой оладьи (самого большого диаметра)
            for i in range(len(stack), 1, -1):
                max_diameter = max(stack[:i])
                # поиск индекса самой большой оладьи в текущей стопке
                max_index = stack.index(max_diameter)
                # Если индекс не равен текущему индексу (т.е., оладьи не находятся в правильном порядке), выполняются
                # перевороты
                if max_index != i - 1:
                    # Если индекс не равен 0, выполняется переворот от верхней оладьи до найденной оладьи
                    if max_index != 0:
                        stack = flip(stack, max_index + 1)
                        flips.append(max_index + 1)
                    # Выполняется переворот от верхней оладьи до текущей оладьи
                    stack = flip(stack, i)
                    flips.append(i)
            # Выводим перевороты, если верхняя оладушка - 1-ая
            print(*map(lambda x: len(stack) - x + 1, flips), 0)
        except EOFError:
            break


if __name__ == "__main__":
    main()
