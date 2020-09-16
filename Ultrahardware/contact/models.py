from django.db import models

# Create your models here.

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False #que hace esto?
        db_table = 'message'

    def __str__(self):
        return self.email