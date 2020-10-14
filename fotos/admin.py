from django.contrib import admin
from .models import Image, Location, Category

admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)


# class DetailsAdmin(admin.ModelAdmin):
#     filter_horizontal =('location',)

# admin.site.register(Category)
# admin.site.register(Details,DetailsAdmin)
# admin.site.register(location)