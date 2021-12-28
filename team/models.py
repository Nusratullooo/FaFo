from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255, blank=True)
    work = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(blank=True)
    experience = models.IntegerField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    biography = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

