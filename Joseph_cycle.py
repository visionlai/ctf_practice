k = 12
people = 2 * k
skip = 12
while True:
    p_num = list(range(1, people + 1))
    position = 0  # 表示要删除编号的位置，初始为0
    death = 0
    while death < k:
        position = (position + skip) % len(p_num)  # 实现约瑟夫循环
        p = p_num[position]
        if p <= k:
            break
        else:
            p_num.remove(p)
            death = death + 1
    if death == 12:
        print(skip + 1)
        break
    else:
        skip = skip + 1
