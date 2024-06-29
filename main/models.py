from django.db import models
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    language = models.CharField(max_length=10, choices=[('en', 'English'), ('fr', 'French')], default='en')

    def __str__(self):
        return self.title