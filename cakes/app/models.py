from django.db import models

# Create your models here.
# class CategoryChoices(models.TextChoices):
#     BIRTHDAY_CAKES =' Birthday_Cakes','Birthday_Cakes'
#     WEDDING_CAKES='Wedding_Cakes','Wedding_Cakes'
# class ShapeChoices(models.TextChoices):
#     RECTANGLE ='Rectangle','Rectangle'
#     ROUND ='Round','Round'
# class WeightChoices(models.TextChoices):
#     HALF_KG='1/2 KG','1/2 KG'
#     ONE_KG='1KG','1 KG'
#     TWO_KG='2 KG','2 KG'
class Category(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name ='Categories'
        verbose_name_plural ='Categories'


class Shape(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name ='Shapes'
        verbose_name_plural ='Shapes'

class Weight(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name ='Weights'
        verbose_name_plural ='Weights'

class Cake(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    photo =models.ImageField(upload_to='cake_images')
    category = models. ForeignKey('Category',on_delete=models.PROTECT)
    shape = models.ForeignKey('shape',on_delete=models.PROTECT)
    weight = models.ForeignKey('weight',on_delete=models.PROTECT)
    price =models.FloatField()
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name ='Cakes'
        verbose_name_plural ='Cakes'