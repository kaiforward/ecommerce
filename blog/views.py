from django.shortcuts import render
from.models import Blog

# Create your views here.
def posts_all_view(request):
	blog_info = Blog.objects.all()[0:3]
	return render(request, 'allposts.html', {'blog_info': blog_info})