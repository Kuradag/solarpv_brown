from django.contrib import admin
from .models import Product, Certificate, Service, Location, User, TestStandard, Client

# Register your models here.
admin.site.register(Product)
admin.site.register(Certificate)
admin.site.register(Service)
admin.site.register(Location)
admin.site.register(User)
admin.site.register(TestStandard)
admin.site.register(Client)
