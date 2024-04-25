from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

class Query(models.Model):
    text = models.CharField(max_length=255)
    date_submitted = models.DateTimeField(auto_now_add=True)
