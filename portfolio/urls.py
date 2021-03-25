from django.urls import path

from .views import index, detail, contact

urlpatterns = [
    path('', index, name='index'),
    path('/<slug:slug>/', detail, name='blog_detail'),
    path('contact/', contact, name='contact'),
]