from django.db import models

# Create your models here.
class Taom(models.Model):
    nomi = models.CharField(max_length=25)
    tavsifi = models.TextField()
    narxi = models.DecimalField(max_digits=19,decimal_places=2)
    mavjudligi = models.BooleanField()
    kategoriya = models.CharField(choices=[("salat","Salat"),("main_food","Main_food"),("shirinlik","Shirinlik")])
    rasm = models.ImageField()
    
def __str__(self):
    return self.nomi
