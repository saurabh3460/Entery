from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Entry(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='entry')
    entry = models.CharField(max_length=1000, primary_key=True)
    timstamp = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.entry


