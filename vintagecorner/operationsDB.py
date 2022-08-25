from django.shortcuts import render
from .models import ItensMenu,Pedido,Mesa
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
conn = psycopg2.connect(database='fullmotion_db', user='postgres', password='5519', host='localhost',port='5432')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

def searchItem(item):
    itemObj=ItensMenu.objects.filter(itemPort=item)
    itemObj=itemObj[0]
    return itemObj
def searchItemID(item):
    itemObj=ItensMenu.objects.filter(id=item)
    itemObj=itemObj[0]
    return itemObj

def searchMesa(mesa):
    try:
        mesaObj = Mesa.objects.filter(nome=mesa)
        mesaObj = mesaObj[0]
        return mesaObj
    except:
        return 'error'

def searchPedido(id):
    pedidoObj = Pedido.objects.filter(id=id)
    pedidoObj = pedidoObj[0]
    return pedidoObj

def id(id,itens):
    alterar=''
    if itens[0]!='-':
        alterar+='preco='+itens[0]+' '
        if itens[1]!='-':
            alterar += ','
    if itens[1]!='-':
        valor=itens[1].lower()
        if valor=='sim':
            valor='true'
        else:
            valor='false'
        alterar+='disponivel='+valor

    cur.execute("UPDATE vintagecorner_itensmenu SET "+str(alterar)+" WHERE id="+str(id))

def getAll():
    cur.execute("SELECT * FROM vintagecorner_itensmenu ORDER BY ordem")
    query = cur.fetchall()
    totalItens=[]
    for item in query:
        totalItens.append([item[0],item[1],float(item[6]),str(item[7])]) #.capitalize()
    return totalItens
