from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_review, name='make_review'),
    path('show_review/', views.show_review, name='show_review'),
]