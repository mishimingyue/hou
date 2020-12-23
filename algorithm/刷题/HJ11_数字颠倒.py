'''
输入一个整数，将这个整数以字符串的形式逆序输出

程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001
'''
import sys

input_number = sys.stdin.readline().strip()
input_list = list(input_number)
input_list.reverse()
str1 = ''
l = str1.join(input_list)
print(l)
