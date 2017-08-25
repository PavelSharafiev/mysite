import os
from django.db import models

# Create your models here.
from visitcard import settings


class Slider(models.Model):
    image = models.ImageField(upload_to='aboutme/static/aboutme/img/slider')
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    def get_slider_img(self):
        return self.image.url[7:]

    def __str__(self):
        return str(self.title)

    def delete(self, using=None, keep_parents=False):
        img = os.path.join(self.image.path)
        os.remove(img)
        return super().delete(using, keep_parents)


class Skills(models.Model):
    image = models.ImageField(upload_to='aboutme/static/aboutme/img/')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def get_skill_img(self):
        return self.image.url[7:]

    def __str__(self):
        return str(self.title)


class New(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    preview_image = models.ImageField(upload_to='aboutme/static/aboutme/img/')
    date = models.DateTimeField(name='pub_date')

    def preview_text(self):
        return self.text[:300] + "..."

    def get_preview_image(self):
        return self.preview_image.url[7:]

    def __str__(self):
        return str(self.title)
