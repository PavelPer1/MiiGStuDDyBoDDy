from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='avatar/')
    email = models.EmailField(max_length=250)
    number = models.CharField(max_length=50)
    fio = models.CharField(max_length=100, null=True)
    speciality = models.CharField(max_length=150, null=True)
    well = models.IntegerField(null=True)
    add_information = models.CharField(max_length=350, null=True)

    def __str__(self):
        return str(self.user)


class Science(models.Model):
    scn = models.CharField(max_length=350, null=True)

    def __str__(self):
        return self.scn


class HelpMe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='helpme', null=True)
    item = models.ForeignKey(Science, on_delete=models.CASCADE, null=True)
    add_information = models.CharField(max_length=350, null=True)

    def __str__(self):
        return f'{self.user} - {self.item}'


class IcanHelp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='can_help', null=True)
    items = models.ForeignKey(Science, on_delete=models.CASCADE, null=True)
    skills = models.CharField(max_length=350, null=True)

    def __str__(self):
        return f'{self.user} - {self.items}'



