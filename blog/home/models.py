from dataclasses import fields
from email.policy import default
from pyexpat import model
from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify
from random import choices, randint
import random,string
from django.contrib.auth.models import User
from ckeditor_uploader.fields import  RichTextUploadingField
# Create your models here.


class tagsData(models.Model):
    tag_text = models.CharField(max_length=50,blank=False)
    tag_uses = models.IntegerField(default=1)
    def __str__(self):
        return self.tag_text



class blog_Details(models.Model):
    blog_title = models.TextField(max_length=255,blank=False)
    blog_thumbnail=models.ImageField(upload_to='thumbnails/',default="data:image/png;base64,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")
    blog_thumbnail_url = models.TextField(blank=True,null=True)
    blog_brief = models.TextField(max_length=255,blank=False)
    blog_creator = models.ForeignKey(User,blank=False,on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True)
    date = models.DateField(default=timezone.now)
    blog_clicks = models.IntegerField(default=0)
    tags_input = models.TextField(blank=True)
    link_chain = models.TextField(blank=True)
    def __str__(self):
        return self.blog_title
    class Meta:
        ordering = ["-blog_clicks"]

        
    def save(self,*args, **kwargs):
            word = ''
            abc = list(string.ascii_lowercase)
            Abc = list(string.ascii_uppercase)
            if not self.slug:
                def slugify_blog():
                    word = ''
                    blog_t = self.blog_title[:50]
                    slug = slugify(blog_t)
                    self.slug = slug
                    while len(word) <= len(self.blog_creator.username):
                        word+=random.choice(abc)
                        word+=random.choice(Abc)
                    if word in blog_Details.objects.all().only("link_chain"):
                        return slugify_blog()
                    else:
                        return word
                word = slugify_blog()
                self.slug+='-'+word 
                self.link_chain=word 

            tags_list=self.tags_input.split(",")
            for i in tags_list:
                tagobj = tagsData.objects.get_or_create(tag_text = i)
                if (tagobj[1]==False):
                    tagobj[0].tag_uses=tagobj[0].tag_uses+1;
                    tagobj[0].save()
            super().save(*args, **kwargs)


class blog(models.Model):
    blog_id = models.ForeignKey(blog_Details,on_delete=models.CASCADE)
    blog_content = RichTextUploadingField(blank=True,null=True)
    link_chain = models.TextField(blank=True)
    def __str__(self):
        return self.blog_id.link_chain

    def get_absolute_url(self):
        return reverse('blog_detail',self.date, kwargs={'slug': self.blog_id.slug})
    def save(self,*args, **kwargs):
            self.link_chain = self.blog_id.link_chain
            super().save(*args, **kwargs)
    
    
class tags(models.Model):
    tag_text = models.CharField(max_length=50,blank=False)
    tag_uses = models.IntegerField(default=1)
    def __str__(self):
        return self.blog_id.tag_text


class PostLikes(models.Model):
    post = models.ForeignKey(blog_Details,on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(default="unlike" ,choices=(('like','like'),('unlike','unlike')),max_length=20)
    def __str__(self):
        return self.post