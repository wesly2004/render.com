from rest_framework import routers
from .api import ProjectViewSet
from django.urls import path, include

routers = routers.DefaultRouter()
routers.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = routers.urls
