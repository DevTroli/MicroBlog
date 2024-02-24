from django.urls import path

from blog.views import views

urlpatterns= [
    path('', views.PostView.as_view(), name='home')
]
