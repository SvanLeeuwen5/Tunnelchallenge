import asyncio
from websockets import connect


async def main():
    url = "localhost:8000"
    async with connect(url) as websocket:
        await websocket.send("hello")
        await websocket.recv()

if __name__ == "__main__":
    asyncio.run(main())
