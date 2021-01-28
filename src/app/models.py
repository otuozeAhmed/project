from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Data(models.Model):

    GROUP_CHOICES = (
        ('one', 'One'),
        ('two', 'Two'),
        ('three', 'Three')
    )

    group     = models.CharField(max_length=20, choices=GROUP_CHOICES, default='one')
    text      = models.TextField()

    def __str__(self):
        return self.text[:30]

    def get_absolute_url(self):
        return reverse('card_detail', args=[str(self.id)])

    class Meta:

        verbose_name_plural = "Data"

    

    
