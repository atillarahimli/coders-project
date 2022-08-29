from turtle import title
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField(verbose_name="Slug",unique=True)



    def __str__(self):
        return self.title
    




class News(models.Model):
    title= models.CharField(max_length=25,verbose_name="Name of News")
    content= models.TextField(verbose_name="Main News")
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True,verbose_name="Should be post?")
    image = models.ImageField(verbose_name="Add image",null=True,upload_to="news_image")
    slug= models.SlugField(verbose_name="Slug",null=True,unique=True) 
    categories = models.ManyToManyField(Category,null=True,related_name='category_blog')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="News"
        verbose_name_plural="More News"
    

