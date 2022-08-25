import asyncio,websockets
import win32api
import win32print
import requests
from requests.auth import HTTPBasicAuth
import sys

file=open('impressoraDefault.txt','r')
printers=eval(file.readline())
file.close()
uri = "ws://localhost:6789"
# wb=websockets.connect(uri)
baseURL='http://localhost:8000/'
# baseURL='http://34.121.93.217/'
def sendToPrinters(pedidos):
    pedidos=eval(pedidos)
    print('----\n',pedidos,'\n------')
    impComida=' Mesa: '+str(pedidos[0]['mesa'])+'\n'
    impBebida=' Mesa: '+str(pedidos[0]['mesa'])+'\n'

    for pedido in pedidos:
        qty = int(pedido['qty'])
        order=str(pedido['item']) + '(x'+ str(qty)+ ').......' + str(qty * float(pedido['valor']))+'\n'
        if pedido['tipo']=='Comida':
            impComida+=order
        else:
            impBebida += order

    if impComida != ' Mesa: '+str(pedidos[0]['mesa'])+'\n':
        impComida+=str(printers['Comida'])
        file=open('impComida.txt','w')
        file.write(impComida)
        file.close()
        print(impComida)
        # win32api.ShellExecute(0, "printto", 'impComida.txt', '"%s"' % printers['Comida'], ".", 0)

    if impBebida != ' Mesa: '+str(pedidos[0]['mesa'])+'\n':
        impBebida+=str(printers['Bebida'])
        file = open('impBebida.txt', 'w')
        file.write(impBebida)
        file.close()
        print(impBebida)
        # win32api.ShellExecute(0, "printto", 'impBebida.txt', '"%s"' % printers['Bebida'], ".", 0)




def ordem(pedidoTotal):
    pedidos=eval(pedidoTotal)
    print('------ New Order ------')
    for pedido in pedidos:
        qty=int(pedido['qty'])
        print(pedido['item'],' Quantidade: ',qty,' Valor a Pagar: ',qty*float(pedido['valor']),' Mesa: ',pedido['mesa'])
    print('------  ------')


async def recebePedido():
    async with websockets.connect(uri) as websocket:
        while True:
            pedido= await websocket.recv()
            # ordem(pedido)
            sendToPrinters(pedido)
# asyncio.get_event_loop().run_until_complete(recebePedido())
# #asyncio.get_event_loop().run_forever()

def getItens():
    # a = requests.get('http://localhost:8000/VintageCorner/lista', auth=HTTPBasicAuth('usuario_vc', '147VINzxc'))
    # a = requests.get('http://35.193.130.254:80/VintageCorner/lista', auth=HTTPBasicAuth('usuario_vc', '147VINzxc'))
    a = requests.get(baseURL+'VintageCorner/lista', auth=HTTPBasicAuth('usuario_vc', '147VINzxc'))


    listaItens = eval(a.text)
    print('---- ', listaItens)
    listaItens = listaItens['lista']
    # for i in listaItens: # Atencao - Disponivel esta como STRING !!!!!!!!!
    return listaItens

def alterar(updates):
    # url='http://localhost:8000/VintageCorner/js'
    # url='http://35.193.130.254:80/VintageCorner/js'
    url=baseURL+'VintageCorner/js'

    client=requests.session()
    p=client.get(url)
    if 'csrftoken' in client.cookies:
        csrftoken=client.cookies['csrftoken']
        # putData=dict(id="6",preco="45",disponivel="sim",user="usuario_vc",pasW="147VINzxc", csrfmiddlewaretoken=csrftoken)
        putData=dict(updates=str(updates),user="usuario_vc",pasW="147VINzxc", csrfmiddlewaretoken=csrftoken)
        headers={'Referer':url}
        a=client.post(url,data=putData,headers=headers, auth=HTTPBasicAuth('usuario_vc','147VINzxc'))
    else:
        print('failed')