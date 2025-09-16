from django.db import models

class StolenCredential(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.timestamp}"
