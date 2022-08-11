from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to = 'uploads/images' , null= False, blank= False)
    name =models.CharField(max_length=150, null=True , blank=False)
    price =models.DecimalField(max_digits=7 , decimal_places=2)
    description=models.TextField(max_length=50 ,null= False , blank= True)
    Category = models.CharField(max_length=50 , null=False, blank= False)
    
    def __str__(self):
        return self.name