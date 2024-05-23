from django.urls import path
from . import views

handler404 = views.custom_page_not_found_view

urlpatterns = [
    path('', views.main, name='main'),
    path('contacts', views.main, name='contacts'),
    path('project/<int:id>', views.project, name='project'),
    
    # path('*',views.custom_page_not_found_view, name = '404'),
]