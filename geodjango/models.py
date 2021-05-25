from django.db import models

class Commande(models.Model):
    mail = models.CharField(max_length=250)
    passw = models.CharField(max_length=250)
    dat = models.DateField(max_length=50)
    message = models.TextField(max_length=500)
    part = models.CharField(max_length=250)
    ent = models.CharField(max_length=250)
    inv = models.CharField(max_length=250)
    ver = models.BooleanField(max_length=8)

    def __str__(self):
        return self.mail


 