import asyncio,websockets

uri = "ws://localhost:6789"
# wb=websockets.connect(uri)

async def recebePedido():
    async with websockets.connect(uri) as websocket:
        while True:
            pedido= await websocket.recv()
            print(pedido)

asyncio.get_event_loop().run_until_complete(recebePedido())
# asyncio.get_event_loop().run_forever()