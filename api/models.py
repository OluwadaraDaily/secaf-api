from django.db import models

# Create your models here.

class Photo(models.Model):
    name = models.CharField(max_length=100, default=False)
    has_face = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
