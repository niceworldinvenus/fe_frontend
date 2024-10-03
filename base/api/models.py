from django.db import models
from tastypie.resources import ModelResource
from shop.models import Category, Course
from .authenticatoin import customApiKeyAuthentication
from tastypie.authorization import Authorization

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']
        
class CourceResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get','delete','post']   
        authentication = customApiKeyAuthentication()
        authorization = Authorization()

        def hydrate(self,bundle):
            bundle.obj.category_id = bundle.data['category_id']    
            return bundle
        
        def dehydrate(self,bundle):
            bundle.data['category_id'] = bundle.obj.category_id     
            bundle.data['category'] = bundle.obj.category
            return bundle
        
        def dehydrate_title(self,bundle):    
            return bundle.data['title'].upper()

        
