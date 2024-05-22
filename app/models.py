from django.db import models
import os
import shutil
import re
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.

def get_img_upload_path(instance, filename):
    return f'/media/{instance.logo}/{filename}'

def path_generator(instance, filename):
    base, extension = os.path.splitext(os.path.basename(filename))
    file_dir = f"Projects/{instance.project.name}/{instance.photo_name}{extension}"
    return file_dir

def path_slider(instance,filename):
    base,extension = os.path.splitext(os.path.basename(filename))

    
    return 'Slider/slide{extension}'.format( extension = extension )



    
class Project(models.Model):
    name = models.CharField('Project Name', max_length=100, unique=True, blank=False, 
        #                     validators=[
        # RegexValidator(
        #     regex = r'[A-Z,a-z,0-9,-,_,]{50}',
        #     message="Only a-z,A-Z,0-9"),
        # ]
        )
    
    Description = models.TextField('Tag Description', max_length=1000, blank=True)
   
    def delete(self, *args, **kwargs):
            path = settings.MEDIA_ROOT + os.path.join('Projects/', self.name)
            super(Project, self).delete(*args, **kwargs)
            if os.path.exists(path):
                shutil.rmtree(path)
    def clean(self):
        regex = re.findall("[\,/,!,#,@,$,%,^,&,*,(,),]", self.name)
        if not len(regex) <1:
            raise ValidationError(
                {'name': "Not !@#$%^&*()"})


class Celebrity(models.Model):
    name = models.CharField(max_length=100)

class Photos(models.Model):
    photo_name = models.CharField('Photo Name', max_length=200, unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)
    photo = models.ImageField(upload_to=path_generator, blank=False)
    def __str__(self):
        return self.photo_name
    
    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = Photos.objects.get(id=self.id)
        except Photos.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.photo and self.photo and obj.photo != self.photo:
            # delete the old image file from the storage in favor of the new file
            obj.photo.delete()
    
    def delete(self, *args, **kwargs):
        storage, path = self.photo.storage, self.photo.path
        self.photo.delete()
        super(Photos, self).delete(*args, **kwargs)
        storage.delete(path)

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        return super(Photos, self).save(*args, **kwargs)

class Image(models.Model):
    celebrity = models.ForeignKey(Celebrity, on_delete=models.CASCADE)
    image = models.ImageField()

class Slider(models.Model):
    slide = models.ImageField(upload_to=path_slider, blank=False)
    def remove_on_image_update(self):
        try:
            obj = Slider.objects.get(id=self.id)
        except Slider.DoesNotExist:
            return
        if obj.slide and self.slide and obj.slide != self.slide:
            obj.slide.delete()
    
    def delete(self, *args, **kwargs):
        storage, path = self.slide.storage, self.slide.path
        self.slide.delete()
        super(Slider, self).delete(*args, **kwargs)
        storage.delete(path)

    def save(self, *args, **kwargs):
        
        self.remove_on_image_update()
        return super(Slider, self).save(*args, **kwargs)
    

class Logo(models.Model):
    def path_Logo(instance, filename):
        base, extension = os.path.splitext(os.path.basename(filename))
        return 'Logo/logo{extension}'.format( extension = extension )

    # logo_name = models.CharField('Logo Name', max_length=200, unique=True)
    logo_title = models.CharField('Logo Title', max_length=500, unique=True)
    logo = models.ImageField(upload_to=path_Logo, blank=False)
    def __str__(self):
        return self.logo_title
    
    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = Logo.objects.get(id=self.id)
        except Logo.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.logo and self.logo and obj.logo != self.logo:
            # delete the old image file from the storage in favor of the new file
            obj.logo.delete()
    
    def delete(self, *args, **kwargs):
        storage, path = self.logo.storage, self.logo.path
        self.logo.delete()
        super(Logo, self).delete(*args, **kwargs)
        storage.delete(path)

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        return super(Logo, self).save(*args, **kwargs)
    

class Contact(models.Model):
    def path_Contact(instance, filename):
        base, extension = os.path.splitext(os.path.basename(filename))
        return 'Contacts/contact{extension}'.format( extension = extension )

    # logo_name = models.CharField('Logo Name', max_length=200, unique=True)
    contact_title = models.CharField('Contact Title', max_length=100, unique=True)
    contact_link = models.CharField('Contact Link', max_length=500, unique=True)
    contact_logo = models.ImageField(upload_to=path_Contact, blank=False)
    def __str__(self):
        return self.contact_title
    
    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = Contact.objects.get(id=self.id)
        except Contact.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.contact_logo and self.contact_logo and obj.contact_logo != self.contact_logo:
            # delete the old image file from the storage in favor of the new file
            obj.contact_logo.delete()
    
    def delete(self, *args, **kwargs):
        storage, path = self.contact_logo.storage, self.contact_logo.path
        self.contact_logo.delete()
        super(Contact, self).delete(*args, **kwargs)
        storage.delete(path)

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        return super(Contact, self).save(*args, **kwargs)

