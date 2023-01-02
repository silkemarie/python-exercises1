import asyncio

async def greet(name):
    print("Hello, " + name)

async def main():
    await greet("Alice")
    await greet("Bob")

asyncio.run(main())


