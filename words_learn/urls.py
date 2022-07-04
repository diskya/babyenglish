from django.urls import path
from . import views

urlpatterns = [
    path('', views.learn, name='learn'),
    path('word/<int:word_id>/', views.word, name='word'),
]