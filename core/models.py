from django.db import models

# Create your models here.
class Camiseta(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    detalle = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    oferta = models.BooleanField()
    imagen = models.CharField(max_length=200)

    def descuento15(self):
        if self.oferta:
            print("$"+str(round(self.precio * 1.15)))
            return "$"+str(round(self.precio * 1.15))
        return ""
    def descuento10(self):
        if self.oferta:
            return "$"+str(round(self.precio * 1.1))
        return ""

class Accesorio(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    detalle = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    oferta = models.BooleanField()
    imagen = models.CharField(max_length=200)
    
    def descuento15(self):
        if self.oferta:
            print("$"+str(round(self.precio * 1.15)))
            return "$"+str(round(self.precio * 1.15))
        return ""
    def descuento10(self):
        if self.oferta:
            return "$"+str(round(self.precio * 1.1))
        return ""
    

class Tour(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    detalle = models.CharField(max_length=200)
    precio = models.IntegerField()
    imagen = models.CharField(max_length=200)
    hora = models.CharField(max_length=50)
    
    
    

    
    def __str__(self):
        return self.detalle+"("+self.codigo+")"
