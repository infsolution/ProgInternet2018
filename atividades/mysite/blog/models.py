from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

class Entry(models.Model):
    headline = models.CharField(max_length=50)
    body_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
class Usuario(models.Model):
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=50)
    nasc_date = models.DateField(auto_now_add=False)

class Perfil(models.Model):
    nome = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Postagem(models.Model):
    texto = models.TextField()
    pud_date = models.DateField(auto_now_add=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    def __str__(self):
        return self.texto
class Comentario(models.Model):
    texto = models.CharField(max_length=1055)
    pub_date = models.DateField(auto_now_add=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    def __str__(self):
        return self.texto
    

class Reacao(models.Model):
    TIPO=(
        ('CURTIR', 'curtir'),
        ('AMEI', 'amei'),
        ('XINGAR', 'Xingar'),
        ('ABRAÇAR', 'Abraçar'),
        ('GARGALHADA','Gargalhada'),
        ('TRISTE','Iriste'),
        ('IRRITADO','Irritado'),
        ('IN]MPRESSIONADO', 'Impressionado')
    )
    tipo = models.CharField(max_length=50, choices=TIPO, default='CURTIR')
    reacao_date = models.DateField(auto_now_add=True)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE)
    peso = models.IntegerField(default=0)


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    data_published = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title