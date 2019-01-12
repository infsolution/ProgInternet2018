"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from games.models import Game
from games.serializers import GameSerializer
from datetime import datetime
from django.utils import timezone

@api_view(['GET', 'POST'])
def game_list(request):
	if request.method == 'GET':
		games = Game.objects.all()
		games_serializer = GameSerializer(games, many=True)
		return Response(games_serializer.data)
	elif request.method == 'POST':
		games_serializer = GameSerializer(data=request.data)
		if games_serializer.is_valid():
			games_serializer.save()
			return Response(games_serializer.data, status=status.HTTP_201_CREATED)
		return Response(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])
def game_detail(request, game_id):
	now = timezone.make_aware(datetime.now(),timezone.get_current_timezone())
	try:
		game = Game.objects.get(id=game_id)
	except Game.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		game_serializer = GameSerializer(game)
		return Response(game_serializer.data)
	elif request.method =='PUT':
		game_serializer = GameSerializer(game, data=request.data)
		if game_serializer.is_valid():
			game_serializer.save()
			return Response(game_serializer.data)
		return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		if game.release_date > now:
			game.delete()
			return Response(status=status.HTTP_202_ACCEPTED)#status.HTTP_204_NO_CONTENT
		return Response(status=status.HTTP_412_PRECONDITION_FAILED)