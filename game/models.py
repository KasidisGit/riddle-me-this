from django.db import models

class HardQuestion(models.Model):
    image = models.FileField(upload_to='img/hard', blank=False)
    answer = models.CharField(max_length=200)
    score = models.IntegerField(default=4)
    is_pass = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
    
class MediumQuestion(models.Model):
    image = models.FileField(upload_to='img/medium', blank=False)
    answer = models.CharField(max_length=200)
    score = models.IntegerField(default=3)
    is_pass = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

class EasyQuestion(models.Model):
    image = models.FileField(upload_to='img/easy', blank=False)
    answer = models.CharField(max_length=200)
    score = models.IntegerField(default=2)
    is_pass = models.BooleanField()

    def __str__(self):
        return self.answer
