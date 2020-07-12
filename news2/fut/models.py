from django.db import models

class News(models.Model):
    text = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.text
