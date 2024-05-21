from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Slider, Project, Photos

# Create your views here.



def main(request):

  slider = Slider.objects.all().values()
  projects = Project.objects.all().values()
  projectPhotos = Photos.objects.all().values()

  selectedPictures = []
  projectMinObject = []
  
  projecIdSet = set()
  for project in projects:
    projecIdSet.add(project['id'])
  mainPhotos = []
  for photo in projectPhotos:
    # print(projecIdSet)
    # print(projectPhotos)
    if ('main' in photo['photo_name'] and photo['project_id']  in projecIdSet):

      projecIdSet.remove(photo['project_id'])
      mainPhotos.append(photo)
  #     mainPhotos.add(photo) 
  def check_if_photo_in_project(id):
    returnedPhoto =''
    for photo in mainPhotos:
      # print(photo.filter(id = project['project_id']).values()[0])
      if photo['project_id'] == id:
        returnedPhoto = photo['photo']
      # print(mainPhotos)
      return returnedPhoto

  for project in projects:
    projectMinObject.append({
      'project_name': project['name'],
      'project_text': project['Description'],
      'project_image': check_if_photo_in_project(project['id'])
    })
    # print(projects.filter(id = project['project_id']).values()[0]['id'])
    # print(projectMinObject)
  
    
  template = loader.get_template('index.html')
  context = {
    'slider':slider,
    'projects': projectMinObject
  }
  print(mainPhotos)
  
  return HttpResponse(template.render(context,request))

