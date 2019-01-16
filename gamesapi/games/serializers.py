from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Game
class GameSerializer(serializers.ModelSerializer):
	#name = serializers.CharField(max_length=200, validators=[UniqueValidator(queryset=Game.objects.all(), message="This name already")])
	game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(),slug_field='name')
	class Meta:
		model = Game
		fields = ('url', 'game_category', 'name', 'release_date', 'played')

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
	model = Score
	fields = ('url',	' pk', 'score', 'score_date', 'player', 'game')