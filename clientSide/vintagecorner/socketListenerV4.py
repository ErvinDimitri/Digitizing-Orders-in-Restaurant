import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import select
import asyncio,websockets,json,random
from websockets.exceptions import ConnectionClosedError
import threading
import traceback
import datetime

def dataFetch(id):
    conn = psycopg2.connect(database='fullmotion_db', user='postgres', password='5519', host='localhost', port='5432')
    cur = conn.cursor()
    cur.execute("SELECT * FROM vintagecorner_pedido WHERE id=" + str(id))  # [(2, 5, 1, 3)]
    query = cur.fetchall()[0]
    print(query)
    if query:
        print('Query ----- ',query)
        id, qty, idItem, idMesa,nrItens,hora = query
        # id, qty,nrItens,hora,idItem, idMesa= query

        cur.execute("SELECT * FROM vintagecorner_itensmenu WHERE id=" + str(idItem))  # [(2, 5, 1, 3)]
        query = cur.fetchall()[0]
        print('Item:: ', query)
        item = query[1]
        tipo = query[3]
        valor = float(query[6])
        pedido={'item':item,'tipo':tipo,'valor':valor,'qty':qty,'mesa':idMesa, 'hora':str(hora)}
        return pedido,nrItens
    else:
        print('Nao Encontrado')
        return None

restaurID={'vc':['VintageCorner751']}
class Operacoes(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.connected = set()
        self.restaurWS={'vc':set()}
        self.nrItens=0
        self.pedido=[]
        self.stop=False
    #USERS = set()

        self.conn = psycopg2.connect(database='fullmotion_db', user='postgres' ,password='5519' ,host='localhost',port='5432')
        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cur = self.conn.cursor()
        self.cur.execute("LISTEN pedido;")


    def run(self):
        while True:
            if select.select([self.conn], [], [], 10) == ([], [], []):
                print("More than 10 seconds passed...")
                if self.stop:
                    break
            else:
                self.conn.poll()
                while self.conn.notifies:
                    print('Got something')
                    notify = self.conn.notifies.pop(0)
                    print(f"Got NOTIFY: {notify.channel} - {notify.payload}")
                    info='channel: '+str(notify.channel)+' Payload:'+str(notify.payload)
                    item_pedido,self.nrItens=dataFetch(notify.payload)
                    self.pedido.append(item_pedido)
                    if len(self.pedido)>=self.nrItens:
                        self.sendData(str(self.pedido),notify.channel)
                        self.nrItens=0
                        self.pedido=[]

    async def handler(self, websocket, path):
        # self.connected.add(websocket)
        print('+Ws+')
        try:
            id=await websocket.recv()
            for i in restaurID:
                if id in restaurID[i]:
                    self.restaurWS[i].add(websocket)
                    print('+Ws+++')
                    break
            waiting= await websocket.recv()
        except websockets.exceptions.ConnectionClosed:
          pass
        finally:
          # self.connected.remove(websocket)
            pass

    def sendData(self, data,source):
        try:
            # for websocket in self.connected.copy():
            #   print("Sending data: %s" % data)
            #   coro = websocket.send(data)
            #   future = asyncio.run_coroutine_threadsafe(coro, loop)

            if source=='pedido':
                for websocket in self.restaurWS['vc']:
                    print("Sending data: %s" % data)
                    try:
                        coro = websocket.send(data)
                    except:
                        print('Remover Ws')
                        print(traceback.format_exc())
                    future = asyncio.run_coroutine_threadsafe(coro, loop)

        except:
            print(traceback.format_exc())


# def ws():
#     start_server=websockets.serve(parte1,'localhost',6789)
#     asyncio.get_event_loop().run_until_complete(start_server)
#     asyncio.get_event_loop().run_forever()

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
        op.join()
        op.stop=True
        #TODO: close ws server and loop correctely
        print("Exiting program...")
