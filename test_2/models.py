from django.db import models

# Create your models here.
class Commit2(models.Model):
    text = models.TextField()
    def __str__(self) -> str:
        return self.text
