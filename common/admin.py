from django.contrib import admin
from .models import Country, CustomerFeedback, Media, OurInstagramStory, Region, Settings


class CustomerFeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'customer_position', 'rank']
    search_fields = ['customer_name', 'customer_position']
    list_filter = ['rank']

    def has_add_permission(self, request):
        return False


# Register your models here.
admin.site.register(Country)
admin.site.register(Media)
admin.site.register(OurInstagramStory)
admin.site.register(Region)
admin.site.register(Settings)
admin.site.register(CustomerFeedback, CustomerFeedbackAdmin)
