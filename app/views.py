from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Slider, Project, Photos,Contact,Logo

# Create your views here.
def custom_page_not_found_view(request, exception):
    if HttpResponse.status_code == 400:
      return render(request, "404.html", {})


def main(request):

  slider = Slider.objects.all().values()
  projects = Project.objects.all().values()
  projectPhotos = Photos.objects.all().values()
  contacts = Contact.objects.all().values()
  logo = Logo.objects.all().values()[0]

  projectMinObject = []
  
  projecIdSet = set()
  for project in projects:
    projecIdSet.add(project['id'])
  mainPhotos = {}
  for photo in projectPhotos:
    if ('main' in photo['photo_name'] and photo['project_id']  in projecIdSet):

      projecIdSet.remove(photo['project_id'])
      mainPhotos[str(photo['project_id'])] = photo['photo']

  for project in projects:
    index = project['id']
    projectMinObject.append({
      'id': project['id'],
      'project_name': project['name'],
      'project_text': project['Description'],
      'project_image':   mainPhotos[str(index)]  if str(index) in mainPhotos else ''
    })
    
  template = loader.get_template('index.html')
  context = {
    'slider':slider,
    'projects': projectMinObject,
    'contact':contacts,
    'logo': logo
  }
  # print(logo)
  
  return HttpResponse(template.render(context,request))


def project(request, id):

  logo = Logo.objects.all().values()[0]
  project = Project.objects.get(id=id)
  contacts = Contact.objects.all().values()
  photoList = Photos.objects.all().values().filter(project_id =id)

  template = loader.get_template('project.html')

  context = {
    'logo': logo,
    'project': project,
    'contact':contacts,
    'photos':photoList
  }

  print(photoList)

  return HttpResponse(template.render(context,request))



