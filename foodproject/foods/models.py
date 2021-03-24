from django.db import models
from django.urls import reverse
class Offer(models.Model):
    rest_name = models.CharField(max_length = 200)
    rest_offer = models.CharField(max_length = 200)
    rating = models.FloatField(max_length = 10)
    source = models.URLField(max_length = 200)
    date = models.DateField(auto_now = True)
    active = models.BooleanField(default = True)
    expiration = models.DateField(null = True)

    def __str__(self):
        return "{} {} {}".format(self.rest_name, self.rest_offer, self.source)

    def get_absolute_url(self):
        return reverse("rest_detail", kwargs = {'pk' : self.id})

# Create your models here.
# filter offers by delivery service
# search by cuisine
# 
# 
# brainstorm views

class Restarantinfo(models.Model):
    rest_name = models.CharField(max_length = 200, default = '') 
    rest_image = models.ImageField(blank = True, default = 'foods/placehold_stock.jpg') 
    is_closed = models.BooleanField(default = False) 
    deliveries = models.BooleanField(default = True)
    pickup = models.BooleanField(default = True)
    cuisines = models.CharField(max_length = 200) 
    price = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200) 
    zip_code = models.PositiveSmallIntegerField()  
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.rest_name, self.cuisines, self.city)
