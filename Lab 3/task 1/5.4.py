def main():
    while True:
        n = input()
        if not n:
            break
        found = False
        for i in range(1, 32):
            t = str(2 ** i)
            # Проверяем что первые цифры получ. числа и искомого совпадают
            # Проверяем, что потерянных цифр больше
            if (n == t[:len(n)]) and (len(n) < len(t) - len(n)):
                found = True
                print(i)
                break
        if not found:
            print("no power of 2")


if __name__ == '__main__':
    main()
