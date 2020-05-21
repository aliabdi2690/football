from django.db import models
from django.template. defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext as _
from user.models import MyUsermodel
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import MyUsermodel

class Post(models.Model):
    title = models.CharField(max_length=250,)
    body = models.TextField()
    image = models.ImageField(upload_to='media',)
    summery = models.CharField(max_length=250,)
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    likes = models.ManyToManyField("user.MyUsermodel", verbose_name=_("liked users"), editable=False)
    objects = models.Manager()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
       
        return super().save(*args, **kwargs) # Call the real save() method


class Tag(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    post = models.ManyToManyField("Post", verbose_name=_("posts related to tag"))
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    objects = models.Manager()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/tag/{self.slug}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.name)
       
        return super().save(*args, **kwargs)


class Comment(models.Model):
    body = models.TextField(_("comment"))
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(_("comment commited"), auto_now_add=True)
    username = models.CharField(max_length=250)

    class Meta:
        ordering = ['time']
