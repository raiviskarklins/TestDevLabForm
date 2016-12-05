from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class SimpleForm(models.Model):
    email = models.EmailField(blank=False)
    text = models.CharField(max_length=400, blank=False)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse('contact:html')

    def __str__(self):
        return self.email + ' - ' + self.text




