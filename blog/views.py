from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

 
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #looks by default for the template in <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #Odering from newest to oldest. To reverse the order remove the minus sign
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #looks by default for the template in <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


#to use your own context name, set the context_object_name to what you want and refer to the post_detail.html
class PostDetailView(DetailView):
    model = Post
    # context_object_name = 'post'

class PostCreateView( LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView( LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

 

#create view expects the template name to be <the name of the name of the model>_<form>.html eg. post_form.html