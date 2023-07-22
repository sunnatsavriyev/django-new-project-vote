from django.urls import path
from .views import *

urlpatterns = [
    path('', Schoolview, name='index'),
    path('<int:question_id>/menu/',Menusview,name = 'menu'),
]