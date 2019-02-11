from django.contrib import admin
from . models import graduator
from .models import portfolio
from .models import internshipExperience
# Register your models here.

class graduatorAdmin(admin.ModelAdmin):
    class Meta:
        model = graduator

admin.site.register(graduator, graduatorAdmin)
admin.site.register(portfolio)
admin.site.register(internshipExperience)
