'''
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
'''
import sys

input_1 = sys.stdin.readline().strip().split(" ")

input_1.reverse()
print(input_1)
# *************************************
str1 = ' '
k = str1.join(input_1)
print(k)
