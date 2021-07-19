# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Employe(models.Model):
    nom = models.CharField(max_length=30, blank=False, default='')
    prenom = models.CharField(max_length=50, blank=False, default='')
    dateN = models.DateField(blank=False, default='')
    adresse = models.CharField(max_length=70, blank=False, default='')
    contact = models.CharField(max_length=20, blank=False, default='')
    fonction = models.CharField(max_length=15, blank=False, default='')
    image = models.ImageField(default='')

    def __str__(self):
        return self.nom


class Category(models.Model):  # The Category table name that inherits models.Model
    name = models.CharField(max_length=100)  # Like a varchar

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name  # name to be shown when called


class TodoList(models.Model):  # Todolist able name that inherits models.Model
    title = models.CharField(max_length=250)  # a varchar
    content = models.TextField(blank=True)  # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    category = models.ForeignKey(Category, default="general", on_delete="restrict")  # a foreignkey

    class Meta:
        ordering = ["-created"]  # ordering by the created field

    def __str__(self):
        return self.title  # name to be shown when called
