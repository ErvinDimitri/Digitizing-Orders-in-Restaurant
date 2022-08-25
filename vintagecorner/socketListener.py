import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import select
import asyncio,websockets,json,random

conn = psycopg2.connect(database='fullmotion_db', user='postgres' ,password='5519' ,host='localhost',port='5432')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute("LISTEN new_id;")
USERS = set()
# while True:
#     if select.select([conn], [], [], 10) == ([], [], []):
#         print("More than 10 seconds passed...")
#     else:
#         conn.poll()
#         while conn.notifies:
#             notify = conn.notifies.pop(0)
#             print(f"Got NOTIFY: {notify.channel} - {notify.payload}")

async def novoPedido():
        await conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop(0)
            print(f"Got NOTIFY: {notify.channel} - {notify.payload}")

async def updateItem():
    id = await websockets.recv()
    print('Recieved ID ',id)

async def callMethods():
    novoPedido()
    updateItem()
    pass



async def register(websocket):
    USERS.add(websocket)
    print('New User: ',USERS)


async def unregister(websocket):
    USERS.remove(websocket)
    # print(' User Left: ',USERS)


async def parte1(websocket,path):
    i=0
    # msg=input('Send Something: ')
    await register(websocket)

    while True:
        msg = 'Lets go'+str(i)
        try:
            # await websocket.send(msg)
            await asyncio.wait([user.send(msg) for user in USERS])
            print(websocket,'\tNormal',i)
        except:
            print('Disconnected\t',websocket)
            await unregister(websocket)

        await asyncio.sleep(random.random() * 3)
        i+=1

start_server=websockets.serve(parte1,'localhost',6789)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()