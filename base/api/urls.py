from django.urls import path, include
from api.models import CourceResource, CategoryResource
from tastypie.api import Api

api = Api(api_name='v1')
api.register(CourceResource())
api.register(CategoryResource())

urlpatterns = [
    path('',include(api.urls)),
    
]
