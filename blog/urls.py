from django.urls import path
from blog import views as v

urlpatterns = [
    path("", v.Post.as_view(), name="home"),
    path("<slug:slug>/", v.PostDetail.as_view(), name="post_detail"),
]
