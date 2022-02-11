import asyncio
import time


async def factorial(name, number):
    f = 1
    for i in range(2 , number + 1):
        print(f"Task {name}: Compute factorial ({number}),  currently i={i}  ")
        await asyncio.sleep(1)
        f *= i

    print(f"Task {name}: factorial({number})  = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    time.sleep(1)
    print(f"blocking_io complete at {time.strftime('%X')}")

async def main():
    print(f"started main at {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io(),
        asyncio.sleep(1))
    )
    print(f"finished main at {time.strftime('%X')}")

asyncio.run(main())



asyncio.run(main())

# Expected output:
#
#     Task A: Compute factorial(2), currently i=2...
#     Task B: Compute factorial(3), currently i=2...
#     Task C: Compute factorial(4), currently i=2...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3), currently i=3...
#     Task C: Compute factorial(4), currently i=3...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4), currently i=4...
#     Task C: factorial(4) = 24
#     [2, 6, 24]