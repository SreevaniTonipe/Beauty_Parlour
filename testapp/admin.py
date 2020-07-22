from django.contrib import admin
from testapp.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','phoneNo','email','message']

admin.site.register(Contact,ContactAdmin)    
