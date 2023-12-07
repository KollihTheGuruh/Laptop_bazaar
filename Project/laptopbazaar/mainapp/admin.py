from django.contrib import admin
from .models import Laptop, User, Client, Customer, Order

# Customize how laptops are displayed in the admin
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'processor')
    list_filter = ('brand', 'processor')
    search_fields = ('brand', 'model')

# Customize how orders are displayed
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'laptop', 'order_date', 'status')
    list_filter = ('order_date', 'status')
    search_fields = ('customer__user__username', 'laptop__brand', 'laptop__model')

# Register your models here
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
