from django.db import models


class Hobanner(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='images/', blank=False, null=True)

    def __str__(self):
        return self.name
