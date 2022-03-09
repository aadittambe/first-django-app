from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # example: /summary/1/
    path('categories/', views.categories, name='categories'),
    path('summary/<int:summary_id>/', views.summary, name='summary'),
    path('categories/<slug>/', views.category_detail, name='category_detail'),
    path('summary/<int:summary_id>/', views.summary, name='summary'),
]
