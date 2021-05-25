from django.db import models

class Commande(models.Model):
    mail = models.CharField(max_length=250)
    passw = models.CharField(max_length=250)
    
    message = models.TextField(max_length=500)
   
   

    def __str__(self):
        return self.mail

        
