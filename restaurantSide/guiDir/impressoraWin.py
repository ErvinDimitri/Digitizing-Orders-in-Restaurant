import tkinter as tk
from tkinter import ttk
file=open('impressoraDefault.txt', 'r')
try:
    impressoras=eval(file.read())
except:
    impressoras={'Comida':'impComida','Bebida':'impBebida'}
file.close()

# print(impressoras) #impComida,impBebida
# print(type(impressoras))
def salvar(event):
    global impressoras
    # print(event)
    comida=impComidaCB.get()
    bebida=impBebidaCB.get()
    if impressoras['Comida'] != comida:
        impressoras['Comida']=comida
    if impressoras['Bebida'] != bebida:
        impressoras['Bebida']=bebida
    file = open('impressoraDefault.txt', 'w')
    file.write(str(impressoras))
    file.close()

def cancelar(event):
    pass
impComDisp=('imp1','impComida','impQ','imp3','imp5')
defaultCom=0
if impressoras['Comida'] in impComDisp:
    defaultCom=impComDisp.index(impressoras['Comida'])

impBebDisp=('impAA','impZZ','impRR','impBebida','impKK')
defaultBeb=0
if impressoras['Bebida'] in impBebDisp:
    defaultBeb=impBebDisp.index(impressoras['Bebida'])

window=tk.Tk()
window.geometry('350x250')
ttk.Label(window,text='Impressora para Comida: ',font=('Times New Roman',10)).grid(column=0,row=15,padx=10,pady=25)
n=tk.StringVar()
impComidaCB=ttk.Combobox(window,width=27,textvariable=n)
impComidaCB['values']=impComDisp
impComidaCB.grid(column=1,row=15)
impComidaCB.current(defaultCom)

ttk.Label(window,text='Impressora para Bebida: ',font=('Times New Roman',10)).grid(column=0,row=18,padx=10,pady=25)
bebida=tk.StringVar()
impBebidaCB=ttk.Combobox(window,width=27,textvariable=bebida)
impBebidaCB['values']=impBebDisp
impBebidaCB.grid(column=1,row=18)
impBebidaCB.current(defaultBeb)

saveBTN=tk.Button(window, text='Salvar')
saveBTN.place(relx=0.15, rely=0.48, relheight=0.17, relwidth=0.3)
saveBTN.bind('<Button-1>',salvar)
saveBTN=tk.Button(window, text='Cancelar')
saveBTN.place(relx=0.6, rely=0.48, relheight=0.17, relwidth=0.3)
saveBTN.bind('<Button-1>',cancelar)

window.mainloop()