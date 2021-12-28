from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField(max_length=255, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name