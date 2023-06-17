from django.shortcuts import render
from .models import Post
from django.views import generic


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    model = Post
    template_name = 'blog/blog.html'
    
# def blog(request):
#     """
#         Display the wishlist.
#     """    
#     blog = Post.objects.filter(status=1).order_by('-created_on')
#     context = {'blog': blog}

#     return render(request, 'blog/blog.html', context)


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'    


