'''
接受一个只包含小写字母的字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）
'''
import sys

input_number = sys.stdin.readline().strip()
input_list = list(input_number)
input_list.reverse()
str1 = ''
l = str1.join(input_list)
print(l)
