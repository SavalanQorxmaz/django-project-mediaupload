from django.contrib import admin
from .models import Logo,Image,Celebrity
from .forms import LogoForm
from django import forms

from django.utils.html import format_html
# Register your models here.



class LogoAdmin(admin.ModelAdmin):
    # model = Logo
    form = LogoForm
    def logoF(self, obj):
        return  format_html('<img src="{}" width="200"   height="200" alt="">'.format(obj.logo))
       
    list_display =['title', 'link','logoF']
 
admin.site.register(Logo, LogoAdmin)



class InlineImage(admin.TabularInline):
    model = Image

@admin.register(Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    inlines = [InlineImage]