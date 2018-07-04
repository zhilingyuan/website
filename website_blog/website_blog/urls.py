"""website_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from blog.views import blog_list
urlpatterns = [
	path('',views.home,name='home'), 
	path('blog/',include('blog.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor',include('ckeditor_uploader.urls')),
    path('login/',views.login,name='login'),
    path('comments/',include('comment.urls')),
    path('register/',views.register,name='register'),
    path('likes/',include('likes.urls')),
    path('login_form_modal/',views.login_form_modal,name='login_form_modal'),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)