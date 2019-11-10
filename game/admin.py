from django.contrib import admin
from .models import HardQuestion, MediumQuestion, EasyQuestion

admin.site.register(HardQuestion)
admin.site.register(MediumQuestion)
admin.site.register(EasyQuestion)
