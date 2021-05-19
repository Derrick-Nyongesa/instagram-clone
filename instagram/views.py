from django.shortcuts import render,redirect,get_object_or_404
from .models import Image,Profile,Comment
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import PostForm, UpdateUserForm, UpdateUserProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
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


@login_required(login_url='login')
def profile(request, username):
    current_user = request.user
    profile = Profile.objects.get_or_create(user_id=current_user.id)
    images = Image.objects.all().filter(profile_id=current_user.id)
   
    return render(request, 'profile.html', {'images':images, 'profile':profile})


