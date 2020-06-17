from django.contrib import admin
from django.urls import path, include
#from app.views import apiViewSet
from rest_framework import routers,viewsets
from rest_framework.authtoken import views

#router = routers.DefaultRouter()
#router.register(r'', apiViewSet)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    #path('api/', include(router.urls)),
    #path('urls/', include('rest_framework.urls')),
    path('',include('app.urls')),
    path('',include('accounts.urls')),
    path('gettoken/', views.obtain_auth_token)
]
