from django.contrib import admin

# Register your models here.
from .models import dashboard

class dashboardAdmin(admin.ModelAdmin):
	class Meta:
		model = dashboard

admin.site.register(dashboard,dashboardAdmin)
