from django.db import models

# Create your models here.
class Game(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200, blank=True, default='')
	release_date = models.DateTimeField()
	game_category = models.CharField(max_length=200, blank=True, default='')
	played = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class Player(models.Model):
	nome = models.CharField(max_length=200,blank=True, default='')
	genero = models.CharField(max_length=2)
	cadastro = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name

class Score(models.Model):
	player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='scores')
	game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='games')
	value = models.IntegerField(default=0)
	date_value = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.value