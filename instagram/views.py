from django.shortcuts import render
from .models import Image,Profile,Comment
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import PostForm, UpdateUserForm, UpdateUserProfileForm
from django.contrib.auth.decorators import login_required


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


@login_required(login_url='login')
def profile(request, username):
    images = request.user.profile.posts.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        'images': images,

    }
    return render(request, 'profile.html', params)
