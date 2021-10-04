from modeltranslation.translator import register, TranslationOptions
from .models import Category, Comment, Post


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')


@register(Post)
class ActorTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(Comment)
class GenreTranslationOptions(TranslationOptions):
    fields = ('body', )


