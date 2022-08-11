from django.db import models
from django.conf import settings
# Create your models here.
CATEGORY_CHOICES = (
    ('Sportif','sportif'),
    ('Culturel','culturel'),
)
class Evenements(models.Model):   
    photo = models.ImageField(upload_to = 'uploads/images' , null= False, blank=True)
    utilisateur= models.ForeignKey(settings.AUTH_USER_MODEL,null=True,on_delete=models.CASCADE)
    titre =models.CharField(max_length=150, null=True , blank=False)
    description=models.TextField(max_length=50 ,null= False , blank= True)
    type=models.CharField(max_length=200,null=True,choices=CATEGORY_CHOICES)
    date = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.titre