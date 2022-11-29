from django.db import models

# Create your models here.


class Profile(models.Model):
    user_id = models.PositiveIntegerField(verbose_name="User ID", unique = True)
    username = models.CharField(verbose_name="Имя Пользователя", max_length=255, blank=True,null=True)
    f_name = models.CharField(verbose_name="Имя", max_length=255, blank=True, null=True)
    l_name = models.CharField(verbose_name="Фамилия", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        
    def __int__(self):
        return self.id

    def __str__(self):
        return self.username



class Message(models.Model):
    text = models.TextField(verbose_name="Сообщение")

    class Meta: 
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class MessageMe(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.PROTECT, verbose_name="Пользователь")
    messages = models.TextField(verbose_name="Полученное сообщение")

    class Meta: 
        verbose_name = 'Сообщение от пользователя'
        verbose_name_plural = 'Сообщения от пользователей'