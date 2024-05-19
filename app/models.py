from django.db import models
import os

# Create your models here.

def get_img_upload_path(instance, filename):
    return f'/media/{instance.logo}/{filename}'

def path_generator(instance, filename):
    base, extension = os.path.splitext(os.path.basename(filename))
    file_dir = f"Photos/{instance.project.name}/{instance.photo_name}{extension}"
    return file_dir

# class Project(models.Model):
#     title =models.CharField(max_length=255)
#     description = models.TextField()
#     link = models.TextField(null=True, blank=True)
#     class Meta:
#        ordering = ('title',)
#     def __str__(self):
#         return self.title

# class Picture(models.Model):
#     content_type = models.ForeignKey(Project, on_delete=models.CASCADE)
#     imgtitle =models.CharField(max_length=20)
#     image = models.ImageField()


# class Contacts(models.Model):
#   name = models.CharField(max_length=32)
#   logo = models.ImageField(upload_to=get_img_upload_path)
#   address = models.CharField(max_length=255)
#   def __str__(self):
#         return self.name
  

# class Logo(models.Model):
#     title =models.CharField(max_length=20)
#     link = models.TextField(null=True, blank=True)
#     logo = models.ImageField(upload_to=get_img_upload_path, null=True)
#     def __str__(self):
#         return self.name
    
class Project(models.Model):
    name = models.CharField('Project Name', max_length=100, unique=True)
    Description = models.TextField('Tag Description', max_length=1000, blank=True)

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

# class Meta:
#     verbose_name = 'Photos'
#     verbose_name_plural = verbose_name
#     ordering = ['Date_uploaded']

