from django.db import models


class Theme(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, null=True)
    professor = models.ForeighnKey(Professor, on_delete=models.DO_NOTHING)
    answer = models.TextField()



