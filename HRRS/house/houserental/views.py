from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
#add first create
from django.contrib import admin
from houserental import views
#we need all time for views.py
from urllib import request
from django.http.response import HttpResponseRedirect, JsonResponse,json
from django.shortcuts import redirect,render, get_object_or_404
from django.contrib import messages
#query ar jonno
from django.db.models import Q

#django.db.model all item need for use
from django.db.models import Avg, Max, Min, Count
#from numpy import product

#google map ar jonno
#from __future__ import division
from multiprocessing import context
from turtle import color
from unittest import result
from django.db.models import Q
import folium
import geocoder
import json

#project ar jonno django thyk nea table, models, bellow all 
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import Create
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# all models and forms name add korar jonno * use kora jay
from .models import *
from .forms import *

#models and forms class ar name dity hoy
from .models import ownerformfill,houserate
from .forms import ownerformfillform,houserateform


def home(request):
    return render(request,"home.html")

def ownersignup(request):
     form=Create()
    
     if request.method == "POST":
        form=Create(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account create successfully!!')
            
     context={'form':form}  
     return render(request,"ownersignup.html",context)

login_result=1
def ownerlogin(request):
    if request.method == "POST":       
        username=request.POST.get('username')
        password=request.POST.get('password') 
        user=authenticate(request, username=username, password=password)

        if user is not None:
            global login_result
            login_result=0
            
            login(request,user)

            return redirect('/') #.ata active hoise

        else:
            messages.info(request,'Username and password incorrect')
    return render(request,"ownerlogin.html")

def ownerlogout(request):
    logout(request)
    return redirect('/')

def fillupform(request):
    
    if request.method =="POST":
        po=ownerformfill()

        po.ownername = request.POST.get('ownername')
        po.email = request.POST.get('email')
        po.phn=request.POST.get('phn')
        
        po.housecategory = request.POST.get('housecategory')
        po.housename = request.POST.get('housename')
        po.houserent=request.POST.get('houserent')

        po.division = request.POST.get('division')
        po.district = request.POST.get('district')
        po.area = request.POST.get('area')
        po.housesize = request.POST.get('housesize')
        

        po.bedroom = request.POST.get('bedroom')
        po.dinning = request.POST.get('dinning')
        po.drawing = request.POST.get('drawing')
        po.bathroom = request.POST.get('bathroom')
        po.kitchen = request.POST.get('kitchen')
        po.balcony = request.POST.get('balcony')

        po.allinfo=request.POST.get('allinfo')
             

        if len(request.FILES) != 0:
            po.img=request.FILES['img']
            po.imgidfont=request.FILES['imgidfont']
            po.imgidback=request.FILES['imgidback']
    
        
        po.save()   

        messages.info(request,'Your data added successfully!!')

    return render(request, 'fillupform.html')


house_list = []
def details(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            global house_list
            house_list = ownerformfill.objects.filter(area__icontains=query).order_by('housesize', 'houserent')

        else:
            house_list = ownerformfill.objects.all().order_by('houserent', 'housesize')     

    context={'house_list':house_list,
             
            'login_result':login_result,
         }
    return render(request, 'details.html', context)


####### AutoSearch API ######..work
def auto_house(request):
    if request.is_ajax():
        q = request.GET.get('term')
        places = ownerformfill.objects.filter(area__icontains=q)
        results = []
        for pl in places:
            place_json = {}
            place_json = pl.area
            results.append(place_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


house_list = []
def alldetails(request):
    max_price = request.GET.get('max_price')
    min_price = request.GET.get('min_price')
    max_room = request.GET.get('max_room')
    min_room = request.GET.get('min_room')
    max_bedroom = request.GET.get('max_bed')
    min_bedroom = request.GET.get('min_bed')
    print(min_price, max_price)
    
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            global house_list
            house_list = ownerformfill.objects.filter(area__icontains=query, houserent__range=(min_price, max_price),
                                                     bedroom__range=(min_room, max_room),
                                                     bathroom__range=(min_bedroom, max_bedroom))
            
            
            return render(request, 'alldetails.html',
                          {'house_list': house_list,  'login_result': login_result})
            
            
def homedetails(request,pk):
    fe=ownerformfill.objects.get(id=pk)  #primary key(pk) ja oi key ar details dekhabe

    #query ar maddhomy search k nia details dekha.min and max
    min_range = fe.houserent-2000
    max_range = fe.houserent+2000
    global house_list
    house_list = ownerformfill.objects.filter(houserent__range=[min_range, max_range])
    
    ratevariable=houserateform()        #amar rate ai product ar jonno create form name houserateform

    #canAdd for rate model ar check ar jonno koyta star use korse
    canAdd=True
    reviewcheck=houserate.objects.filter(infor_id=fe).count()   #ai fe ta info ar uporer fe k bujayse..it is user variable upore..r infor_id ta houserate model ar foreng variable thyk nea
    if reviewcheck>0:
        canAdd=False
    

    #fetch review and rate from houserate model in this primary key of ownerformfill model thyk.fe holo primary ownerformfill key ar variable
    reviewfetch=houserate.objects.filter(infor_id=fe)           #infor_id holo houserate ar forengkey.ja ownerformfill thyk nea

    
    #average rating  create
    avg_reviewfetch=houserate.objects.filter(infor_id=fe).aggregate(avg_rate=Avg('info_rate'))


    #success to fetch rating reviews objects===details..ok
    d=houserate.objects.all().order_by('info_rate')


    #check for rate value for recommandation
    if 'r' in request.GET:
        r=request.GET['r']
        rat=houserate.objects.filter(info_rate__icontains=r)
    else:
        rat=houserate.objects.all()  



    #check for houserent and size
    if 'houserentid' in request.GET:
        houserentid=request.GET['houserentid']
        houserentidcheck=ownerformfill.objects.filter(houserent__icontains=houserentid)
    else:
        houserentidcheck=ownerformfill.objects.all()    

    #ok work this owner variable by filter..group a
    owner=ownerformfill.objects.filter(houserent__range=["5000", "20000"], housesize__range=["1000","1500"]).order_by('houserent', 'housesize')



    context={'fe':fe,                               #fe-all detail, fe,ratevariable,canAdd,reviewfetch,avg_reviewfetch all for rating and review work
              'ratevariable':ratevariable,
              'canAdd':canAdd,
              'reviewfetch':reviewfetch,
              'avg_reviewfetch':avg_reviewfetch,

              'd':d,     #try success for fetch rate value..not need
              'rat':rat,  #how much rate need value for people see..not need
              'owner':owner, #ok work this owner variable by filter..group a..not use this
              'houserentidcheck':houserentidcheck,

              'house_list':house_list,     #now this main recommendation use
             
              }
    return render(request, 'homedetails.html', context)                

#rate and review url...ok
def save(request, pid):
    projuct=ownerformfill.objects.get(pk=pid)
    reve=houserate.objects.create(
        infor_id=projuct,
        info_review=request.POST['info_review'],
        info_rate=request.POST['info_rate'],
    )

    data={
        'info_review':request.POST['info_review'],
        'info_rate':request.POST['info_rate'],
    }

    #average rating  create
    avg_reviewfetch=houserate.objects.filter(infor_id=projuct).aggregate(avg_rate=Avg('info_rate'))

    #return JsonResponse({'bool':True, 'data':data, 'avg_reviewfetch':avg_reviewfetch})   #ai line code dily o right ..but success ar jjonno reviewok page create
  
    return HttpResponseRedirect('/reviewok')

def reviewok(request):    
    return render(request, 'reviewok.html')   #only success ar jonno create kora review and rating k


def ourcountry(request):
    address=request.POST.get('address')
    if request.method=='POST':
        form=mapformagain(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/ourcountry')
    else:
        form=mapformagain() 
        
    ##geocoder code
    address=map.objects.all().last()

    location=geocoder.osm(address)
    lat=location.lat
    lng=location.lng
    country=location.country

    #correct area na dily data ty add hobe na.tuturial thyk dekty hobe aber
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('Your location input is invalid')
    
    #create map for bangladesh lat,lng and location num ok
    m=folium.Map(location=[23.684994, 90.356331], zoom_start=4)
 
    folium.Marker([lat, lng], tooltip='click for more', icon=folium.Icon(color='green', icon='cloud'), popup=country).add_to(m)

    #we can want to add 8 division marker map to our creat map
    folium.Marker(location=[24.903561,91.873611], tooltip='click for more', icon=folium.Icon(color='red', icon='envelope'), popup="<strong>Sylhet</strong>").add_to(m)
    folium.Marker(location=[24.098379,90.328712], tooltip='click for more', icon=folium.Icon(color='red', icon='cloud'), popup="<strong>Dhaka</strong>").add_to(m)
    #baki gula per day ty nity hobe
    folium.Marker(location=[24.376930,88.603073], tooltip='click for more', icon=folium.Icon(color='red', icon='envelope'), popup="<strong>Rajshahi</strong>").add_to(m)
    folium.Marker(location=[22.841930,89.558060], tooltip='click for more', icon=folium.Icon(color='red', icon='cloud'), popup="<strong>Khulna</strong>").add_to(m)
    folium.Marker(location=[22.700411,90.374992], tooltip='click for more', icon=folium.Icon(color='red', icon='envelope'), popup="<strong>Barishal</strong>").add_to(m)
    folium.Marker(location=[22.330370,91.832626], tooltip='click for more', icon=folium.Icon(color='red', icon='cloud'), popup="<strong>Chittagong</strong>").add_to(m)
    folium.Marker(location=[24.744221,90.403008], tooltip='click for more', icon=folium.Icon(color='red', icon='envelope'), popup="<strong>Mymensingh</strong>").add_to(m)
    folium.Marker(location=[25.740580,89.261139], tooltip='click for more', icon=folium.Icon(color='red', icon='cloud'), popup="<strong>Rangpur</strong>").add_to(m)


    m=m._repr_html_()
    context={
        'm':m,
        'form':form,
    } 
    return render(request, 'ourcountry.html', context)

#this recommandation_details page need for our project
def recommandation_details(request, pk):

    fe=ownerformfill.objects.get(id=pk)
    
    context={
        'fe':fe,
    }
    return render(request, 'recommandation_details.html', context)
          

def admindashboard(request):
    if request.method =="POST":
        a=request.POST.get('houserent')
        b=request.POST.get('housesize')
        formfetch=ownerformfill.objects.all()
    else:
        formfetch=ownerformfill.objects.all()
    

    return render(request, 'admindashboard.html',{'formfetch':formfetch} )

#edit page ta dui ta model ar edit ar kaj korse.use edit.html
def admindashbord_edit(request, id):
    if request.method == 'POST':
         pi=ownerformfill.objects.get(pk=id)
         fm=ownerformfillform(request.POST, instance=pi)
         if fm.is_valid():
             fm.save()  

    else:
           pi=ownerformfill.objects.get(pk=id)
           fm=ownerformfillform(instance=pi)
            
    return render(request, 'edit.html', {'fo':fm})   


def admindashbord_delete(request,id):
    if request.method == 'POST':
        pi=ownerformfill.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/admindashboard')