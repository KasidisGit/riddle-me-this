from django.db import models

class HardQuestion(models.Model):
    image = models.FileField(upload_to='img', blank=False)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.answer
    
class MediumQuestion(models.Model):
    image = models.FileField(upload_to='img', blank=False)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.answer

class EasyQuestion(models.Model):
    image = models.FileField(upload_to='img', blank=False)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.answer