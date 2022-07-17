from django.urls import path, include
from  . views import *

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('<int:blog_id>/', detail, name='detail')
]
    