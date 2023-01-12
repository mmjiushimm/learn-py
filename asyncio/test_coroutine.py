# -*- coding: utf-8 -*-
import asyncio, time

async def f():
    print('h')
    # await()方法挂起当前协程的执行（不阻塞其他协程的执行），以等待1个awaitable对象（协程函数返回的对象）。await后面只能跟awaitable对象（coroutine\task\future），await只能用在async方法里
    await asyncio.sleep(1)
    print('w')

async def f1(content, delay):
    # asyncio.sleep()会挂起当前任务，运行其他协程。待sleep结束后，这个协程才能继续执行
    await asyncio.sleep(delay)
    print(content)

async def f1_await():
    t0 = time.time()
    # 按顺序等待2个协程运行完成，不是并发运行
    await f1('h', 1)
    await f1('w', 2)
    # asyncio.run(f1('h', 1))
    t1 = time.time()
    dt = t1 - t0
    print(dt)
    
async def f1_task():
    # 把协程对象封装成任务对象，main()函数中通过asyncio.run()并发运行2个协程。
    t1 = asyncio.create_task(f1('h', 1))
    t2 = asyncio.create_task(f1('w', 2))
    print(time.strftime('%X'))
    # await t1
    # await t2
    # await f1('w', 2)
    # asyncio.sleep和time.sleep的区别是，前者不阻塞程序，只是挂起当前任务，事件循环依然可以运行其他任务，而后者是阻塞式的，在sleep的时间里，任何任务都不会被运行，所以为了让t1和t2有时间运行，此处应非阻塞式的挂起一段时间，时间长度至少应该是t1和t2两个任务中时间最长的那个
    # await asyncio.sleep(4)
    # time.sleep(4)
    # asyncio.wait()等待2个任务完成后，再继续当前协程
    await asyncio.wait((t1, t2))
    print(time.strftime('%X'))

def main():
    # f()
    # 主函数通过asyncio.run()运行协程，有3种方式：直接运行协程对象；运行await的协程对象；通过asyncio.create_task()把协程对象封装成任务对象。
    asyncio.run(f())
    # asyncio.run(f1_await())
    # asyncio.run(f1_task())

if __name__ == '__main__':
    main()