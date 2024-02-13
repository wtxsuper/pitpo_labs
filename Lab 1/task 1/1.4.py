# блоки голосования
blocks = int(input())
for _ in range(blocks):  # Для каждого блока
    input()  # пропуск строки ввода
    names = {}  # имена кандидатов в порядке бюллетеня
    papers = []  # Список бюллетеней
    c_num = int(input())  # Число кандидатов
    # Ввод кандидатов
    for i in range(c_num):
        names[str(i + 1)] = input()
    # Ввод бюллетеней
    while True:
        t = input()
        if t.strip() == "":  # Если введена пустая строка, прерываем ввод
            break
        papers.append(t.split())

    while True:  # пока не будет определён победитель или равное кол-во голосов
        candidates = {k: 0 for k in names.keys()}  # Обнуляем результаты голосования
        for paper in papers:
            candidates[paper[0]] += 1
        # Сортировка словаря по значениям с преобразованием в список
        sorted_candidates = sorted(candidates.items(), key=lambda x: x[1])

        # -- Условия победы --
        # Если кандидат с наибольшим кол-вом голосов имеет 50 и более процентов
        if sorted_candidates[-1][1] / len(papers) > 0.5:
            print(names[sorted_candidates[-1][0]])  # Выводим имя победителя
            print()  # пустая строка-разделитель
            break
        is_equal = True
        for i in range(len(sorted_candidates) - 1):
            if sorted_candidates[i][1] != sorted_candidates[i + 1][1]:
                is_equal = False
                break
        # Если равное кол-во голосов - вывод всех кандидатов
        if is_equal:
            for sc in sorted_candidates:  # Выводим имена всех кандидатов с равными голосами
                print(names[sc[0]])
            print()  # пустая строка-разделитель
            break
        # -- Убираем из бюллетеней наименьшего --
        smaller = sorted_candidates[0][0]
        for paper in papers:
            paper.remove(smaller)
