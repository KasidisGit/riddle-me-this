from django.db import models

class Question(models.Model):
    image = models.FileField(upload_to='static/img', blank=False)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.answer
    
