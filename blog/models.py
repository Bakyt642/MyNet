from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_list_by_category',
                       args=[self.slug])
class Post (models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = RichTextUploadingField(blank=True,null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='published')
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.
    category = models.ForeignKey(Category,
                                 related_name='blog_category',
                                 on_delete=models.CASCADE)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])
    # def get_absolute_url(self):
    #     return reverse('post_detail',
    #                    kwargs={'post_slug': self.slug})


class Comment(models.Model):
        post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
        email = models.EmailField()
        body = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        active = models.BooleanField(default=True)
        author = models.ForeignKey(User,null=True,
                                   on_delete=models.CASCADE,
                                   related_name='comment_author')


        class Meta:
              ordering = ('created',)

        def __str__(self):
              return f'Comment by {self.name} on {self.post}'

# class PostImage(models.Model):
#     flat= models.ForeignKey(Post, blank=True, null=True,related_name='post_picture' , default=None,on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='flat_images/')
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)