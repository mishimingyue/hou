'''
整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
print(a[:-1])  ### 除了最后一个取全部

print(a[::-1]) ### 取从后向前（相反）的元素

'''


def reverse1(x):
    if -10 < x < 10:
        return x
    else:
        str_x = str(x)
        str_x = str_x[::-1]
        if str_x[-1] == '-':
            str_x = str_x[:-1]
            x = -int(str_x)
        else:
            x = int(str_x)
        return x


if __name__ == '__main__':
    print(reverse1(-44167))
