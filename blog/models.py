from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='media/product', null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    orgin =  models.TextField(max_length=1000, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    def get_name(self):
        return self.name
    def get_img(self):
        return self.img
    def get_price(self):
        return self.price
    def get_descripion(self):
        return self.description

