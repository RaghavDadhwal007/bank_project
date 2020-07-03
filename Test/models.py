from django.db import models


class Bank(models.Model):
    Name = models.CharField(max_length=50, default="")
    id = models.BigIntegerField(primary_key=True)

    def __str__(self):
        return self.Name


class Branches(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=255, default="", null=False)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField(max_length=255, default="")
    address = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="")
    district = models.CharField(max_length=255, default="")
    state = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.branch
