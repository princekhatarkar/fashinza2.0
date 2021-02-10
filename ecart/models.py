from django.db import models

class categorymap(models.Model):
    category = models.CharField(max_length=100, blank=True, default='')


# Create your models here.
class ecart(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    quantity = models.IntegerField()
    category_id = models.ManyToManyField(categorymap)

    class Meta:
        ordering = ['created']
