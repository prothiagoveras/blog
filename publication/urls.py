from django.urls import path
from .views import index, contact, about, post

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contact, name='contact'),
    path('sobre/', about, name='about'),
    path('poste/', post, name='post')
]