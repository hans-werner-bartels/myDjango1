from django.contrib import admin
from .models import Post
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.

admin.site.register(Post, SimpleHistoryAdmin)