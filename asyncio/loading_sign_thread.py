# -*- coding: utf-8 -*-
import itertools, sys, time, threading

# 通过对象的属性，从外部控制子线程的循环结束
class Signal(object):
    flag = True

def spinner(signal):
    for s in itertools.cycle('|/-\\'):
        if not signal.flag:
            break
        sys.stdout.write(s)
        sys.stdout.flush()
        # 光标回退（backspace）到初始位置，为下一次在同一个位置的write做好准备
        sys.stdout.write('\b')
        time.sleep(0.1)
    # 循环退出后，把当前位置的内容覆盖为空白
    sys.stdout.write(' ')
    # 把光标位置回退到初始位置，为后续打印信息做好准备
    sys.stdout.write('\b')
    
def work():
    time.sleep(2)
    return 'loading done'

def main():
    signal = Signal()
    t = threading.Thread(target=spinner, args=(signal,))
    t.start()
    result = work()
    # 修改signal对象的属性值，控制子线程循环体的结束
    signal.flag = False
    t.join()
    print(result)
    
if __name__ == '__main__':
    main()