from django.db import models

# Create your models here.

class Project(models.Model):
    
    title=models.CharField(max_length=200,verbose_name='Titulo')
    des =models.TextField()
    creacion =models.DateTimeField(auto_now_add=True)
    modifica =models.DateTimeField(auto_now=True)
    class Meta:
            verbose_name= "Proyecto"
            verbose_name_plural= "Proyectos"

    def __str__(self):
         return self.title