from django.db import models

# Create your models here.
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=250)
    supplier_code = models.CharField(max_length=25)
    supplier_address = models.TextField()

    class Meta:
        verbose_name = 'supplier',
        verbose_name_plural = 'suppliers'