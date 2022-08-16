from django.views.generic import ListView, DetailView
from .models import Post


class BlogDetailVew(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'Post'


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
# Create your views here.
