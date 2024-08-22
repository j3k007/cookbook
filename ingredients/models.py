from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        db_table='category'
    
    def __str__(self) -> str:
        return self.name


class Ingredients(models.Model):
    name=models.CharField(max_length=255)
    notes=models.TextField()
    category=models.ForeignKey(Category, 
                               related_name='ingredients', 
                               on_delete=models.CASCADE)
    
    class Meta:
        db_table='ingredients'
    
    def __str__(self) -> str:
        return self.name