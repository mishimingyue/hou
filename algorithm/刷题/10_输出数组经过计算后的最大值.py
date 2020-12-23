'''
 给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：
区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。如给定序列  [6 2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:
[6] = 6 * 6 = 36;
[2] = 2 * 2 = 4;
[1] = 1 * 1 = 1;
[6,2] = 2 * 8 = 16;
[2,1] = 1 * 3 = 3;
[6, 2, 1] = 1 * 9 = 9;
从上述计算可见选定区间 [6] ，计算值为 36， 则程序输出为 36。

区间内的所有数字都在[0, 100]的范围内;
第一行输入数组序列长度n，第二行输入数组序列。
'''

import sys

global max_value
max_value = 0


def input_list():
    recivelist1 = sys.stdin.readline().strip()
    recivelist2 = sys.stdin.readline().strip().split(" ")
    arr = []
    for x in recivelist2:
        k = int(x)
        arr.append(k)
    return arr


def search_max(arr):
    global max_value
    if not arr:
        return max_value

    min_value = min(arr)
    min_index = arr.index(min_value)
    sum_value = sum(arr)
    max_value = max(sum_value * min_value, max_value)

    sub_left = arr[0:min_index]
    sub_right = arr[min_index + 1:]

    return max(search_max(sub_left), search_max(sub_right), max_value)


if __name__ == '__main__':
    print(search_max(input_list()))
