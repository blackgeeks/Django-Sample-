from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, default="bank_file")
    code = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    currency = models.CharField(max_length=6, null=True, default="usd")
    createdAt = models.DateTimeField(auto_now_add=True, blank=True,null=True,)

    def __str__(self):
        return str(self.name)

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    file_name = models.CharField(max_length=200, default="")
    file_path = models.CharField(max_length=200, null=True)
    file_type = models.CharField(max_length=100, null=True)
    file_size = models.FloatField(null=True)
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True,null=True,)

    def __str__(self):
        return str(self.file_path)
