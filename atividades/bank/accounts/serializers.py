from rest_framework import serializers
from .models import Account
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('id','owner', 'balance','creation_date')
	def validate(self,data):
		if data['balance'] < 0:
			raise serializers.ValidationError('Saldo menor que 0')
		elif data['creation_date'] != timezone.now:
			raise serializers.ValidationError('Data diferente da atual')
		return data

	def update(self,instance,validated_data):
		instance.balance=validated_data.pop('balance',instance.balance)
		super().update(instance, validated_data)
		instance.save()

class AccountUpdate(UpdateModelMixin,GenericAPIView):
	serializer_class = AccountSerializer
	model = Account
	lookup_field = 'balance'
	def patch(self,request,*args,**kwargs):
		return self.partial_update(request,*args,**kwargs)