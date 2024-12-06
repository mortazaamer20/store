from django.contrib import admin
from .models import Category, Product, ProductImage,Projects

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of empty image fields shown by default

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_AR', 'category','pdf_file','tag')
    search_fields = ('name_AR','category','tag')
    list_filter = ('category',)
    inlines = [ProductImageInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_AR', 'parent')
    search_fields = ('name_AR','name_EN')
    list_filter = ('parent',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name_EN', 'name_AR')
    search_fields = ('name_EN', 'name_AR')




admin.site.site_title = "ادارة الموقع"
admin.site.site_header = "ادارة الموقع"