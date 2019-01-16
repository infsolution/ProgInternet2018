from accounts.serializers import AccountSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from .models import Account

@api_view(['GET', 'POST'])
def account_list(request):
	if request.method == 'GET':
		accounts = Account.objects.all()
		accounts_serializer = AccountSerializer(accounts, many=True)
		return Response(accounts_serializer.data)
	if request.method == 'POST':
		
		ac_serializer = AccountSerializer(data=request.data)
		if ac_serializer.is_valid():
			ac_serializer.save()
			return Response(ac_serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT', 'GET', 'DELETE', 'PATCH'])
def account_detail(request, account_id):
	try:
		account = Account.objects.get(id=account_id)
	except Account.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		accounts_serializer = AccountSerializer(account)
		return Response(accounts_serializer.data)
	elif request.method == 'PUT':
		accounts_serializer = AccountSerializer(account, data=request.data)
		if accounts_serializer.is_valid():
			accounts_serializer.save()
			return Response(accounts_serializer.data)
		return Response(accounts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
	elif request.method == 'DELETE':
		account.delete()
		return Response(status=status.HTTP_202_ACCEPTED)#status.HTTP_204_NO_CONTENT
		#return Response(status=status.HTTP_412_PRECONDITION_FAILED)
	elif request.method == 'PATCH':

		if request.data['balance']>0:
			account.balance = account.balance + request.data['balance']
			account.save()
			return Response(status=status.HTTP_202_ACCEPTED)
		elif request.data['balance'] < 0:
			if request.data['balance'] <= account.balance:
				account.balance = (account.balance + request.data['balance'])
				account.save()
				return Response(status=status.HTTP_202_ACCEPTED)
			else:
				return Response(status=status.HTTP_412_PRECONDITION_FAILED)
		elif request.data['balance'] == 0:
			return Response(status=status.HTTP_412_PRECONDITION_FAILED)