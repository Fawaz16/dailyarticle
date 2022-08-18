from django.contrib import admin
from .models import  Entertainment, Metro, New, Politic, Topic, latest


# Register your models here.
admin.site.register(Topic)
admin.site.register(Politic)
admin.site.register(New)
admin.site.register(Metro)
admin.site.register(Entertainment)
admin.site.register(latest)
