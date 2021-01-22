'''
 编写一个程序，将输入字符串中的字符按如下规则排序。
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
如，输入： Type 输出： epTy
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
如，输入： BabA 输出： aABb
规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y

注意有多组测试数据，即输入有多行，每一行单独处理（换行符隔开的表示不同行）
'''

while True:
    try:
        a = input()
        # 构造两个列表，一个列表用来放全字母的字符串2，另外一个列表取出来
        char = []  # 构造一个列表用来存放字符串
        res = [False] * len(a)  # 构造一个列表用来记住非字母的位置
        for i, v in enumerate(a):
            if v.isalpha():  # 如果全是字母则放入char中
                char.append(v)
            else:
                res[i] = v
        # 然后对char进行排序
        char.sort(key=lambda c: c.lower())
        # 重构,在res中的false项中放入char
        for i, v in enumerate(res):
            if not v:
                res[i] = char[0]
                char.pop(0)
        print(''.join(res))
    except:
        break
