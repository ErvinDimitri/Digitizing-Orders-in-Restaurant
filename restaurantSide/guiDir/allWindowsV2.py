from tkinter import ttk
from tkinter import *
import random
from PIL import Image,ImageTk

class GuiApp(Tk):
    def __init__(self, *args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        self.minsize(600, 300)
        self.geometry("600x450+534+207")
        container=Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        for F in (MainWindow,ItensWindow,ImpressoraWindow):
            page_name=F.__name__
            frame=F(parent=container,controller=self)

            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky='nsew')
            # frame.grid_columnconfigure(10, weight=1)
            # frame.grid_rowconfigure(3, weight=1)

        self.show_frame("MainWindow")

    def show_frame(self,page_name):
        frame=self.frames[page_name]
        frame.tkraise()

class MainWindow(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        # self.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.03)
        bItens = Button(self, text="Itens", command=lambda: controller.show_frame('ItensWindow'))
        bItens.place(relx=0.2, rely=0.3, relheight=0.2, relwidth=0.3)

        # bItens.pack()
        bImpres = Button(self, text="Impressora", command=lambda: controller.show_frame('ImpressoraWindow'))
        bImpres.place(relx=0.6, rely=0.3, relheight=0.2, relwidth=0.3)

        # bImpres.pack()

class ItensWindow(Frame):
    def entryupdate(self, pvar, idItem, col):
        print(idItem, col)
        self.clicks.append((idItem, col))

    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        bVoltar = Button(self, text="Cancelar", command=lambda: controller.show_frame('MainWindow'))
        bVoltar.pack()
        b =  Button(self, text="Salvar", command=self.upload_cor)
        b.pack()
        table =  Frame(self)
        table.pack(side="top", fill="both", expand=True)
        self.precoVar = []
        self.disp = []
        self.clicks=[]

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
            "itemCol":  Label(table, text='Item'),
            "precoCol":  Label(table, text='Preco'),
            "disponivelCol":  Label(table, text='Disponivel')
        }
        self.widgets[0]["itemCol"].grid(row=0, column=0, sticky="nsew")
        self.widgets[0]["precoCol"].grid(row=0, column=1, sticky="nsew")
        self.widgets[0]["disponivelCol"].grid(row=0, column=2, sticky="nsew")
        for rowid, item, preco, disponivel in self.data:
            row += 1
            self.precoVar.append( StringVar())
            self.precoVar[i].set(preco)
            self.precoVar[i].trace('w', lambda name, index, mode, var=self.precoVar[i], i=i: self.entryupdate(var,self.data[i][ 0],'preco'))
            self.disp.append( StringVar())
            self.disp[i].set(disponivel)
            self.disp[i].trace('w', lambda name, index, mode, var=self.disp[i], i=i: self.entryupdate(var,self.data[i][0],'disponivel'))
            self.widgets[rowid] = {
                "item":  Label(table, text=item),
                "preco":  Entry(table, textvariable=self.precoVar[i]),
                "disponivel":  Entry(table, text=self.disp[i]),
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
        clicks1 = list(set(self.clicks))
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
        self.clicks = []
        self.controller.show_frame('MainWindow')


class ImpressoraWindow(Frame):
    def salvar(self,event):
        # print(event)
        comida = self.impComidaCB.get()
        bebida = self.impBebidaCB.get()
        if self.impressoras['Comida'] != comida:
            self.impressoras['Comida'] = comida
        if self.impressoras['Bebida'] != bebida:
            self.impressoras['Bebida'] = bebida
        file = open('impressoraDefault.txt', 'w')
        file.write(str(self.impressoras))
        file.close()
        self.controller.show_frame('MainWindow')

    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        salvarBtn = Button(self, text="Salvar")
        salvarBtn.grid(column=0,row=23)
        salvarBtn.bind('<Button-1>',self.salvar)
        bVoltar = Button(self, text="Voltar", command=lambda: controller.show_frame('MainWindow'))
        bVoltar.grid(column=1,row=23)
        file = open('impressoraDefault.txt', 'r')
        try:
            self.impressoras = eval(file.read())
        except:
            self.impressoras = {'Comida': 'impComida', 'Bebida': 'impBebida'}
        file.close()

        impComDisp = ('imp1', 'impComida', 'impQ', 'imp3', 'imp5')
        self.defaultCom = 0
        if self.impressoras['Comida'] in impComDisp:
            self.defaultCom = impComDisp.index(self.impressoras['Comida'])

        impBebDisp = ('impAA', 'impZZ', 'impRR', 'impBebida', 'impKK')
        self.defaultBeb = 0
        if self.impressoras['Bebida'] in impBebDisp:
            self.defaultBeb = impBebDisp.index(self.impressoras['Bebida'])

        ttk.Label(self, text='Impressora para Comida: ', font=('Times New Roman', 10)).grid(column=0, row=15, padx=10,
                                                                                              pady=25)
        self.n = StringVar()
        self.impComidaCB = ttk.Combobox(self, width=27, textvariable=self.n)
        self.impComidaCB['values'] = impComDisp
        self.impComidaCB.grid(column=1, row=15)
        self.impComidaCB.current(self.defaultCom)

        ttk.Label(self, text='Impressora para Bebida: ', font=('Times New Roman', 10)).grid(column=0, row=18, padx=10,
                                                                                              pady=25)
        self.bebida = StringVar()
        self.impBebidaCB = ttk.Combobox(self, width=27, textvariable=self.bebida)
        self.impBebidaCB['values'] = impBebDisp
        self.impBebidaCB.grid(column=1, row=18)
        self.impBebidaCB.current(self.defaultBeb)

if __name__=='__main__':
    app=GuiApp()
    app.mainloop()