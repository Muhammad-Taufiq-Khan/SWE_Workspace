from django.db import models


class File(models.Model):
    filename = models.CharField(max_length=200)
    file = models.FileField()

    def __str__(self):
        return self.filename


