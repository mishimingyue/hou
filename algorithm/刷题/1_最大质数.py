'''
寻找小于给定值的最大质数
'''
# -*- utf-8 -*-
import sys


def prime(value):
    for i in range(2, value // 2 + 1):
        if value % i == 0:
            return False
    return True


def max_prime(value):
    for i in range(value, 2, -1):
        if prime(i):
            return i


if __name__ == '__main__':
    reciveStr = sys.stdin.readline()
    input_number = int(reciveStr)
    c = max_prime(input_number)
    print(c)
