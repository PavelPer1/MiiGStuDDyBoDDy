from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Chat(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member1', null=True)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member2', null=True)

    def get_absolute_url(self):
        return 'users:message', (), {'chat_id': self.pk}

    def __str__(self):
        return str(self.user1) + '-' +str(self.user2)


class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name="Чат", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    message = models.TextField("Сообщение")
    pub_date = models.DateTimeField('Дата сообщения', default=timezone.now)
    is_readed = models.BooleanField('Прочитано', default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message
