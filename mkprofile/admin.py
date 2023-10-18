from django.contrib import admin
from .models import Campaign
from .models import Priorities
from .models import priorityExamples
from .models import Meet
from .models import Testimonials
from .models import Products


admin.site.register(Campaign)
admin.site.register(Priorities)
admin.site.register(priorityExamples)
admin.site.register(Meet)
admin.site.register(Testimonials)
admin.site.register(Products)

