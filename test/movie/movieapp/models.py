from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('title',)
        verbose_name='Category'
        verbose_name_plural='Categories'

    def get_url(self):
        return reverse('movie:products_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.title)

class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='product', blank=True)
    release_date = models.DateField()
    actors = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    youtube_link = models.URLField(max_length=550)

    class Meta:
        ordering=('title',)
        verbose_name='Movie'
        verbose_name_plural='Movies'

    def __str__(self):
        return '{}'.format(self.title)