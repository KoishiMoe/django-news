from django.contrib import admin

# Register your models here.


from .models import Chart, Market


admin.site.register(Chart)
admin.site.register(Market)
