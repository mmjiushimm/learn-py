# -*- coding:utf-8 -*-
from multiprocessing.managers import BaseManager
import time, random

'''
class MyManager(BaseManager):
    pass
'''

BaseManager.register('get_task_queue')
BaseManager.register('get_result_queue')

address = ('127.0.0.1', 60000)
authkey = b'12'
manager = BaseManager(address, authkey)
print('manager is created')

#if __name__ == '__main__':
manager.connect()
print('manager is connected')
worker_task_queue = manager.get_task_queue()
worker_result_queue = manager.get_result_queue()

i = 0
while True:
    data = worker_task_queue.get()
    print(f'No {i} data = {data}')
    time.sleep(random.randint(1, 5))
    result = data * data
    worker_result_queue.put(result)
    print(f'No {i} result = {result}')
    i += 1
