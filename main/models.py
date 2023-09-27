from django.db import models
import uuid
from os.path import join
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    def __str__(self):
        return self.name

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(unique=True)


class Item(models.Model):
    def __str__(self):
        return self.name

    def upload_path(instance, filename):
        ext = filename.split('.')[-1]

        return join('uploads', instance.category.name, f'{instance.name}_{instance.id}.{ext}')

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(unique=True)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_path, null=True, blank=True)
