from django.db import models

# Assuming that one item can belong to only one category.


class Category(models.Model):
    category_name = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length='255', help_text=' A brief description about what'
                                                               ' kind of items fall into this category', blank=True)


class Item(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    CURRENCY_CHOICES = (
        ('EURO', 'Euro'),
        ('DOLLAR', 'Dollar'),
        ('POUND', 'Pound'),


    )
    currency = models.CharField(max_length=50, choices=CURRENCY_CHOICES, default='EURO')
    category = models.ForeignKey(Category)
