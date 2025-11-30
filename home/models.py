# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    madeof = models.TextField(max_length=255, null=True, blank=True)
    whereused = models.TextField(max_length=255, null=True, blank=True)
    howtouse = models.TextField(max_length=255, null=True, blank=True)
    precautions = models.TextField(max_length=255, null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Order(models.Model):

    #__Order_FIELDS__
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    instructions = models.TextField(max_length=255, null=True, blank=True)

    #__Order_FIELDS__END

    class Meta:
        verbose_name        = _("Order")
        verbose_name_plural = _("Order")


class Orderdetails(models.Model):

    #__Orderdetails_FIELDS__
    orderid = models.IntegerField(null=True, blank=True)
    productid = models.IntegerField(null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)

    #__Orderdetails_FIELDS__END

    class Meta:
        verbose_name        = _("Orderdetails")
        verbose_name_plural = _("Orderdetails")



#__MODELS__END
