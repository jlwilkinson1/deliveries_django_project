from django.db import models
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Offer, Restarantinfo
# Create your views here.


class OfferListView(ListView):
    model = Offer

class DeliveryListView(ListView):
    model = Offer
    template_name = "foods/doordash_list.html"
    def get_context_data(self, *args, **kwargs):
        context = super(DeliveryListView, self).get_context_data(*args, **kwargs)
        queryset = Offer.objects.filter(source = "Doordash")
        context ["source"] = queryset
        return context

class DeliveryListViewGH(ListView):
    model = Offer
    template_name = "foods/grubhub_list.html"
    def get_context_data(self, *args, **kwargs):
        context = super(DeliveryListViewGH, self).get_context_data(*args, **kwargs)
        queryset = Offer.objects.filter(source = "Grubhub")
        context ["source"] = queryset
        return context

class RestaurantDetailView(DetailView):
    model = Restarantinfo
    template_name = "foods/rest_detail.html"
    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
        #print("Hello Hello Hello",self.requests)
        instance  = self.get_object()
        restaurant = Restarantinfo.objects.get(pk = instance.pk)
        offers = Offer.objects.filter(rest_name = restaurant.rest_name)
        context["dining_name"] = restaurant
        context["dining_offers"] = offers
        context["number_of_offers"] = offers.count()
        return context
       # queryset = Offer.objects.filter(rest_name = )
       # context ["rest_name"] = queryset
       # return context
   # I want the home page to be a list of the carriers and
   # possibly the cuisines. Title and brief description of
   # the webpage as the header, larger icons as links to 
   # specific delivery services(grubhub, doordash, etc.) While 
   # Always having the option to filter by cuisine(navbar?).
   # Clicking into a Delivery service will automatically pull
   # The information for any of the deals in your area through
   # That service. From there you can look at details and 
   # Eventually link to the page to initiate the ordering
   # process with the proper service.

    #Home page -> carriers/or cuisines -> user sees restaurants and deals

    #
    
    # Another Idea is having 4 main icons on the start page. 
    # DD, GH, UE, and one for all deals. I was told that 
    # Postmates is a lot more popular within cities, so maybe
    # 4 main icons with the services, and one more spanning the bottom
    # for all deals.

    #goal to be done on tuesday or wednesday
    #get doordash working first