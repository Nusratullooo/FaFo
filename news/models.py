from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse


class News(models.Model):
    name = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'self': self.slug})


class Comment_news(models.Model):
    STATUS = (
        ('TRUE', 'ARE AVAILABLE'),
        ('FALSE', 'NOT AVAILABLE'),
    )
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    comment = models.TextField(max_length=255, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
