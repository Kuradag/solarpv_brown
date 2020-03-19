from django.contrib import admin
from .models import Comment

# Register your models here.
#allows modification of comment on dashboard.
admin.site.register(Comment)
