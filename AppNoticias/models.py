from django.db import models
from django.contrib.auth.models import User

class NotasNoticias(models.Model):
    NotasNoticiasSeleccion = (
    ('deporte','Deporte'),
    ('politica', 'Politica'),
    ('farandula','Farandula'),
    ('tecnologia','Tecnologia'),
    ('ciencia','Ciencia'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    noticia = models.CharField(max_length=15, choices=NotasNoticiasSeleccion, default='deportes')
    descripcion = models.TextField(null=False, blank=False)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()
    imagenNoticias = models.ImageField(null=False, blank=False, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    comentario = models.ForeignKey(NotasNoticias, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=False, blank=False)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)