import json
from django.core.management.base import BaseCommand
from common.models import Region, Country
from the_core.settings.base import BASE_DIR


class Command(BaseCommand):
    help = 'Load all Regions'

    def handle(self, *args, **kwargs):
        # load all regions
        try:
            with open(str(BASE_DIR) + '/data/region.json', 'r') as file:
                regions = json.load(file)
                country = Country.objects.get(name="O'zbakiston", code="UZ")
                for region in regions:
                    Region.objects.get_or_create(name=region['name_uz'], country=country)

                self.stdout.write(self.style.SUCCESS("All regions are loaded successfully"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
