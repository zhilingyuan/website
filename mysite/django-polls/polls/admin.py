#from django.contrib import admin
# Register your models here.
#tell admin that Question objects have an admin interface
#from .models import Question,Choice
#admin.site.register(Question)
#customize the admin form 
#class QuestionAdmin(admin.ModelAdmin):
#	fields=['pub_date','question_text']
# makes the “Publication date” come before the “Question” field
#admin.site.register(Question,QuestionAdmin)

#spilt the form up into fieldsets





#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#       (None,               {'fields': ['question_text']}),
#        ('Date information', {'fields': ['pub_date']}),
#   ]

#admin.site.register(Question, QuestionAdmin)


#admin.site.register(Choice)
#above choice model is not efficient 

from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):#inline takes alot space to display
#Class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1 #provide  extra choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]# 
    list_display=('question_text','pub_date','was_published_recently')
    list_filter=['pub_date']#add pub_date 
    search_fields=['question_text']#add search

		

admin.site.register(Question, QuestionAdmin)