import asyncio


async def functionA():
    # print ("1")
    pass

if __name__ == '__main__':
    a = asyncio.get_event_loop()
    asyncio.run(functionA())

    pass