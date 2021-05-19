from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='homePage'),
    path('profile/<username>/', views.profile, name='profile'),
    #path('user_profile/<username>/', views.user_profile, name='user_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)