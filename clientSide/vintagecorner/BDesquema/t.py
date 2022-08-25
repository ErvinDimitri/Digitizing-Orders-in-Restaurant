# import requests
# from requests.auth import HTTPBasicAuth
# a = requests.get('http://35.193.130.254:9944/')
# print('-----   ',a)
# class ItensMenu:
# 	def __init__(self):
# 	    self.itemPort:str
# 	    self.itemIng:str
# 	    self.tipo:str #Comida ou Bebida
# 	    self.categoria :str # Frias, Quentes,com alcool
# 	    self.subcategoria :str #Agua,cerveja,whisky
# 	    self.preco :float
# 	    self.disponivel=True
# 	    self.ordem:int
#
# p1=ItensMenu()
# p1.itemPort="Calabresa"
# p1.itemIng="Calabresas"
# p1.tipo="Comida"
# p1.categoria ="Pizza"
# p1.subcategoria ="Carne" #Agua,cerveja,whisky
# p1.preco=500
# p1.disponivel=True
# p1.ordem=1
#
# p2=ItensMenu()
# p2.itemPort="2M"
# p2.itemIng="2M"
# p2.tipo="Bebida"
# p2.categoria ="Com alcool"
# p2.subcategoria ="Cerveja"
# p2.preco=45
# p2.disponivel=True
# p2.ordem=6
#
# p3=ItensMenu()
# p3.itemPort="Capuccino"
# p3.itemIng="Capuccino"
# p3.tipo="Bebida"
# p3.categoria ="Quente"
# p3.subcategoria ="Cafe"
# p3.preco=45
# p3.disponivel=True
# p3.ordem=5
#
# p5=ItensMenu()
# p5.itemPort="4 Estacoes"
# p5.itemIng="4 Seasons"
# p5.tipo="Comida"
# p5.categoria ="Pizza"
# p5.subcategoria ="Vegetariana"
# p5.preco=600
# p5.disponivel=True
# p5.ordem=3
#
# itens=[p1,p2,p3,p5]
#
# organ=sorted(itens,key=lambda x:x.ordem)
#
# for x in organ:
# 	print(x.itemPort)
#
# a=input('Waiting....')

# import psycopg2
# import datetime
# d='datetime.datetime(2021, 1, 8, 1, 12, 18, 558095, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=120, name=None))'
# d=eval(d)
# print(d.day)
l=[4,50]
l.insert(0,30)
print(l)

import csv
with open('logPedidos.csv','r') as textfile:
    for row in reversed(list(csv.reader(textfile))):
        print(','.join(row))