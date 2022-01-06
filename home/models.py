from django.db import models
from django.urls import reverse
# from PIL import Image

# Create your models here.
class Category(models.Model):
    name = models.CharField( max_length=100)
    slug = models.SlugField(unique=True)
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product:product_list_category", args={ self.slug})
    


class Product(models.Model):
    name = models.CharField( max_length=100)
    image  = models.ImageField(upload_to = 'pictures/', blank = True, null = True,)
    price  = models.FloatField()
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)   
    date_created  = models.DateTimeField( auto_now=True) 
    discount_price =  models.FloatField()
    description =models.TextField()
    
    
    
    
    class Meta:
        
        ordering = ('-id',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product:product_detail", args=[self.id,])
    
    
    
    # @property
    # def my_image(self):

    #     if self.image :
    #         return self.image.url
    #     return ''
        
        