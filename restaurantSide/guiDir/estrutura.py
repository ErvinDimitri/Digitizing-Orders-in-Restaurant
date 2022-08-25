from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk

class GuiApp(Tk):
    def __init__(self, *args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
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
        self.show_frame("MainWindow")

    def show_frame(self,page_name):
        frame=self.frames[page_name]
        frame.tkraise()

class MainWindow(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        bItens = Button(self, text="Itens", command=lambda: controller.show_frame('ItensWindow'))
        bItens.pack()
        bImpres = Button(self, text="Impressora", command=lambda: controller.show_frame('ImpressoraWindow'))
        bImpres.pack()

class ItensWindow(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        bVoltar = Button(self, text="Voltar", command=lambda: controller.show_frame('MainWindow'))
        bVoltar.pack()

class ImpressoraWindow(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        bVoltar = Button(self, text="Voltar", command=lambda: controller.show_frame('MainWindow'))
        bVoltar.pack()
if __name__=='__main__':
    app=GuiApp()
    app.mainloop()