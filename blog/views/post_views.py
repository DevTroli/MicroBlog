from django.views import generic

from blog.models import Posts


class Post(generic.ListView):
    queryset = Posts.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"


class PostDetail(generic.DetailView):
    model = Posts
    template_name = "postDetails.html"
