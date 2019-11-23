from django.db import models

class HardQuestion(models.Model):
    image = models.FileField(upload_to='img/hard', blank=False)
    answer = models.CharField(max_length=200)
    score = models.IntegerField(default=4)

    def __str__(self):
        return self.answer
    
class MediumQuestion(models.Model):
    image = models.FileField(upload_to='img/medium', blank=False)
    answer = models.CharField(max_length=200)
    score = models.IntegerField(default=3)

    def __str__(self):
        return self.answer

class EasyQuestion(models.Model):
    image = models.FileField(upload_to='img/easy', blank=False)
    answer = models.CharField(max_length=200)
    score = models.IntegerField(default=2)

    def __str__(self):
        return self.answer