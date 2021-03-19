from foods.models import Offer
import csv
with open(r"S:\foodproject\foodproject\utils\foodoffers.csv", encoding = "utf-8") as csv_file:
    data = csv.reader(csv_file, delimiter= ',')
    for line in data:
        if len(line)>0:
            restaurant, offer, rating = line
            rating = float(rating)
            print(restaurant, offer, rating)
            rest, created = Offer.objects.get_or_create(
                rest_name = restaurant,
                rest_offer = offer,
                rating = rating,
                source = "Doordash"
            )
            print(rest, created)