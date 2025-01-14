from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
            return self.nombre

class Noticia(models.Model):
    autor= models.ForeignKey('auth.user',on_delete=models.CASCADE)
    titulo=models.CharField(max_length=250)
    contenido=models.TextField()
    img= models.ImageField(null=True,blank=True,upload_to='img/noticias',help_text='Seleccione una imagen para mostrar')
    creado=models.DateTimeField(default=timezone.now)
    modificado= models.DateTimeField(auto_now=True)
    publicado=models.DateTimeField(blank=True,null=True)
    categorias=models.ManyToManyField('Categoria',related_name='Noticias')
    
    def publicarLaNoticia(self):
        self.publicado= datetime.now()  
        self.save
    
    def comentariosAprobados(self):
        return self.comentariosAprobados(aprobado=True)
    def __str__(self):
        return self.titulo    
    
class Comentarios(models.Model):
    noticia=models.ForeignKey('Noticia', related_name='comentarios',on_delete=models.CASCADE)
    autor=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    texto_comentario= models.TextField()
    creado=models.DateTimeField(default=timezone.now)
    aprobado=models.BooleanField(default=False)
    
    def aprobarcomentario(self):
        self.aprobado=True
        self.save()
    
    def __str__(self):
        return str(self.texto_comentario)

