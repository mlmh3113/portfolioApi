from django.db import models

class Work(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='images/', default='images/imagen_default.jpg', verbose_name='Image')
    github = models.URLField(blank=True, verbose_name='Github')
    live = models.URLField(blank=True, verbose_name='Live')

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return self.title
