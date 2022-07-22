from django.db import models

# Create your models here.
#image ar time ,date debr jonno bellow
import datetime
import os

#ownerformfill new create
#division ar list
DIVISION=(                #dity pari nai ata
    ('Dhaka', 'Dhaka'),
    ('Chattogram', 'Chattogram'),
    (' Khulna', ' Khulna'),
    ('Barishal', 'Barishal'),
    ('Rajshahi', 'Rajshahi'),
    ('Sylhet', 'Sylhet'),
    ('Rangpur', 'Rangpur'),
    ('Mymensingh', 'Mymensingh'),
)

#img ar jonno
def fileimg(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

#house-category for ownerformfill model ar..work
HOUSE_CATEGORY=(                
    ('flat', 'flat'),
    ('duplex', 'duplex'),
    ('commercial', ' commercial'),
    ('family_house', 'family_house'),
   
)
class ownerformfill(models.Model):
    ownername=models.CharField(max_length=100)
    email=models.EmailField()
    phn=models.IntegerField()    

    housecategory=models.CharField(choices=HOUSE_CATEGORY, max_length=200)
    housename=models.CharField(max_length=100)

    houserent=models.PositiveIntegerField(default=0)
    
    img=models.ImageField(upload_to=fileimg, null=True, blank=True )
    imgidfont=models.ImageField(upload_to=fileimg, null=True, blank=True )
    imgidback=models.ImageField(upload_to=fileimg, null=True, blank=True )
    

    division=models.CharField(max_length=50)   #select dity pari nai..tai choices=DIVIDSION cut korlm
    district=models.CharField(max_length=100) 
    area=models.CharField(max_length=250, verbose_name='Area', blank=True)
    

    housesize=models.CharField(max_length=100)
    bedroom=models.PositiveIntegerField(default=0)
    dinning=models.PositiveIntegerField(default=0)
    drawing=models.PositiveIntegerField(default=0)
    bathroom=models.PositiveIntegerField(default=0) 
    kitchen=models.PositiveIntegerField(default=0)
    balcony=models.PositiveIntegerField(default=0)

    allinfo=models.CharField(max_length=100) 
     
    class Meta:
        verbose_name = "Ownerformfill"
        verbose_name_plural = "Ownerformfill"


#RATE AR RAVIEWS AR JONNO
RATING=(
(1, '1'),
(2, '2'),
(3, '3'),
(4, '4'),
(5, '5'),
)

class houserate(models.Model):
    infor_id=models.ForeignKey(ownerformfill, on_delete=models.CASCADE)
    info_review=models.TextField()
    info_rate=models.CharField(choices=RATING, max_length=100)

    def get_info_rate(self):
        return self.info_rate        

#map ar jonno
#again try map..work
class map(models.Model):
    address=models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.address    


#Auto search for location last try..not work
class Location(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self) -> str:
       return self.name    