from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Bot(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class FakeComment(models.Model):
    comment = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

class History(models.Model):
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField()

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default="")
    address = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)

class InstagramAccount(models.Model):
    username = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)