from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Placements)
admin.site.register(Announcements)



class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['user','number','email',]
    exclude=['password']
    list_display=['user','full_name']

    
    fieldsets = (
        (None, {
            'fields': ('user',),
        }),

        ('Contact Details', {
            'fields': ('email', 'number','whatsapp_number'),
        }),

        ('Personal Details', {
            'fields': ('full_name','about_me','quote','graduation_year'),
        }),

       

        ('Professional Details', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('designation','company_name','tools_and_techonologies'),
        }),

        ('Documents', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('proof','offer_letter'),
        }),

        ('Socials', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('linkedin','socials'),
        }),
    )
admin.site.register(Profile,ProfileAdmin)
