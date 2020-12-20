# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00) 
    stocks = models.IntegerField(default=1000)
    sold = models.IntegerField(default=20)

    def __unicode__(self):
        return self.book_name


