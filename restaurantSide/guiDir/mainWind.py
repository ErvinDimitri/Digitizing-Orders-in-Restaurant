from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk

def itensM(event):
    pass

def impressoraM(event):
    pass
#-----------------------Evitar o usuario mexer na resolucao da tela
root = Tk()
root.minsize(600, 300)
root.geometry("600x450+534+207")
mainFrame=Frame(root,bg="blue")
mainFrame.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.03)

itensBTN=Button(mainFrame, text='Itens')
itensBTN.place(relx=0.2, rely=0.3, relheight=0.2, relwidth=0.3)
itensBTN.bind('<Button-1>',itensM)

impBTN=Button(mainFrame, text='Impressora')
impBTN.place(relx=0.6, rely=0.3, relheight=0.2, relwidth=0.3)
impBTN.bind('<Button-1>',itensM)

root.mainloop()