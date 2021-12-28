from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    STATUS = (
        ('TRUE', 'ARE AVAILABLE'),
        ('FALSE', 'NOT AVAILABLE'),
    )
    parent = TreeForeignKey('self',
                            blank=True,
                            null=True,
                            related_name='children',
                            on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=15, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        ('TRUE', 'ARE AVAILABLE'),
        ('FALSE', 'NOT AVAILABLE'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    description = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'self': self.slug})


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)
    ip = models.CharField(max_length=20, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('NEW', 'NEW'),
        ('ACCEPTED', 'ACCEPTED'),
    )
    name = models.CharField(max_length=255, blank=True)
    food = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255, blank=True)
    address = models.TextField(max_length=255, blank=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS, default='NEW')
    ip = models.CharField(blank=True, max_length=50)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MPTTMeta:
    order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'self': self.slug})

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '/'.join(full_path[::-1])
