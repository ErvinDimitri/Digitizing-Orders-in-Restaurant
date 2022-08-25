import asyncio,websockets
import win32api
import win32print
import requests
from requests.auth import HTTPBasicAuth
import sys
import threading
import ctypes
import winsound

frequency=2500
duration=2000

uri = "ws://localhost:6789"
# uri = "ws://35.239.57.255:5432"
# wb=websockets.connect(uri)
# uri = "ws://35.193.130.254:9944"
# uri = "ws://34.121.93.217:9944"

# def registarPedido(pedidos):
def registarPedido(comida,bebida,time,mesa):

    # filePed=open('logPedidos.txt','r')
    # data=filePed.readlines()
    # filePed.close()
    # filePed=open('logPedidos.txt', 'w')
    # if type(data) == str:
    #     data=eval(data)
    # regSave=[pedidos]
    # if data != []:
    #     for i in data:
    #         regSave.append(i)
    # filePed.write(str(regSave))
    # filePed.close()
    # with open('logPedidos.csv', 'a') as csvFile:
    #     csvFile.write('Inicio,-,-\n')
    #     for pedido in pedidos:
    #         row=str(pedido['item'])+','+str(pedido['tipo'])+','+str(pedido['valor'])+','+str(pedido['qty'])+','+str(pedido['mesa'])+','+str(pedido['hora'])+'\n'
    #         csvFile.write(row)
    #     csvFile.write('Fim,-,-\n')

    comida=comida.replace('\n','#')
    bebida=bebida.replace('\n','#')
    with open('logPedidos.csv', 'a') as csvFile:
        csvFile.write(str(mesa)+','+str(comida)+','+str(bebida)+','+str(time)+'\n')



def sendToPrinters(pedidos):
    winsound.Beep(frequency,duration)
    pedidos = eval(pedidos)
    # registarPedido(pedidos)
    file = open('impressoraDefault.txt', 'r')
    printers = eval(file.readline())
    file.close()
    print(pedidos)

    print('----\n',pedidos,'\n------')
    impComida=' Mesa: '+str(pedidos[0]['mesa'])+'\n'
    impBebida=' Mesa: '+str(pedidos[0]['mesa'])+'\n'
    com=''
    beb=''
    for pedido in pedidos:
        qty = int(pedido['qty'])
        order=str(pedido['item']) + '(x'+ str(qty)+ ').......' + str(qty * float(pedido['valor']))+'\n'
        if pedido['tipo']=='Comida':
            impComida+=order
            com+=order
        else:
            impBebida += order
            beb += order
    registarPedido(com,beb,pedidos[0]['hora'],pedidos[0]['mesa'])
    pedidoMsg=''
    if impComida != ' Mesa: '+str(pedidos[0]['mesa'])+'\n':
        impComida+=str(printers['Comida'])
        file=open('impComida.txt','w')
        file.write(impComida)
        file.close()
        pedidoMsg+='Comida:\n'+com+'\n'
        print(impComida)
        # win32api.ShellExecute(0, "printto", 'impComida.txt', '"%s"' % printers['Comida'], ".", 0)

    if impBebida != ' Mesa: '+str(pedidos[0]['mesa'])+'\n':
        impBebida+=str(printers['Bebida'])
        file = open('impBebida.txt', 'w')
        file.write(impBebida)
        file.close()
        pedidoMsg += 'Bedida:\n' + beb
        print(impBebida)
        # win32api.ShellExecute(0, "printto", 'impBebida.txt', '"%s"' % printers['Bebida'], ".", 0)
    text='Mesa: '+str(pedidos[0]['mesa'])+'\n'+pedidoMsg
    ctypes.windll.user32.MessageBoxW(0, text , 'Novo Pedido', 0)


def ordem(pedidoTotal):
    pedidos=eval(pedidoTotal)
    print('------ New Order ------')
    for pedido in pedidos:
        qty=int(pedido['qty'])
        print(pedido['item'],' Quantidade: ',qty,' Valor a Pagar: ',qty*float(pedido['valor']),' Mesa: ',pedido['mesa'])
    print('------  ------')

class WsPedidos(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)


    async def recebePedido(self):
        async with websockets.connect(uri) as websocket:
            await websocket.send('VintageCorner751')
            while True:
                pedido= await websocket.recv()
                # ordem(pedido)
                sendToPrinters(pedido)

    def run(self):
        loop=asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        future=asyncio.ensure_future(self.recebePedido())
        loop.run_until_complete(future)
# #asyncio.get_event_loop().run_forever()
