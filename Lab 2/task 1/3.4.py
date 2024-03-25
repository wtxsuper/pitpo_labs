def find_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])

    # Перебираем все клетки в сетке
    for i in range(rows):
        for j in range(cols):
            # Проверяем, начинается ли слово с текущей буквы
            if grid[i][j].lower() == word[0].lower():
                # Проверяем все направления
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue  # Пропускаем текущую клетку
                        x, y = i, j
                        found = True
                        # Для каждой буквы в слове, кроме первой
                        for char in word[1:]:
                            # Передвигаемся по сетке
                            x += dx
                            y += dy
                            # Если текущая клетка не выходит за границы сетки или текущая буква не соотвествует слову -
                            # выходим и обнуляем флаг найденного
                            if not (0 <= x < rows and 0 <= y < cols) or grid[x][y].lower() != char.lower():
                                found = False
                                break
                        if found:
                            return i + 1, j + 1  # Возвращаем координаты (с единицы) первой буквы слова


def main():
    blocks = int(input())
    for _ in range(blocks):
        input()
        m, n = map(int, input().split())
        grid = [input() for _ in range(m)]
        k = int(input())
        for _ in range(k):
            word = input()
            position = find_word(grid, word)
            print(*position)


if __name__ == '__main__':
    main()
