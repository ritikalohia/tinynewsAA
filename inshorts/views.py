from django.shortcuts import render, HttpResponse
from inshorts.models import Post

# Create your views here.
def home(request):
    posts= Post.objects.filter(status=1).order_by('-created_on')
    context = {'posts': posts}
    return render(request, "index.html", context)