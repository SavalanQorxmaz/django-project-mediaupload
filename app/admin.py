from django.contrib import admin
from .models import Image,Celebrity,Photos,Project
# from .forms import LogoForm
from django import forms
from django.conf import settings
import os
import shutil
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
        # print(queryset)

        """
        you can do anything here BEFORE deleting the object(s)
        """
        paths =[]
        for value in queryset.values_list('photo'):
            paths.append(value[0])
            print(paths)
        # deletedPath = Photos.objects.values_list('photo')[0][0]
        # print(deletedPath)
        queryset.delete()

        for image in paths:
            imagePath = settings.MEDIA_ROOT + image
            if os.path.exists(imagePath):
                os.remove(imagePath)
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
        print(obj)

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

    def delete_queryset(self, request, queryset):

        paths =[]
        for value in queryset.values_list('name'):
            paths.append(value[0])
            print(paths)

        queryset.delete()

        for projectFolder in paths:
            folderPath = settings.MEDIA_ROOT + os.path.join('Projects/', projectFolder)
            # print(folderPath)
            if os.path.exists(folderPath):
                shutil.rmtree(folderPath)
    # readonly_fields = ['name']

    def get_readonly_fields(self, request, obj=None):
       if obj:
           return ['name']
       return self.readonly_fields



  
