"""
HOW IT WORKS:
==============
    * Defining Coroutines:
        The functions say_hello and say_goodbye are defined using async def.

    * Awaiting:
        The await asyncio.sleep() pauses the coroutine without blocking other tasks.

    * Concurrency with asyncio.gather():
        The asyncio.gather() runs both tasks concurrently.
        The event loop switches between tasks while they are waiting for asyncio.sleep().

    * Running the Event Loop:
        The asyncio.run(main()) starts the event loop and runs the main coroutine.

"""
import asyncio


async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)  # Simulate an I/O-bound task
    print("How are you?")


async def say_goodbye():
    print("Goodbye!")
    await asyncio.sleep(2)  # Simulate an I/O-bound task
    print("See you soon!")


async def main():
    # Run both tasks concurrently
    await asyncio.gather(say_hello(), say_goodbye())


# Run the asyncio program
asyncio.run(main())
