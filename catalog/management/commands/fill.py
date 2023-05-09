from django.core.management import BaseCommand
from catalog.models import Category
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