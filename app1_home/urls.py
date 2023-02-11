#from django.contrib import admin
from django.urls import path ,re_path
from app1_home import views
#from django.conf.urls import include
# these 2 are removed because we are in the app folder only and other things also you dont need when
# you open url file in app1_home
urlpatterns = [
    #path('admin/', admin.site.urls),
    re_path(r'^$', views.welcome,name='welcome'),
    #re_path(r'^$app1_home', include('app1_home')),
]