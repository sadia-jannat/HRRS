"""house URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from unicodedata import name

#houserental app to use views add
from houserental import views
#image add ar jonno
from django.conf import settings
from django.conf.urls.static import static

#API
from houserental.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name="home"),
    path('ownersignup/', views.ownersignup, name="ownersignup"),
    path('ownerlogin/', views.ownerlogin, name="ownerlogin"),
    path('logout/', views.logout, name="logout"),
    path('fillupform/', views.fillupform, name="fillupform"),
    path('details/', views.details, name="details"),
    path('alldetails/', views.alldetails, name="alldetails"),
    path('homedetails/<str:pk>', views.homedetails, name='homedetails'),
    path('save/<int:pid>', views.save, name='save'),
    path('reviewok/', views.reviewok, name='reviewok'),
    path('ourcountry/', views.ourcountry, name="ourcountry"),
    path('recommandation_details/<str:pk>', views.recommandation_details, name="recommandation_details"), 
    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('admindashbord_edit/<int:id>/', views.admindashbord_edit, name='admindashbord_edit'),
    path('admindashbord_delete/<int:id>/', views.admindashbord_delete, name='admindashbord_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
