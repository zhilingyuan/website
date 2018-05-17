from django.urls import path 
from . import views
app_name='blog'
urlpatterns=[path('',views.blog_list,name='index'),
			path('all',views.blog_list_all,name='blogs_all'),
			path('<int:blog_id>',views.blog_detail,name='detail'),
			path('type/<int:blogs_type_pk>',views.blogs_with_type,name='blogs_with_type'),
			path('<int:year>/<int:month>',views.blogs_with_date,name='blogs_with_date'),]