import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import select
import asyncio,websockets,json,random
from websockets.exceptions import ConnectionClosedError
import threading

class Operacoes(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.connected = set()
    #USERS = set()

        self.conn = psycopg2.connect(database='fullmotion_db', user='postgres' ,password='5519' ,host='localhost',port='5432')
        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cur = self.conn.cursor()
        self.cur.execute("LISTEN new_id;")

    def run(self):
        while True:
            if select.select([self.conn], [], [], 10) == ([], [], []):
                print("More than 10 seconds passed...")
            else:
                self.conn.poll()
                while self.conn.notifies:
                    print('Got something')
                    notify = self.conn.notifies.pop(0)
                    print(f"Got NOTIFY: {notify.channel} - {notify.payload}")
                    info='channel: '+str(notify.channel)+' Payload:'+str(notify.payload)
                    self.sendData(info)

    async def handler(self, websocket, path):
        self.connected.add(websocket)
        try:
          await websocket.recv()
        except websockets.exceptions.ConnectionClosed:
          pass
        finally:
          self.connected.remove(websocket)

    def sendData(self, data):
        for websocket in self.connected.copy():
          print("Sending data: %s" % data)
          coro = websocket.send(data)
          future = asyncio.run_coroutine_threadsafe(coro, loop)


def ws():
    start_server=websockets.serve(parte1,'localhost',6789)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__=='__main__':
    op=Operacoes()
    try:
        op.start()

        ws_server = websockets.serve(op.handler, 'localhost', 6789)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(ws_server)
        loop.run_forever()
    except KeyboardInterrupt:
        stopFlag = True
        #TODO: close ws server and loop correctely
        print("Exiting program...")
