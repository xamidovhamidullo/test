from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    phone = models.CharField(max_length=255)



class Information(models.Model):
    img = models.ImageField(upload_to="logo/")
    address = models.CharField(max_length=255)
    phone = models.IntegerField()
    text = models.TextField()
    fb = models.URLField()
    insta = models.URLField()
    tw = models.URLField()
    yt = models.URLField()


class Slider(models.Model):
    img = models.ImageField()
    bg_img = models.ImageField()
    title = models.TextField()
    text = models.CharField(max_length=255)


class Category(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField()
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    is_popular = models.BooleanField()


class About(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    img = models.ImageField()
    img_text = models.CharField(max_length=255)
    video = models.FileField()
    video_img = models.ImageField()


class Info(models.Model):
    logo = models.ImageField()
    number = models.IntegerField()
    name = models.CharField(max_length=50)


class WhyChooseOption(models.Model):
    name = models.CharField(max_length=255)


class WhyChoose(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    img = models.ImageField()
    options = models.ManyToManyField(WhyChooseOption)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField()
    name = models.CharField(max_length=255)
    short = models.CharField(max_length=255)
    text = models.TextField()
    price = models.IntegerField()
    bonus = models.IntegerField(default=0)

class ClientFeedback(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    img = models.ImageField()


class GalleryCategory(models.Model):
    name = models.CharField(max_length=255)


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    img = models.ImageField()
    is_active = models.CharField(max_length=255)


class TimeRemind(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    time = models.IntegerField()


class Logo(models.Model):
    image = models.ImageField()

