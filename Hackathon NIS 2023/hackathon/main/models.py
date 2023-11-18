from django.db import models

# Create your models here.
class Files(models.Model):
    file = models.FileField(upload_to= 'files')
    images = models.ImageField(upload_to= 'files')

    class Meta:
        verbose_name='File'
        verbose_name_plural = 'Files'
