from django.db import models

# Create your models here.

class MainCategoryFood(models.Model):
    mainStreamFoodName = models.CharField(max_length=100)
    subCategoryFoodCharge = models.CharField(max_length=100)
    def __str__(self):
        return self.mainStreamFoodName
    
class Tables(models.Model):
    tablename = models.CharField(max_length=50)
    def __str__(self):
        return self.tablename
    
class Waiters(models.Model):
    WaiterName = models.CharField(max_length=50)
    def __str__(self):
        return self.WaiterName
    
class bookorder_1(models.Model):
    foodName = models.CharField(max_length=50)
    foodPrice = models.CharField(max_length=50)
    nameOfTable = models.CharField(max_length=50)
    nameOfWaiter = models.CharField(max_length=50)
    def __str__(self):
        return self.foodName
