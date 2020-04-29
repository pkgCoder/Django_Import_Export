from django.urls import path
from . import views
urlpatterns=[
path('', views.export , name="index"),

path('plot', views.simple_upload , name="inde")
]