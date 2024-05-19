from django.contrib import admin
from .models import Image,Celebrity,Photos,Project
# from .forms import LogoForm
from django import forms
import os
import base64

from django.utils.html import format_html
# Register your models here.



# class LogoAdmin(admin.ModelAdmin):
#     # model = Logo
#     form = LogoForm
#     def logoF(self, obj):
#         return  format_html('<img src="{}" width="200"   height="200" alt="">'.format(obj.logo))
       
#     list_display =['title', 'link','logoF']
 
# admin.site.register(Logo, LogoAdmin)



class InlineImage(admin.TabularInline):
    model = Image
    def imageField(self, obj):
        return  format_html('<img src="{}" width="200"   height="200" alt="">'.format(obj.logo))
    list_display = ['imageField']
    extra = 0
    classes =('collapse',)
@admin.register(Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

class PhotoAdmin(admin.ModelAdmin):
    model = Photos
    actions = ['delete_model']

    def delete_queryset(self, request, queryset):
        print('========================delete_queryset========================')
        print(queryset)

        """
        you can do anything here BEFORE deleting the object(s)
        """

        queryset.delete()

        """
        you can do anything here AFTER deleting the object(s)
        """

        print('========================delete_queryset========================')

    def delete_model(self, request, obj):
        print('==========================delete_model==========================')
        print(obj)

        """
        you can do anything here BEFORE deleting the object
        """

        obj.delete()

        """
        you can do anything here AFTER deleting the object
        """

        print('==========================delete_model==========================')

    
  
    def imageField(self, obj):
        return  format_html('<img src="{}"    height="200" width = "200" alt="">'.format(obj.photo))
    list_display = ['photo_name','imageField']

admin.site.register(Photos,PhotoAdmin)

class InlinePhoto(admin.TabularInline):
    model = Photos
    def imageField(self, obj):
        return  format_html('<img src="./media/{}"    height="200" alt="">'.format(obj.photo))
    list_display = ['imageField']
    extra = 0
    classes =('collapse',)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [InlinePhoto]
    def get_inline_instances(self, request, obj=None):
        return [inline(self.model, self.admin_site) for inline in self.inlines]
    list_display = ['name','Description']