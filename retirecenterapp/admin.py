from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Apartment, Apt_Resident, Order, Assign_Order, OrderComment

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

class ApartmentList(admin.ModelAdmin):
    list_display = ('aptBuilding', 'aptRoomNum', 'aptFloor')
    list_filter = ('aptBuilding',)
    search_fields = ('aptBuilding','aptRoomNum','aptFloor')
    ordering = ['id']

class OrderList(admin.ModelAdmin):
    list_display = ( 'aptID', 'ordPriority', 'ordStatus','ordDescription','ordProbType')
    list_filter = ( 'aptID', 'ordStatus')
    search_fields = ('aptID', )
    ordering = ['aptID']

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Profile)
admin.site.register(Apartment, ApartmentList)
admin.site.register(Apt_Resident)
admin.site.register(Order, OrderList)
admin.site.register(Assign_Order)
admin.site.register(OrderComment)