from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk



def itensM(event):
    import tkinter as tk
    import random

    def grid_loc():
        print('location: ')

    class Example(tk.Frame):
        def entryupdate(self, pvar, idItem, col):
            print(idItem, col)
            clicks.append((idItem, col))

        def cancelM(self):
            pass

        def __init__(self, parent):
            tk.Frame.__init__(self, parent)
            b = tk.Button(self, text="Salvar", command=self.upload_cor)
            b.pack()
            cancelar = tk.Button(self, text="Cancelar", command=self.cancelM)
            cancelar.pack()
            table = tk.Frame(self)
            table.pack(side="top", fill="both", expand=True)
            self.precoVar = []
            self.disp = []

            words = ['qwer', 'asdf', 'zxcv', 'sdfg', 'vcbn', 'tyui']
            disp = ['sim', 'nao']
            self.data = []
            for i in range(5):
                self.data.append(((i + 1), random.choice(words), random.randint(100, 500), random.choice(disp)))
            self.data = tuple(self.data)
            self.widgets = {}
            row = 1
            i = 0
            self.widgets[0] = {
                "itemCol": tk.Label(table, text='Item'),
                "precoCol": tk.Label(table, text='Preco'),
                "disponivelCol": tk.Label(table, text='Disponivel')
            }
            self.widgets[0]["itemCol"].grid(row=0, column=0, sticky="nsew")
            self.widgets[0]["precoCol"].grid(row=0, column=1, sticky="nsew")
            self.widgets[0]["disponivelCol"].grid(row=0, column=2, sticky="nsew")
            for rowid, item, preco, disponivel in self.data:
                row += 1
                self.precoVar.append(tk.StringVar())
                self.precoVar[i].set(preco)
                self.precoVar[i].trace('w', lambda name, index, mode, var=self.precoVar[i], i=i: self.entryupdate(var,self.data[i][0],'preco'))
                self.disp.append(tk.StringVar())
                self.disp[i].set(disponivel)
                self.disp[i].trace('w', lambda name, index, mode, var=self.disp[i], i=i: self.entryupdate(var,self.data[i][0],'disponivel'))
                self.widgets[rowid] = {
                    "item": tk.Label(table, text=item),
                    "preco": tk.Entry(table, textvariable=self.precoVar[i]),
                    "disponivel": tk.Entry(table, text=self.disp[i]),
                }

                self.widgets[rowid]["item"].grid(row=row, column=0, sticky="nsew")
                self.widgets[rowid]["preco"].grid(row=row, column=1, sticky="nsew")
                self.widgets[rowid]["disponivel"].grid(row=row, column=2, sticky="nsew")
                i += 1
            table.grid_columnconfigure(1, weight=1)
            table.grid_columnconfigure(2, weight=1)
            # invisible row after last row gets all extra space
            table.grid_rowconfigure(row + 1, weight=1)

        def upload_cor(self):
            global clicks
            clicks1 = list(set(clicks))
            alteracaoDict = {}
            for alteracao in clicks1:
                try:
                    if alteracaoDict[alteracao[0]]:
                        alteracaoDict[alteracao[0]].append(alteracao[1])
                        alteracaoDict[alteracao[0]].sort(reverse=True)
                except:
                    alteracaoDict[alteracao[0]] = [alteracao[1]]
            sendDict = {}
            for i in alteracaoDict:
                pos = 0
                for k in range(len(self.data)):
                    if self.data[k][0] == int(i):
                        pos = k
                        break
                if 'preco' in alteracaoDict[i]:
                    preco = self.precoVar[pos].get()
                else:
                    preco = '-'
                if 'disponivel' in alteracaoDict[i]:
                    disp = self.disp[pos].get()
                else:
                    disp = '-'
                sendDict[i] = [preco, disp]
            print(alteracaoDict)
            print(sendDict)
            clicks = []

    if __name__ == "__main__":
        clicks = []
        itensTopLevel = Toplevel(root)
        Example(itensTopLevel).pack(fill="both", expand=True)

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