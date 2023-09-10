from django.db import models
import uuid

# Create your models here.


class Category(models.Model):
    category_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField()


class Item(models.Model):
    item_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField()
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
