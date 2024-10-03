
from django.contrib import admin
from django.urls import path, include


# courseresource = CourceResource()
# categoryresource = CategoryResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include('shop.urls')),
    path('api/',include('api.urls')),
#     path('api/',include(courseresource.urls)),
#     path('api/',include(categoryresource.urls)),
    
 ]
