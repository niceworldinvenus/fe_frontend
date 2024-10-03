from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=255)
    pub_date  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (self.title)

class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    student_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return (self.title)
    
