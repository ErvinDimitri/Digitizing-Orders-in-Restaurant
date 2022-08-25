
import select
import asyncio,websockets,json,random
from websockets.exceptions import ConnectionClosedError
USERS = set()
# while True:
#     if select.select([conn], [], [], 10) == ([], [], []):
#         print("More than 10 seconds passed...")
#     else:
#         conn.poll()
#         while conn.notifies:
#             notify = conn.notifies.pop(0)
#             print(f"Got NOTIFY: {notify.channel} - {notify.payload}")



async def updateItem():
    id = await websockets.recv()
    print('Recieved ID ',id)

async def callMethods():

    updateItem()
    pass



async def register(websocket):
    USERS.add(websocket)
    print('New User: ',USERS)


async def unregister(websocket):
    USERS.remove(websocket)
    # print(' User Left: ',USERS)

i=0

async def iIncrise():
    global i
    while True:
        await asyncio.sleep(random.random() * 5)
        i+=1

async def parte1(websocket,path):
    global i
    # msg=input('Send Something: ')
    await register(websocket)

    while True:
        msg = 'Lets go'+str(i)
        try:
            await websocket.send(msg)
        except ConnectionClosedError: #Dar Break
            break
        await asyncio.sleep(random.random() * 3)


start_server=websockets.serve(parte1,'localhost',6789)
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()

asyncio.ensure_future(iIncrise())
asyncio.ensure_future(start_server)
loop=asyncio.get_event_loop()
loop.run_forever()

#
# Error in connection handler
# Traceback (most recent call last):
#   File "C:\Users\Ervin Dimitri\AppData\Local\Programs\Python\Python38-32\lib\asyncio\windows_events.py", line 453, in finish_recv
#     return ov.getresult()
# OSError: [WinError 64] The specified network name is no longer available

# ---------
#    raise ConnectionResetError(*exc.args)
# ConnectionResetError: [WinError 64] The specified network name is no longer available
# ----------
#     raise self.connection_closed_exc()
# websockets.exceptions.ConnectionClosedError: code = 1006 (connection closed abnormally [internal]), no reason