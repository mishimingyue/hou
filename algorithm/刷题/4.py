'''
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。


'''


def plusOne(number_1):
    str1 = ''
    # number_1 = number_1
    for i in range(len(number_1)):
        print(number_1[i])
    str2 = str(int(str1) + 1)
    shuzu = []
    for j in str2:
        shuzu.append(j)
    return shuzu


if __name__ == '__main__':
    plusOne([1, 2, 3])

    #
    # def plusOne(number_1):
    #     str1 = ''
    #     # number_1 = number_1
    #     for i in range(len(number_1)):
    #         print(number_1[i])
    #     str2 = str(int(str1) + 1)
    #     shuzu = []
    #     for j in str2:
    #         shuzu.append(j)
    #     return shuzu
    #
    #
    # if __name__ == '__main__':
    #     plusOne([1, 2, 3])
