from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255,default=0.00)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='product/', default='default_image.jpg')

    def __str__(self):
        return self.name

class FormContact(models.Model):
    formContact_name = models.CharField(max_length=250, null=True, blank=True)
    formContact_surname = models.CharField(max_length=250, null=True, blank=True)
    formContact_email = models.EmailField(null=True, blank=True)
    formContact_comment = models.TextField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return f"{self.formContact_name} {self.formContact_surname}"
