from django.urls import path
from . import views

# app_name =  'blog'
urlpatterns = [

    path('about/', views.about, name='about'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('add/', views.post_add, name='post_add'),
    path('', views.post_list, name='post_list'),
    path('search/', views.post_search, name='post_search'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail,name='post_detail'),
    path('edit/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_edit, name='post_edit'),
    path('delete/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_delete, name='post_delete'),
    path('comment/edit/<int:id>/', views.comment_edit, name='comment_edit'),
    path('comment/delete/<int:id>/', views.comment_delete, name='comment_delete'),
    path('<slug:category_slug>/', views.post_list, name='post_list_by_category'),


    # path('comment/reply/', views.reply_page, name="reply"),

]
