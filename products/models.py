from django.db import models


class Products(models.Model):
    """ Modelo de producto del que heredaran los productos
    
        Anotations:
            Al ser una clase abstracta, estano genera ninguna tabla en la db.
    """
    name = models.CharField(max_length=75)
    price = models.FloatField()
    descriptions = models.TextField(blank=True, null=True)
    
    # el status indica si el producto está disponible o no
    status = models.BooleanField(default=True)
    
    class Meta:
        # opción necesaria para poder heredar de este modelo
        abstract = True    
    

def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Fruits(Products):
    
    photo = models.ImageField( upload_to=user_directory_path,blank=True, null=True) 
    
    def __str__(self):
        return self.name
    
    @property
    def get_photo_url(self):
        if self.photo:
            return self.photo.url
        return ''