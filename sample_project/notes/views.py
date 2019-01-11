from django.shortcuts import render,get_object_or_404
from .models import notes
from django.views.generic import ListView ,DetailView , CreateView ,UpdateView ,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User

notifications =[{
	
	'author' : 'ABCD',
	'title': 'python notes',
	'content': 'notes content',
	'shared_date' : 'december 31,2018'},
	{
      'author' : 'WXYZ',
	'title': 'Remainder notes',
	'content': 'notes content',
	'shared_date' : 'jan 01,2019'

	},



	]


def home(request):
	context ={
	'posts': notes.objects.all(), 'notifications' : notifications
	}
	return render(request,'notes/main-dup.html',context,{'title':'Django'})	
def about(request):
	return render(request,'notes/about.html',{'title':'About'})
 
class PostListView(ListView):
	model = notes
	template_name = 'notes/main-dup.html'
	context_object_name = 'posts'
	ordering =['-date_posted']
	paginate_by = 10

class UserPostListView(ListView):
	model = notes
	template_name = 'notes/user_notes.html'
	context_object_name = 'posts'
	paginate_by = 10
	def get_queryset(self):
		user =get_object_or_404(User,username = self.kwargs.get('username'))
		return notes.objects.filter(author = user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = notes
	queryset = notes.objects.filter()

class PostCreateView(LoginRequiredMixin,
	CreateView):
	model = notes
	fields =['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = notes
	fields =['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = notes
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
