from django.contrib import admin
from .models import Campaign
from .models import Priorities
from .models import priorityExamples
from .models import Meet
from .models import Testimonials
from .models import Products
from .models import UserProfile
from .models import News
from .models import Event
from .models import Mission

admin.site.register(Campaign)
admin.site.register(Priorities)
admin.site.register(priorityExamples)
admin.site.register(Meet)
admin.site.register(Testimonials)
admin.site.register(Products)
admin.site.register(News)
admin.site.register(Event)
admin.site.register(Mission)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'zip_code', 'checkboxes', 'comments')
    list_filter = ('zip_code', 'checkboxes')
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(UserProfile, UserProfileAdmin)
