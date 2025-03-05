from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:4
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
