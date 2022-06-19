from curses.ascii import US
from django.contrib import admin
from .models import User
# Register your models here.

# decorator
@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'name', 'address', 'mobile')