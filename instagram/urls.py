from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='homePage'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('new/status/<username>', views.new_status, name='newStatus'),
    path('post/<id>', views.post_comment, name='comment'),
    path('search/', views.search_profile, name='search'),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow'),
    path('like', views.like_post, name='like_post'),
    path('single_image/likes/<id>', views.single_image_like, name='singleImageLike'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)