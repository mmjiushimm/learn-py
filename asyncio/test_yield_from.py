# -*- coding: utf-8 -*-

# 子生成器
def sub_gen():
    num = 0
    sum = 0
    count = 0
    average = 0
    
    while True:
        num = yield average
        # 只有退出循环，return才能返回值
        if num == None:
            break
        sum = sum + num
        count += 1
        average = sum / count
    
    return average, count

# 委派生成器
def dele_gen():
    while True:
        # 子生成器return之前，委派生成器一直停在yield from表达式,当子生成器的循环结束后，才能返回值，yield from才能把子生成器函数的返回值赋给等号左边。
        average, count = yield from sub_gen()
        print('average = {0}, count = {1}'.format(average, count))

# 调用方
def main():
    g = dele_gen()
    print(next(g))
    # 调用方通过send()把值直接传递给子生成器，再通过send()直接从子生成器获得产出值。
    print(g.send(10))
    print(g.send(20))
    print(g.send(None))
    print(g.send(30))
    print(g.send(None))

if __name__ == '__main__':
    main()