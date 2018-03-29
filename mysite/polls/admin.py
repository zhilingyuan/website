from django.contrib import admin

# Register your models here.
#tell admin that Question objects have an admin interface
from .models import Question

admin.site.register(Question)
