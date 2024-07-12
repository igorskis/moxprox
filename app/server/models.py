from django.db import models

# Create your models here.


class Server(models.Model):
    name = models.CharField(max_length=18)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'сервер'
        verbose_name_plural = 'сервера'
