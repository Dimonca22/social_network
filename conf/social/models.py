from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(verbose_name='Имя', max_length=50, unique=True,
                                help_text="Требуется не больше 50 символов.Только буквы, цифры и @/./+/-/_.",
                                error_messages={'unique': "Пользователь с таким именем пользователя уже существует"})


class PostCreations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Основная часть')
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'
        ordering = ('created_at',)

    def __str__(self):
        return self.title




class PostLikes(models.Model):
    post_id = models.ForeignKey(PostCreations, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Client(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
