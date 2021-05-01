from django.contrib import admin
from .models import *

@admin.register(Talking) # decorator
class TalkingAdmin(admin.ModelAdmin): 
    list_display = ['name', 'massage']