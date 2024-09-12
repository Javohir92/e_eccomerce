import os
import json
from django.core.management.base import BaseCommand
from the_core.settings.base import BASE_DIR
from common.models import Country


class Command(BaseCommand):
    help = "Load all countries"

    def handle(self, *args, **kwargs):
        print('my path', (os.path.abspath(BASE_DIR)))
        print(str(BASE_DIR))
        try:
            print("Hello")
            with open(str(BASE_DIR) + "/data/countries.json", 'r') as f:
                print("Good By")

                countries = json.load(f)
                for country in countries:
                    Country.objects.get_or_create(name=country['name_uz'], code=country['code'])

            self.stdout.write(self.style.SUCCESS("Countries loaded successfully"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
