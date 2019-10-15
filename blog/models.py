from django.db import models
from django.utils import timezone

class Entrada(models.Model):
    autor = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 100)
    contenido = models.TextField()
    informacion = models.TextField(blank = True)
    imagen = models.CharField(blank = True, max_length = 150)
    # imagen = models.ImageField(blank = True, upload_to="archivo")
    enlace = models.CharField(blank = True, max_length = 200)
    fecha = models.DateTimeField(auto_now_add = True)

    fecha_creacion = models.DateTimeField(default = timezone.now)
    fecha_publicacion = models.DateTimeField(blank = True, null = True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    entrada = models.ForeignKey('blog.Entrada', related_name='comentarios', on_delete = models.CASCADE)
    autor = models.CharField(max_length = 100)
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(default = timezone.now)
    aprovado = models.BooleanField(default = True)

    def aprovar(self):
        self.aprovado = True
        self.save()

    def __str__(self):
        return self.texto

class Serie(models.Model):
    autor = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 100)
    poster = models.CharField(max_length = 150)
    capturaUno = models.CharField(max_length = 150)
    capturaDos = models.CharField(max_length = 150)
    capturaTres = models.CharField(max_length = 150)
    capturaCuatro = models.CharField(max_length = 150)
   # poster = models.ImageField(upload_to="series")
   # capturaUno = models.ImageField(upload_to="archivo")
   # capturaDos = models.ImageField(upload_to="archivo")
   # capturaTres = models.ImageField(upload_to="archivo")
   # capturaCuatro = models.ImageField(upload_to="archivo")
    creador = models.CharField(max_length = 100)
    franquicia = models.CharField(max_length = 100)
    emision = models.CharField(max_length = 100)
    episodios = models.CharField(max_length = 100)
    sipnosis = models.TextField()
    enlace = models.CharField(max_length = 100)
    activa = models.BooleanField(default = True)

    def finalizar(self):
        self.activa = False
        self.save()
    
    def __str__(self):
        return self.titulo