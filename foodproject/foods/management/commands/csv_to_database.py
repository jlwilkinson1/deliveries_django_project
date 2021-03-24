import requests
import time
from foods.models import Offer, Restarantinfo
from django.core.management.base import BaseCommand, CommandError
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        offers = Offer.objects.all()
        with open(r"S:\foodproject\foodproject\foods\management\commands\grubhub.csv", encoding = "utf-8") as csv_file:
            data = csv.reader(csv_file, delimiter= ',')
            for line in data:
                if len(line)>0:
                    restaurant, offer, cuisine = line
                    print(restaurant, offer, cuisine)
                    rest, created = Offer.objects.get_or_create(
                        rest_name = restaurant,
                        rating = 0.0,
                        rest_offer = offer,
                        source = "Grubhub"
                    )
                    print(rest, created)