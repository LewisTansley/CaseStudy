from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
  fieldsets = (
      (None, {'fields': ('username', 'password', )}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('username', 'password1', 'password2'),
      }),
  )
  list_display = ['username',]
  search_fields = ('username',)
  ordering = ('username',)
admin.site.register(User, UserAdmin)

class Book(models.Model):
    bookTitle = models.CharField(max_length=180)
    bookAuthor = models.CharField(max_length=180)
    bookDescription = models.CharField(max_length=180)
    bookCover = models.ImageField()