from django.urls import path
from . import views

app_name = 'resume'

urlpatterns =[
    path('', views.base, name='base'),
    path('gallery/', views.gallery, name='gallery'),
    path('certificates/', views.certificate, name='certificates')
]