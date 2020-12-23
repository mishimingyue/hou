'''
给定n个字符串，请对n个字符串按照字典序排列。
'''
import sys

input_list = []
reciveStr = sys.stdin.readline().strip()
while 1:
    line = sys.stdin.readline().strip()
    if line:
        line = map(str, line.split())
    else:
        break
    input_list += line

input_list.sort(reverse=False)

i = len(input_list)
for i in range(i):
    print(input_list[i])
