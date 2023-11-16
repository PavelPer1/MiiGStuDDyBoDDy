from django.contrib.auth.models import User
from django.db import models
from users.models import HelpMe


class CreateOffers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True)
    user_offer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_offer', null=True)
    offer = models.ForeignKey(HelpMe, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user} - {self.user_offer}'
