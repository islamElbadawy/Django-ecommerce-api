import json
from .models import Product

with open('data.json') as f:
    json_data = json.load(f)
    print(json_data[0])

    for item in json_data['products']:
        product = Product(
            title=item['title'],
            price=item['price'],
            image=item['image'],
            rating=item['rating'],
            url=item['url'],
            category=item['category'],
            brand=item['brand'],
            user = item['user'],
            createdAt = item['createdAt'],
            stock = item['stock']
        )
        product.save()