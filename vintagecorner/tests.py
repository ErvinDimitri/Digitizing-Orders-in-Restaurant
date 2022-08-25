# import psycopg2
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
#
# conn = psycopg2.connect(database='fullmotion_db', user='postgres' ,password='5519' ,host='localhost',port='5432')
# # conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cur = conn.cursor()
# cur.execute("SELECT * FROM vintagecorner_pedido WHERE id="+str(2)) #[(2, 5, 1, 3)]
# query= cur.fetchall()[0]
# print(query)
# id,qty,idItem,idMesa=query
# cur.execute("SELECT * FROM vintagecorner_itensmenu WHERE id="+str(idItem)) #[(2, 5, 1, 3)]
# query= cur.fetchall()[0]
# print('Item:: ',query)
# item=query[1]
# tipo=query[3]
# valor=query[6]
# print(item,tipo,valor)
# [(1, 2, 1, 1), (2, 5, 1, 3), (3, 1, 1, 2), (4, 2, 1, 3), (5, 1, 2, 3), (6, 6, 1, 1)]

# {'item': 'Calabresa', 'tipo': 'Comida', 'valor': 580.0, 'qty': 4, 'mesa': 2}
# file=open('printers.txt','r')
# printers=eval(file.readline())
# file.close()
# print(printers['Comida'])
# print(printers['Bebida'])

