# -*- coding:utf-8 -*-
from queue import Queue
from multiprocessing.managers import BaseManager
import random, time, threading, queue

v_task_queue = Queue()
v_result_queue = Queue()

def task_queue():
    return v_task_queue

def result_queue():
    return v_result_queue

def thread_put_data(q):
    i = 0
    while True:
        if i == 10:
            break
        data = random.randint(1, 10)
        print(f'No {i} data = {data}')
        q.put(data)
        time.sleep(random.randint(0, 3))
        i += 1

def thread_get_result(q):
    i = 0
    while True:
        try:
            data = q.get(timeout=20)
            print(f'No {i} result = {data}')
            i += 1
        except queue.Empty as e:
            print(e)
            break

'''
class MyManager(BaseManager):
    pass
'''

BaseManager.register('get_task_queue', task_queue)
BaseManager.register('get_result_queue', result_queue)

address = ('127.0.0.1', 60000)
authkey = b'12'
manager = BaseManager(address, authkey)
print('manager is created')

if __name__ == '__main__':
    manager.start()
    print('manager is started')
    master_task_queue = manager.get_task_queue()
    master_result_queue = manager.get_result_queue()

    '''
    for i in range(10):
        x = random.randint(1, 100)
        master_task_queue.put(x)
        print('No %d is put into queue, value = %d' % (i, x))
        time.sleep(random.randint(0, 3))
    
    for i in range(10):
        master_result_queue = manager.get_result_queue()
        print('master_result_queue is', master_result_queue)
        print(master_result_queue.get(timeout=10))
    '''
    t_task = threading.Thread(target=thread_put_data, args=(master_task_queue,))
    t_result = threading.Thread(target=thread_get_result, args=(master_result_queue,))
    t_task.start()
    t_result.start()
    t_task.join()
    t_result.join()
    
    manager.shutdown()
    print('manager is shutdown')

