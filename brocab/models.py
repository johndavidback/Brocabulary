from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=50)
    definition = models.TextField()
    image = models.FileField(upload_to='images', blank=True)

    def __unicode__(self):
        return self.word