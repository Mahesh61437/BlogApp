from django.urls import path
from . import views
from .views import PostListView ,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
    path('', PostListView.as_view(),name = 'note-home'),
    path('user/<str:username>', UserPostListView.as_view(),name = 'user-notes'),
    path('about/', views.about,name = 'note-about'),
    path('notes/<int:pk>/',PostDetailView.as_view(),name ='notes-detail'),
    path('notes/new/',PostCreateView.as_view(),name ='notes-create'),
    path('notes/<int:pk>/update/',PostUpdateView.as_view(),name ='notes-update'),
    path('notes/<int:pk>/delete/',PostDeleteView.as_view(),name ='notes-delete'),
]