from django.shortcuts import render,redirect,get_object_or_404
from .models import Image,Profile,Follow
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import PostForm, UpdateUserForm, UpdateUserProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic.detail import DetailView


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
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
    #current_user = request.user
    #images = Image.objects.all().filter(profile_id=current_user.id)
    images = request.user.posts.all()
    if request.method == 'POST':
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if prof_form.is_valid():
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'form': prof_form,
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


@login_required(login_url='login')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.posts.all()
    
    followers = Follow.objects.filter(followed=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False

    params = {
        'user_prof': user_prof,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status
    }
    print(followers)
    
    return render(request, 'user_profile.html', params)


# @login_required(login_url='login')
# def post_comment(request, id):
#     image = get_object_or_404(Image, pk=id)
#     is_liked = False
#     if image.likes.filter(id=request.user.id).exists():
#         is_liked = True
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             savecomment = form.save(commit=False)
#             savecomment.post = image
#             savecomment.user = request.user
#             savecomment.save()
#             return HttpResponseRedirect(request.path_info)
#     else:
#         form = CommentForm()
#     params = {
#         'image': image,
#         'form': form,
#         'is_liked': is_liked,
#         'total_likes': image.total_likes()
#     }
#     return render(request, 'single_post.html', params)


@login_required(login_url='login')
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'results.html', {'message': message})


def unfollow(request, to_unfollow):
    if request.method == 'GET':
        user_profile2 = Profile.objects.get(pk=to_unfollow)
        unfollow_d = Follow.objects.filter(follower=request.user.profile, followed=user_profile2)
        unfollow_d.delete()
        return redirect('user_profile', user_profile2.user.username)



def follow(request, to_follow):
    if request.method == 'GET':
        user_profile3 = Profile.objects.get(pk=to_follow)
        follow_s = Follow(follower=request.user.profile, followed=user_profile3)
        follow_s.save()
        return redirect('user_profile', user_profile3.user.username)


@login_required (login_url='/accounts/register/')
def like_post(request, id):
    image = Image.objects.get(id=id)
    image.likes = image.likes + 1
    image.save()
    return redirect('index')







