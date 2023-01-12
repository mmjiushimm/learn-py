# -*- coding: utf-8 -*-
import itertools, asyncio, time

async def spin():
    for s in itertools.cycle('|/-\\'):
        print(s, end='\r')
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    print(' ', end='\r')

async def work():
    await asyncio.sleep(3)
    return 'loading down'


async def spin_work():
    t1 = asyncio.create_task(spin())
    t2 = asyncio.create_task(work())
    t0 = time.time()
    print(t0)
    # await t1
    result = await t2
    # result = await work()
    t1.cancel()
    t1 = time.time()
    print(t1)
    dt = t1 - t0
    print(dt)
    return result

def main():
    result = asyncio.run(spin_work())
    print(result)

if __name__ == '__main__':
    main()