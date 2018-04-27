from django.db import models
from django.urls import reverse

class PersonProfile(models.Model):
    name = models.CharField(max_length=256, default=None, null=True, blank=True)
    email = models.EmailField(max_length=256,blank=True, null= True, unique= True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('personinfo:view')

