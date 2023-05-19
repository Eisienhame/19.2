from django.core.management import BaseCommand
from catalog.models import Category, Products
import psycopg2, os

class Command(BaseCommand):
    def handle(self, *args, **options):
        with psycopg2.connect(
                host="localhost",
                database="lesson20",
                user="postgres",
                password=os.getenv('bd_pass')) as conn:
            with conn.cursor() as cur:
                cur.execute('truncate table catalog_product, catalog_category')

        categories_list = [
            {"name": "fruits", "description": "Фрукты"},
            {"name": "Sweet", "description": "Сладкое"},
            {"name": "Vegetables", "description": "Овощи"},
            {"name": "Telephones", "description": "Телефоны и планшеты"},
            {"name": "Meat", "description": "Мясо"}
        ]
        category_objects = []
        for i in categories_list:
            category_objects.append(Category(**i))

        Category.objects.bulk_create(category_objects)

        product_list = [
            {"name": "mango", "description": "fruits", "preview_image": "products/freshmango.jpg", "category": "fruits", "price": 124,"date_of_creation": "2023-05-14T22:18:42Z","Last_modified_date": "2023-05-14T22:18:42Z"},
            {"name": "banan", "description": "fruits", "preview_image": "products/01banan.jpg", "category": "fruits", "price": 32,"date_of_creation": "2023-05-14T23:18:42Z","Last_modified_date": "2023-05-14T23:18:42Z"},
            {"name": "Яблоко", "description": "fruits", "preview_image": "products/03яблоко.jpg", "category": "fruits", "price": 14,"date_of_creation": "2023-05-14T24:18:42Z","Last_modified_date": "2023-05-14T24:18:42Z"}
        ]
        product_objects = []
        for i in categories_list:
            product_objects.append(Category(**i))

        Products.objects.bulk_create(product_objects)