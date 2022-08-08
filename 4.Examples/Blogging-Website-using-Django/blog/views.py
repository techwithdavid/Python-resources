from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Comment, Profile
from django.views.generic import ListView, DetailView,CreateView,UpdateView, DeleteView
from .form import PostForm, CommentForm
from django.urls import reverse_lazy
#def home(request):
    #return render(request,"home.html",{ })
class HomeView(ListView):
    model= Post
    template_name ='home.html'
    ordering = ["-id"] #Ordering them with ID's is equivalent to ordering by date


class articleDetailView(DetailView):
    model=Post
    template_name = 'articles.html'
class PostView(CreateView):
    model = Post
    #Only required when using our custom form
    template_name = 'add_post.html'
    fields = ('title', 'content','topic','author','header_image')
class UpdateEditView(UpdateView):
    model = Post
    template_name = 'edit_update.html'
    fields = ('title', 'content', 'topic','header_image')
    #form_class = UpdateForm
class DeleteMyView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
class CommentView(CreateView):
    model = Comment
    #Only required when using our custom form
    template_name = 'comments.html'
    form_class = CommentForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.post_id= self.kwargs['pk']
        return super().form_valid(form)



def about(response):
    all_data= Profile.objects.all
    return render(response,'about.html',{'all':all_data})

    #fields = ('post', 'name','body')
# Create your views here.
