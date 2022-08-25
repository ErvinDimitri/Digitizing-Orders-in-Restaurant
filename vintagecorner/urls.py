from django.urls import path
from . import views

urlpatterns=[
	path('', views.index, name='mainPage'),
	path('sendOrder', views.sendOrder, name='sendOrder'),
	path('js', views.req, name='httpRes'),
	path('lista', views.listaItens, name='lista')

]