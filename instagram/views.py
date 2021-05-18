from django.shortcuts import render
from .models import Image,Profile,Comment
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    images = Image.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    params = {
        'images': images,
        'form': form,
        'users': users,

    }
    return render(request, 'index.html', params)
