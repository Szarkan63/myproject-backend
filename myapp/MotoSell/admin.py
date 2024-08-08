
from django.contrib import admin
from .models import Vehicle  # Import the Vehicle model
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'category', 'brand', 'model', 'year', 'mileage', 'engine_capacity', 'power', 'fuel_type', 'user', 'date_added', 'date_published'
    )
    search_fields = ('title', 'description', 'brand', 'model', 'user__username')  # Adjust the search fields as needed

