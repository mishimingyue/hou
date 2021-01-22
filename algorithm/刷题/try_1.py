def maopao(list_1):
    n = len(list_1)
    count = 0
    for j in range(n - 1):
        for i in range(n - 1 - j):
            if list_1[i] > list_1[i + 1]:
                list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]
                count += 1
        if count == 0:
            return list_1

    return list_1


if __name__ == '__main__':
    print(maopao([3, 2, 1, 4, 55, 6, 7, 655]))
