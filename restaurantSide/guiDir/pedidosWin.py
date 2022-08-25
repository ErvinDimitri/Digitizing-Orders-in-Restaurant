import tkinter as tk
from tkinter import ttk
import csv
window=tk.Tk()
window.title('Historico de Pedidos')
window.iconbitmap('icon/icon1.ico')

import ctypes
ctypes.windll.user32.MessageBoxW(0,'Opaaaaaaa','Titulo',0) #(0,text,title,style)

bgImage=tk.PhotoImage(file='icon/bg.png')
bgLabel=tk.Label(window, image=bgImage)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
window.resizable(width=False,height=False)
# container = ttk.Frame(window,height=400, width=300, highlightthickness=1,)
container = tk.Canvas(window,height=400, width=400, highlightthickness=5,highlightbackground='blue')

canvas=tk.Canvas(container, height=300, width=300)#, highlightthickness=1,highlightbackground='blue')
scrollbar=ttk.Scrollbar(container,orient="vertical", command=canvas.yview)
scrollable_frame=ttk.Frame(canvas)
scrollable_frame.bind("<Configure>", lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

ttk.Label(window,text='Pedidos: ',font=('Times New Roman',25)).pack(ipady=30,padx=0.9)

order=''
with open('logPedidos.csv','r') as textfile:
    for row in reversed(list(csv.reader(textfile))):
        print(row)
        comida = row[1].replace('#', '\n')
        bebida = row[2].replace('#', '\n')
        if comida!='':
            comida='Comida:\n' + comida
        if bebida != '':
            bebida='Bebidas:\n'+bebida

        order='Mesa: '+str(row[0])+'\tData: '+str(row[3][:16])+'\n'+comida+'\n'+bebida+'\n\n\t\t***\n'
        #Cada msg num container

        ttk.Label(scrollable_frame,text=order,font=('Times New Roman',15)).pack()
container.pack(pady=30)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


window.mainloop()









# window.geometry('350x250')
# ttk.Label(window,text='Pedidos: ',font=('Times New Roman',15)).grid(column=0,row=15,padx=10,pady=25)
#
# order=''
# with open('logPedidos.csv','r') as textfile:
#     for row in reversed(list(csv.reader(textfile))):
#         print(row)
#         comida = row[1].replace('#', '\n')
#         bebida = row[2].replace('#', '\n')
#         if comida!='':
#             comida='Comida:\n' + comida
#         if bebida != '':
#             bebida='Bebidas:\n'+bebida
#
#         order+='Mesa: '+str(row[0])+'\tData: '+str(row[3][:16])+'\n'+comida+'\n'+bebida+'\n\n\n'
#         #Cada msg num container
#
# ttk.Label(window,text=order,font=('Times New Roman',15)).grid(column=0,row=20,padx=10,pady=25)
#
# window.mainloop()