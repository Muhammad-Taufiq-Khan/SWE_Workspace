from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class File(models.Model):
    client_name = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    file_name = models.CharField(max_length=200, null=True)
    file = models.TextField(max_length=90000, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.file_name


class Result(models.Model):
    client_name = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    file_name = models.OneToOneField(File, null=True, on_delete=models.CASCADE)
    positive_pct = models.IntegerField(blank=True, null=True)
    negative_pct = models.IntegerField(blank=True, null=True)
    neutral_pct = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

