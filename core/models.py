from django.db import models

# Create your models here.
class Plate(models.Model):
    name = models.CharField(max_length = 20)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Check(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    plate = models.ForeignKey(Plate, on_delete= models.PROTECT, related_name= "checks")
    date = models.DateTimeField()
    message = models.CharField(max_length = 20)
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null = True, blank = True, related_name = "checks")

    def __str__(self):
        return f"{self.amount} {self.Plate.name} {self.Category.name}"
