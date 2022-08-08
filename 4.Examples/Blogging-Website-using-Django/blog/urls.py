from . import views
from.views import HomeView,articleDetailView, PostView, UpdateEditView,DeleteMyView,CommentView
from django.urls import path, include
urlpatterns=[
    path('home/', HomeView.as_view(), name= 'home'),
    path('article/<int:pk>',articleDetailView.as_view(),name='article-detail'),
    #"pk' means primary key using above <int:pk> we are accessing each blog posts with their primary keys
    path('create/',PostView.as_view(), name = 'create'),
    path('article/update/<int:pk>', UpdateEditView.as_view(), name='update'),
    path('article/<int:pk>/delete/', DeleteMyView.as_view(), name='delete'),
    path('article/<int:pk>/comment/', CommentView.as_view(), name='comment'),
    path('about/', views.about, name='about'),

]