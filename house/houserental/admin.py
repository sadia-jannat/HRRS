from django.contrib import admin

# Register your models here.


#ownerformfill register
from  .models import ownerformfill  
@admin.register(ownerformfill)

class ownerformadmin(admin.ModelAdmin):
    list_display= ('id', 'ownername', 'email', 'phn',  'housecategory','housename','houserent','img','imgidfont','imgidback',
    'division','district', 'area', 'housesize', 'bedroom', 'dinning', 'drawing', 'bathroom', 'kitchen', 
    'balcony', 'allinfo' )


#rating register for model houserate
from .models import houserate
@admin.register(houserate)
class houseratereg(admin.ModelAdmin):
    list_display=('infor_id', 'info_review', 'info_rate', 'get_info_rate')



#again map add..work
from .models import map
@admin.register(map)
class mymapreg(admin.ModelAdmin):
    list_display=()
  
    
#auto Location model try
from .models import Location
@admin.register(Location)
class Locationreg(admin.ModelAdmin):
    list_display=()    