from django.contrib.postgres.search import SearchVector
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
# from taggit_autocomplete.managers import TaggableManager
# from taggit_autosuggest.managers import TaggableManager
# Create your models here.
from account.models import Profile


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

    # likes = models.ManyToManyField(User, blank=True, related_name='likes')
    # dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    # likes = models.ManyToManyField(User,related_name='post_liked',
    #                                     blank=True)
    # total_likes = models.PositiveIntegerField(db_index=True,
    #                                           default=0)
    visit_count = models.IntegerField(default=0)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(Profile,
                               on_delete=models.CASCADE,
                               related_name='post_author')
    body = RichTextUploadingField(blank=True,null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='published')
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.
    tags = TaggableManager()
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
    # def get_comments(self):
    #     return self.comments.filter(parent=None).filter(active=True)




class Comment(models.Model):

        post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
        email = models.EmailField()
        # parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
        body = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        active = models.BooleanField(default=True)
        author = models.ForeignKey(User,null=True,
                                   on_delete=models.CASCADE,
                                   related_name='comment_author')


        class Meta:
              ordering = ('-created',)

        def __str__(self):
              return f'Comment by {self.body} on {self.post}'

        def get_comments(self):
            return Comment.objects.filter(parent=self).filter(active=True)


# class PostImage(models.Model):
#     flat= models.ForeignKey(Post, blank=True, null=True,related_name='post_picture' , default=None,on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='flat_images/')
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)