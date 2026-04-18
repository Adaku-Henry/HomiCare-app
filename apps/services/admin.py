from django.contrib import admin
from .models import ServiceCategory, Service, ServiceTag, ServiceTagMapping


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):

    list_display = ("name", "is_active", "created_at")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ServiceInline]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "base_price",
        "is_featured",
        "is_available",
        "popularity_score",
    )

    list_filter = ("category", "is_featured", "is_available")

    search_fields = ("name", "description")

    prepopulated_fields = {"slug": ("name",)}


admin.site.register(ServiceTag)
admin.site.register(ServiceTagMapping)