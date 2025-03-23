from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tecnologias = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='proyectos/', null=True, blank=True)
    enlace = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('principal:proyecto-detalle', kwargs={'pk': self.pk})

