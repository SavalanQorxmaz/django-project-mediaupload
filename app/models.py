from django.db import models

# Create your models here.

def get_img_upload_path(instance, filename):
    return f'/media/{instance.logo}/{filename}'

class Project(models.Model):
    title =models.CharField(max_length=255)
    description = models.TextField()
    link = models.TextField(null=True, blank=True)
    class Meta:
       ordering = ('title',)
    def __str__(self):
        return self.title

class Picture(models.Model):
    content_type = models.ForeignKey(Project, on_delete=models.CASCADE)
    imgtitle =models.CharField(max_length=20)
    image = models.ImageField()


class Contacts(models.Model):
  name = models.CharField(max_length=32)
  logo = models.ImageField(upload_to=get_img_upload_path)
  address = models.CharField(max_length=255)
  def __str__(self):
        return self.name
  

class Logo(models.Model):
    title =models.CharField(max_length=20)
    link = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to=get_img_upload_path, null=True)
    def __str__(self):
        return self.name
    


class Celebrity(models.Model):
    name = models.CharField(max_length=100)

class Image(models.Model):
    celebrity = models.ForeignKey(Celebrity, on_delete=models.CASCADE)
    image = models.ImageField()

