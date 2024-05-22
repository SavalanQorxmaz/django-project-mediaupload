from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Slider, Project, Photos,Contact,Logo

# Create your views here.


# def contacts(request):

#   contacts = Contact.objects.all().values()
#   template = loader.get_template('*.html')
#   context = {
#     'contacts':contacts
#   }
#   return HttpResponse(template.render(context,request))


# __________________________index page_________________

def main(request):

  slider = Slider.objects.all().values()
  projects = Project.objects.all().values()
  projectPhotos = Photos.objects.all().values()
  contacts = Contact.objects.all().values()

  projectMinObject = []
  
  projecIdSet = set()
  for project in projects:
    projecIdSet.add(project['id'])
  print(projecIdSet)
  mainPhotos = {}
  for photo in projectPhotos:
    if ('main' in photo['photo_name'] and photo['project_id']  in projecIdSet):

      projecIdSet.remove(photo['project_id'])
      mainPhotos[str(photo['project_id'])] = photo['photo']

  for project in projects:
    index = project['id']
    projectMinObject.append({
      'project_name': project['name'],
      'project_text': project['Description'],
      'project_image':   mainPhotos[str(index)]  if str(index) in mainPhotos else ''
    })
    
  template = loader.get_template('index.html')
  context = {
    'slider':slider,
    'projects': projectMinObject,
    'contacts':contacts
  }

  print(contacts[0])
  
  return HttpResponse(template.render(context,request))

