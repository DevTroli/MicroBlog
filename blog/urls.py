from django.urls import path
from blog import views as v

urlpatterns = [path("", v.Post.as_view(), name="Index")]
