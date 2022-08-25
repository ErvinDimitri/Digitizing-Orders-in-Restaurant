from django.db import models

# Create your models here.
class ItensMenu(models.Model):
    itemPort=models.CharField(max_length=100)
    itemIng=models.CharField(max_length=100)
    TIPO_CHOICE=[('Comida','Comida'),('Bebida','Bebida')]
    tipo=models.CharField(choices=TIPO_CHOICE, max_length=100)  #Comida ou Bebida
    CATEGORIA_CHOICE=[('Pizza','Pizza'),('Sobremesas','Sobremesas'),('Com alcool','Com alcool'),('Quentes','Quentes')]
    categoria = models.CharField(choices=CATEGORIA_CHOICE,max_length=40) # Frias, Quentes,com alcool, sem alcool
    SUBCATEGORIA_CHOICE =[('Carne','Carne'),('Vegetariana','Vegetariana'),('Bolos','Bolos'),('Cafe','Cafe'),('Agua','Agua'),('Cerveja','Cerveja'),('Whisky','Whisky')]
    subcategoria = models.CharField(choices=SUBCATEGORIA_CHOICE,max_length=40) #Agua,cerveja,whisky
    preco = models.DecimalField(decimal_places=2,max_digits=6)
    disponivel=models.BooleanField(default=True)
    ORDEM_CHOICE =[(2,'Carne'),(3,'Vegetariana'),(6,'Bolos'),(50,'Agua'),(54,'Cafe'),(59,'Cerveja'),(63,'Whisky')]
    ordem = models.IntegerField(choices=ORDEM_CHOICE,default=0)

    class Meta:
        app_label = 'vintagecorner'  # name of app

class Mesa(models.Model):
    nome=models.CharField(max_length=50)
    nr_cadeiras=models.IntegerField(default=0)

class Pedido(models.Model):
    item=models.ForeignKey(ItensMenu,default=1,on_delete=models.SET_DEFAULT)
    mesa=models.ForeignKey(Mesa,default=1,on_delete=models.SET_DEFAULT)
    qty=models.IntegerField(default=0)
    total_itens=models.IntegerField(default=0)
    data=models.DateTimeField(auto_now=True)