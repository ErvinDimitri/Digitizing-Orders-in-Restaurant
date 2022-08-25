from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ItensMenu,Pedido
import vintagecorner.operationsDB as oDB
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import traceback
token=''
def index(request):
	global token
	itens= ItensMenu.objects.all()
	itensOrg=sorted(itens,key=lambda x:x.ordem)
	# getAtrib=lambda atributo:[getattr(i,atributo) for i in itensOrg]  #Ciclos for comecando com categoria,sub, produtos
	# getCateg=set(getAtrib('categoria'))
	# getSubCateg = set(getAtrib('subcategoria'))
	getCateg=[]
	cat=[]
	getSubCateg=[]
	subcat=[]
	bebida=''
	for i in itensOrg:
		if i.categoria not in getCateg:
			cat.append(i.itemPort)
			getCateg.append(i.categoria)
		if i.subcategoria not in getSubCateg:
			subcat.append(i.itemPort)
			getSubCateg.append(i.subcategoria)
		if i.tipo == 'Bebida' and bebida == '':
			bebida = i.itemPort

	itensAgroup = []
	# for i in itensOrg:
	# 	if i.categoria not in getCateg:
	# 		getCateg.append(i.categoria)
	# 	if i.subcategoria not in getSubCateg:
	# 		getSubCateg.append(i.subcategoria)

	subcategL = []
	for isub in getSubCateg:
		l=[]
		for i in itensOrg:
			if i.subcategoria == isub:
				l.append(i)
		subcategL.append(l)
	# print('sub',subcategL)
	categL=[]
	for icat in getCateg:
		l=[]
		for isub in subcategL:
			if isub[0].categoria == icat:
				l.append(isub)
		categL.append(l)
	# print('cat',categL)
	for itipo in ['Comida','Bebida']:
		l = []
		for icat in categL:
			if icat[0][0].tipo == itipo:
				l.append(icat)
		itensAgroup.append(l)

	# print(itensAgroup)
	if request.POST:
		if token!=request.POST['csrfmiddlewaretoken']:
			print('Possssssst')
			print(request.POST)
			token=request.POST['csrfmiddlewaretoken']
	else:

		print('Voltou pra qui')
	# return render(request, 'vintageWP1.html', {'itens':itensOrg})
	# print(getCateg,getSubCateg)
	# for ob in itensOrg:
	# 	print(ob.categoria)

	return render(request, 'vincor.html', {'itens':itensAgroup,'tipoJ':bebida,'cat':cat,'subcat':subcat})

def sendOrder(request):
	#/vintageWP.html?Pedido1=&Pedido2=&Bolos_null=11&Bolos_null=22&Bolos_null=33&Enviar=Submit
	#tml?Pedido1=&Pedido2=&Bolos_1=qqQ&Bolos_1=ww&Bolos_1=eee&Enviar=Submit
	pedidos = request.POST
	print('Pedidossssss ',pedidos)
	itensL=list(pedidos)
	itensL.pop(0)
	nr=0

	for i in itensL:
		if '_' in i:
			nr+=1
	getUrl=''
	for pedido in itensL:
		if '_' in pedido:
			item,mesa=pedido.split('_')
			getUrl=mesa
			if type(item)==list:
				item=item[0]
			if '+' in pedido:
				pedido=pedido.replace('+',' ')
			qty=pedidos[pedido]
			item=oDB.searchItem(item)
			mesa=oDB.searchMesa(mesa)
			if mesa=='error':
				getUrl = ''
				break
			ordem=Pedido(item=item,mesa=mesa,qty=qty,total_itens=nr)
			ordem.save()

#Redirect...
	next=request.POST.get('next','/')
	if getUrl != '':
		next+='?mesa='+getUrl
	return HttpResponseRedirect(next)

@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def listaItens(request):
	# print('------\n',request.user)
	if request.user.is_authenticated:
		lista=oDB.getAll()
		return Response({'lista':lista})
	else:
		print('No')
	return Response({'error'})

# @permission_classes((IsAuthenticated,))
# @api_view(['POST'])
# def req(request):
# 	print('------\n')
# 	ps = request.POST
# 	keys = list(request.POST)
# 	myDict={}
# 	for i in keys:
# 		myDict[i]=ps[i]
# 	print('***')
# 	print(myDict.keys())
# 	print('***')
# 	try:
# 		if myDict['user'] == 'usuario_vc' and myDict['pasW'] == '147VINzxc':
# 			id=myDict['id']
# 			preco=myDict['preco']
# 			disp=myDict['disponivel']
# 			oDB.id(id,[preco,disp])
# 			# UPDATE vintagecorner_itensmenu
# 			# SET disp=false
# 			# WHERE id=id
#
# 	except:
# 		for i in myDict:
# 			print(i)
# 		print(traceback.format_exc())
# 	print('----------\n')
#
# 	return render(request, 'submit.html')

def req(request):
	ps = request.POST
	keys = list(request.POST)
	myDict={}
	for i in keys:
		myDict[i]=ps[i]
	try:
		if myDict['user'] == 'usuario_vc' and myDict['pasW'] == '147VINzxc':
			updates=eval(myDict['updates'])
			for i in updates:
				iDict=updates[i]
				id=i
				oDB.id(id,iDict)
			print('Success')

	except:
		print(myDict)
		print(traceback.format_exc())

	return render(request, 'submit.html')

d={'updates': {2: ['35', '-'], 5: ['35', 'nao']}, 'user': 'usuario_vc', 'pasW': '147VINzxc', 'csrfmiddlewaretoken': 'boIsRdvgGiA1eDP5apTVN5U6Qk0n8gUzMwgAwx5hYX36GHHbcXoTYPCoizbYpRSk'}
#updates  {4: ['35', 'NAO'], 6: ['35', '-']}
#mydict  {'updates': '6', 'user': 'usuario...
#<QueryDict: {'updates': ["{3: ['35', 'nao'], 5: ['35', '-']}"], 'user': ['