from django.db import models
from server.models import Server

# Create your models here.


class VM(models.Model):
    server = models.ForeignKey(Server, related_name='vm', on_delete=models.PROTECT)
    name = models.CharField(max_length=18)

    def __str__(self):
        return 'Машина: {}'.format(
            self.name
        )

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'
