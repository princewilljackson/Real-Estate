from django.db import models

class SaleContact(models.Model):
  sale = models.CharField(max_length=200)
  sale_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.EmailField()
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(auto_now_add=True)
  user_id = models.IntegerField(blank=True)

  class Meta:
        verbose_name_plural = "Contacts from Apartments listed for Sale"

  def __str__(self):
    return self.name

class RentContact(models.Model):
  rent = models.CharField(max_length=200)
  rent_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.EmailField()
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(auto_now_add=True)
  user_id = models.IntegerField(blank=True)

  class Meta:
        verbose_name_plural = "Contacts from Apartments listed for Rent"

  def __str__(self):
    return self.name

class PropertyManagement(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  context = models.TextField()

  class Meta:
        verbose_name_plural = "Property Management"

  def __str__(self):
    return self.name