from django.contrib import admin
from .models import Department,Courses,Order

# Register your models here.
admin.site.register(Department)
admin.site.register(Courses)
admin.site.register(Order)
