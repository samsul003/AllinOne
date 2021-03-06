from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from django.utils import timezone

# Assuming that one item can belong to only one category.
from user_manager.models import AllUser


class Category(models.Model):
    category_name = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length='255', help_text=' A brief description about what', blank=True)

    def __str__(self):
        return self.category_name

    def __unicode__(self):
        return self.category_name


class CategoryByUser(models.Model):
    user = models.ForeignKey(AllUser, related_name="category_user")
    category_name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(blank=True, default='No desc')

    class CategoryType(DjangoChoices):
        BuitIn = ChoiceItem(1, "built_in")
        UserGenerated = ChoiceItem(2, "user_specific")

    category_type = models.IntegerField("category type", choices=CategoryType.choices,
                                        default=CategoryType.UserGenerated)
    # Null in case it is created by the user, otherwise it refers to a System category
    built_in_cat = models.ForeignKey(Category, related_name="category", null=True, blank=True, default=None)

    def __str__(self):
        return self.category_name

    def __unicode__(self):
        return self.category_name


class Item(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(CategoryByUser)
    user = models.ForeignKey(AllUser)
    purchase_date = models.DateField(default=timezone.now(), null=True, blank=True)
    CURRENCY_CHOICES = (
        ('EURO', 'Euro'),
        ('DOLLAR', 'Dollar'),
        ('POUND', 'Pound'),


    )
    currency = models.CharField(max_length=50, choices=CURRENCY_CHOICES, default='EURO')
    category = models.ForeignKey(CategoryByUser)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name





