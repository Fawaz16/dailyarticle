from django import views
from django.contrib import admin
from django.urls import path , include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
    path('politics/',views.politics,name='politics'),
    path('metro/',views.metro,name='metro'),
    path('news/',views.news,name='news'),
    path('entertain/',views.entertain,name='entertain'),
    path('article/<int:post_id>',views.article,name='article'),
    path('article2/<int:post_id>',views.article2,name='article2'),
    path('article3/<int:post_id>',views.article3,name='article3'),
    path('article4/<int:post_id>',views.article4,name='article4'),
    path('article5/<int:post_id>',views.article5,name='article5'),
    path('article6/<int:post_id>',views.article6,name='article6'),
   
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
