import requests
import time
from foods.models import Offer, Restarantinfo
from django.core.management.base import BaseCommand, CommandError

def api_fetcher(restaurant):
    params = {'term':restaurant,'location':'IL', 'limit': 1 }
    url = "https://api.yelp.com/v3/businesses/search"
    headers = {"Authorization": "Bearer 6vtgmwC33wmcUCZZuMv9YK_7d_UjTA2G7L8VuVBfQ7fXdE8E4dIVMQ1NXbmbKvK4UJafETmOUA4d1KZs508R_6sUNr2ovTRdRWOhHsyJ0WtRA20JGO8yLCO9eClQYHYx"}
    r = requests.get(url,params=params, headers = headers)
    print(r)
    rest = r.json()
    data = rest["businesses"][0]
    rest_name = data["name"]
    rest_image = data["image_url"]
    rest_cuisine = data["categories"][0]["alias"]
    is_closed = data["is_closed"]
    price = data["price"]
    phone = data["phone"]
    address = data["location"]["address1"]
    zip_code = data["location"]["zip_code"]
    city = data["location"]["city"] 
    new_dict = {"rest_name" : rest_name, "rest_image": rest_image, "rest_cuisine" : rest_cuisine, "is_closed" : is_closed, "price" : price, "phone" : phone, "address" : address, "zip_code" : zip_code, "city" : city}
    return new_dict

class Command(BaseCommand):
    def handle(self, *args, **options):
        offers = Offer.objects.filter(source = "Grubhub")
        print(offers)
        offers = [(i.rest_name, i) for i in offers]   #rest name from Offers, named same in restaurantinfo
        print(offers)
        for restaurant, obj in offers:
            try:    
                data = api_fetcher(restaurant)
                print(data)
                rest, created = Restarantinfo.objects.get_or_create(
                            rest_name = data['rest_name'],
                            rest_image = data['rest_image'],
                            is_closed = data['is_closed'],
                            cuisines = data['rest_cuisine'],
                            price = data['price'],
                            phone = data['phone'],
                            address = data['address'],
                            city = data['city'],
                            zip_code = data['zip_code'],
                            offer = obj
                    )
                print(rest, created)
            except:
                print("couldnt fetch", restaurant)
            time.sleep(10)        