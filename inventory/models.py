from django.db import models
from django.urls import reverse

class Category_shopping(models.Model):
    class Meta:
        verbose_name = 'Shopping_Category'
        verbose_name_plural = 'Shopping_Categories'
    shopping_category_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.shopping_category_name
    
class Store_shopping(models.Model):
    class Meta:
        verbose_name = 'Shopping_store'
        verbose_name_plural = 'Shopping_stores'
    shopping_store = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.shopping_store
    
class Cart(models.Model):
    category_shopping = models.ForeignKey(Category_shopping, on_delete=models.SET_NULL, null=True, blank=True)
    store_shopping = models.ForeignKey(Store_shopping, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Category: {self.category_shopping}, Store: {self.category_shopping}, Product: {self.product}, Quantity: {self.quantity}"

    def get_absolute_url(self):
        return reverse("cart:cart_detail")
