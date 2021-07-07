from django.db import models

# Create your models here.
class idpais(models.Model):
    idPais = models.IntegerField(primary_key=True, verbose_name='Id Pais')
    nombrepais = models.CharField(max_length=50, verbose_name='Nombre del pais')

    def __str__(self):
        return(self.nombrepais)


class Usuario(models.Model):
    NombreCompleto = models.CharField(max_length=100,  verbose_name='Nombre completo')
    Telefono =models.CharField(max_length=30, verbose_name='Telefono')
    Rut =models.CharField(max_length=10,primary_key=True,verbose_name='RUT')
    Pais=models.ForeignKey(idpais, on_delete=models.CASCADE)
    correo=models.EmailField()
    foto=models.ImageField(upload_to='usuario', blank=True,null=True)
    Direccion=models.CharField(max_length=100,verbose_name='Direccion')



    def __str__(self):
        return(self.Rut)



    



