from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Data(models.Model):

    superuser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    uzer      = models.CharField(max_length=50, null=True)
    group     = models.CharField(max_length=100)
    text      = models.TextField()

    def __str__(self):
        return self.text[:50]

    def get_absolute_url(self):
        return reverse('card_detail', args=[str(self.id)])

    class Meta:

        verbose_name_plural = "Data"

    

    
