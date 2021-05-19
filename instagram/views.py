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
            post.user = request.user
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
#def profile(request, username):
    #current_user = request.user
    #profile = Profile.objects.get_or_create(user_id=current_user.id)
    #images = Image.objects.all().filter(profile_id=current_user.id)
   
    #return render(request, 'profile.html', {'images':images, 'profile':profile})
def profile(request, username):
    current_user = request.user
    images = Image.objects.all().filter(profile_id=current_user.id)
    if request.method == 'POST':
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if prof_form.is_valid():
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'prof_form': prof_form,
        'images': images,

    }
    return render(request, 'profile.html', params)


@login_required(login_url='/accounts/login/')
def new_status(request, username):
    current_user = request.user
    username = current_user.username
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.user = request.user
            image.save()
        return redirect('homePage')
    else:
        form = PostForm()
    return render(request, 'new_status.html', {"form": form})



