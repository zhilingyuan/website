from django.urls import path

from . import views
#generic vies abstract common patterns to easy using
#we can delete a bunch of our own code 
#there several steps to make conversion
#1 convert the url conf
#2 delete some of the old unneeded views
#3 introduce new views based on django's generic views 
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
#above are URLconf 

#urlpatterns = [
#    path('', views.index, name='index'),
#    path('<int:question_id>/',views.detail,name='detail'),
#    path('<int:question_id>/results/',views.results,name='results'),
#    path('<int:question_id>/vote/',views.vote,name='vote'),
    # add url cruft such as .html
    #path('polls/latest.html',view.index)
    # but that's silly]

