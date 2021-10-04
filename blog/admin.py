from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
# Register your models here.
from .models import Post, Category, Comment
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
@admin.register(Post)
class PostAdmin(TranslationAdmin):
        body_en = forms.CharField(label="Article", widget=CKEditorUploadingWidget())
        body_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
        list_display = ('title', 'slug', 'author', 'publish', 'status')
        list_filter = ('status', 'created', 'publish', 'author')
        search_fields = ('title', 'body')
        prepopulated_fields = {'slug': ('title',)}
        raw_id_fields = ('author',)
        date_hierarchy = 'publish'
        ordering = ('status', 'publish')

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(TranslationAdmin):
        list_display = ('author', 'email', 'post', 'created', 'active')
        list_filter = ('active', 'created', 'updated')
        search_fields = ('author', 'email', 'body')
