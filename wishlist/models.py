from django.db import models


class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


class Places(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField(max_length=255)

