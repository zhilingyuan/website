from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),#这里的路径就是网址的路径 127.0.0.1：8000\admin
    #
    path('admin/', admin.site.urls),
]
