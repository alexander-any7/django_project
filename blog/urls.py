from django.urls import path
from blog import views #chech for import error
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home' ), #The empty string makes this the home page of the blog app
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail' ),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts' ),
    path('post/new/', PostCreateView.as_view(), name='post-create' ),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update' ),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete' ),
    path('about/', views.about, name='blog-about')
]