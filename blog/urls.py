
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]

# from django.urls import path
# from .views  import postListView,postDetailView,postCreateView,postUpdateView,postDeleteView
# from . import views

# urlpatterns = [
#     path('', postListView.as_view(),name='blog-home'),
#     path('post/<int:pk>/', postDetailView.as_view(),name='post-detail'),
#     path('post/new/', postCreateView.as_view(),name='post-create'),
#     path('post/<int:pk>/update/',postUpdateView.as_view(),name='post-update'),
#         path('post/<int:pk>/delete/',postDeleteView.as_view(),name='post-delete'),
#     path('about/', views.about,name='blog-about'),
#     path('log',views.loginn,name='blog-login'),
# ]  