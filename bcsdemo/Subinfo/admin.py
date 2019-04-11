from django.contrib import admin

from .models import subjects,subcatagory,contcatagory,contentelement,question,contenttabletitle,contentelementimage,contenttableinfo,types
# Register your models here.
admin.site.register(subjects)
admin.site.register(subcatagory)
admin.site.register(contcatagory)
admin.site.register(contentelement)
admin.site.register(question)
admin.site.register(contenttableinfo)
admin.site.register(contenttabletitle)
admin.site.register(contentelementimage)
admin.site.register(types)
