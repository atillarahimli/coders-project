from django.contrib import admin
from blog.models import News,Category

# Register your models here.

@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ['title','created_date','updated_date','draft','slug']

admin.site.register(Category)
